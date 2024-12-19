static TEST: bool = false;

use std::fmt;
use std::iter::Peekable;
use std::collections::HashSet;

static _TEST_INPUT: &str = include_str!("inputs/202415_test.txt");
static _INPUT: &str = include_str!("inputs/202415.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
struct Point {
    x: i32,
    y: i32,
}

// Implement addition on Point
impl std::ops::Add for Point {
    type Output = Point;

    fn add(self, other: Point) -> Point {
        Point { x: self.x + other.x, y: self.y + other.y }
    }
}

// Implement multiplication by a scalar on points (i32, i32)
impl std::ops::Mul<i32> for Point {
    type Output = Point;

    fn mul(self, scalar: i32) -> Self {
        Point { x: self.x * scalar, y: self.y * scalar }
    }
}

// Implement scalar multiplication on points (i32, i32)
impl std::ops::Mul<Point> for i32 {
    type Output = Point;

    fn mul(self, point: Point) -> Point {
        Point { x:self * point.x, y:self * point.y }
    }
}

struct Warehouse {
    x: i32,
    y: i32,
    walls: HashSet<Point>,
    left_boxes: HashSet<Point>,
    right_boxes: HashSet<Point>,
    reindeer: Point,
}

// Implement print for warehouse
impl fmt::Debug for Warehouse {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        for y in 0..self.y {
            for x in 0..self.x {
                let point = Point { x, y };
                if self.walls.contains(&point) {
                    write!(f, "#")?;
                } else if self.reindeer == point {
                    write!(f, "@")?;
                } else if self.left_boxes.contains(&point) {
                    write!(f, "[")?;
                } else if self.right_boxes.contains(&point) {
                    write!(f, "]")?;
                } else {
                    write!(f, ".")?;
                }
            }
            writeln!(f)?; // Newline at the end of each row
        }
        Ok(()) // Return success
    }
}

fn get_warehouse(lines: &mut Peekable<std::str::Lines>) -> Warehouse {
    let mut warehouse = Warehouse {
        x: 2 * lines.peek().unwrap().len() as i32,
        y: 0,
        walls: HashSet::new(),
        left_boxes: HashSet::new(),
        right_boxes: HashSet::new(),
        reindeer: Point { x: 0, y: 0 },
    };

    // Iterate over the lines until a blank line is found
    for (y, line) in lines.enumerate() {
        if line.is_empty() {
            break;
        }
        warehouse.y += 1;

        for (x, c) in line.chars().enumerate() {
            match c {
                '.' => (),
                '#' => {
                    warehouse.walls.insert(Point { x: (2 * x) as i32, y: y as i32 });
                    warehouse.walls.insert(Point { x: (2 * x + 1) as i32, y: y as i32 });
                },
                'O' => {
                    warehouse.left_boxes.insert(Point { x: (2 * x) as i32, y: y as i32 });
                    warehouse.right_boxes.insert(Point { x: (2 * x + 1) as i32, y: y as i32 });
                },
                '@' => warehouse.reindeer = Point { x: (2 * x) as i32, y: y as i32 },
                _ => panic!("Invalid character in input"),
            }
        }
    }

    warehouse
}

fn move_reindeer(warehouse: &mut Warehouse, lines: &mut Peekable<std::str::Lines>) {
    for line in lines {
        for c in line.chars() {
            let direction = match c {
                '^' => Point { x: 0, y: -1 },
                '>' => Point { x: 1, y: 0 },
                'v' => Point { x: 0, y: 1 },
                '<' => Point { x: -1, y: 0 },
                _ => panic!("Invalid character in input"),
            };

            let mut frontier: HashSet<Point> = HashSet::from([warehouse.reindeer + direction]);
            let mut left_boxes_to_move: HashSet<Point> = HashSet::new();
            let mut right_boxes_to_move: HashSet<Point> = HashSet::new();

            loop {
                if frontier.intersection(&warehouse.walls).next().is_some() {
                    // Can't move any further
                    break;
                } else if frontier.intersection(&warehouse.left_boxes).next().is_some() || frontier.intersection(&warehouse.right_boxes).next().is_some() {
                    match c {
                        '^' | 'v' => {
                            let new_left_boxes: Vec<Point> = frontier.intersection(&warehouse.left_boxes).cloned().collect();
                            for new_box in new_left_boxes {
                                // Found a box
                                // Add this box to the set of boxes to move
                                left_boxes_to_move.insert(new_box);
                                right_boxes_to_move.insert(new_box + Point { x: 1, y: 0 });
                                frontier.remove(&new_box);
                                frontier.remove(&(new_box + Point { x: 1, y: 0 }));
                                frontier.insert(new_box + direction);
                                frontier.insert(new_box + direction + Point { x: 1, y: 0 });
                            }
                            let new_right_boxes: Vec<Point> = frontier.intersection(&warehouse.right_boxes).cloned().collect();
                            for new_box in new_right_boxes {
                                // Found a box
                                // Add this box to the set of boxes to move
                                right_boxes_to_move.insert(new_box);
                                left_boxes_to_move.insert(new_box + Point { x: -1, y: 0 });
                                frontier.remove(&new_box);
                                frontier.remove(&(new_box + Point { x: -1, y: 0 }));
                                frontier.insert(new_box + direction);
                                frontier.insert(new_box + direction + Point { x: -1, y: 0 });
                            }

                        },
                        '>' => {
                            // Found a box
                            let new_box = frontier.intersection(&warehouse.left_boxes).next().unwrap().clone();
                            left_boxes_to_move.insert(new_box);
                            right_boxes_to_move.insert(new_box + Point { x: 1, y: 0 });
                            frontier.remove(&new_box);
                            frontier.insert(new_box + direction * 2);
                        },
                        '<' => {
                            // Found a box
                            let new_box = frontier.intersection(&warehouse.right_boxes).next().unwrap().clone();
                            right_boxes_to_move.insert(new_box);
                            left_boxes_to_move.insert(new_box + Point { x: -1, y: 0 });
                            frontier.remove(&new_box);
                            frontier.insert(new_box + direction * 2);
                        },
                        _ => panic!()
                    }
                    continue;
                } else {
                    // No boxes in the way - move the boxes and reindeer
                    
                    let mut new_left_boxes: HashSet<Point> = HashSet::new();
                    for box_to_move in &left_boxes_to_move {
                        warehouse.left_boxes.remove(box_to_move);
                        new_left_boxes.insert(*box_to_move + direction);
                    }
                    warehouse.left_boxes = warehouse.left_boxes.union(&new_left_boxes).copied().collect();
                    let mut new_right_boxes: HashSet<Point> = HashSet::new();
                    for box_to_move in &right_boxes_to_move {
                        warehouse.right_boxes.remove(box_to_move);
                        new_right_boxes.insert(*box_to_move + direction);
                    }
                    warehouse.right_boxes = warehouse.right_boxes.union(&new_right_boxes).copied().collect();
                    warehouse.reindeer = warehouse.reindeer + direction;
                    break;
                }
            }
            // println!("{:?}", c);
            // println!("{:?}", warehouse);
            // println!();
        }
    }
}

fn score_warehouse(warehouse: &Warehouse) {
    let mut score = 0;
    for left_box in &warehouse.left_boxes {
        score += 100 * left_box.y + left_box.x;
    }
    println!("Score: {}", score);
}

fn main() {
    // let mut lines: Vec<Vec<char>> = INPUT.lines().map(|line| line.chars().collect()).collect();
    let mut lines = INPUT.lines().peekable();
    let mut warehouse = get_warehouse(&mut lines);
    // println!("{:?}", warehouse);

    move_reindeer(&mut warehouse, &mut lines);

    score_warehouse(&warehouse);
}
