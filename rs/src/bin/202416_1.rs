static TEST: bool = false;

use std::cmp::Ordering;
use std::collections::BinaryHeap;
use std::iter::Peekable;
use std::collections::HashSet;
use aoc::utils::{Point, Position};
use std::fmt;

static _TEST_INPUT: &str = include_str!("../../../inputs/test/202416.txt");
static _INPUT: &str = include_str!("../../../inputs/full/202416.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

struct Maze {
    width: i32,
    height: i32,
    walls: HashSet<Point>,
    start: Point,
    end: Point,
}

// Implement print for maze
impl fmt::Debug for Maze {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        for y in 0..self.height {
            for x in 0..self.width {
                let point = Point { x, y };
                if self.walls.contains(&point) {
                    write!(f, "#")?;
                } else if self.start == point {
                    write!(f, "S")?;
                } else if self.end == point {
                    write!(f, "E")?;
                } else {
                    write!(f, ".")?;
                }
            }
            writeln!(f)?; // Newline at the end of each row
        }
        Ok(()) // Return success
    }
}

fn get_maze(lines: &mut Peekable<std::str::Lines>) -> Maze {
    let mut maze = Maze {
        width: lines.peek().unwrap().len() as i32,
        height: 0,
        walls: HashSet::new(),
        start: Point { x: 0, y: 0 },
        end: Point { x: 0, y: 0 },
    };

    // Iterate over the lines until a blank line is found
    for (y, line) in lines.enumerate() {
        if line.is_empty() {
            break;
        }
        maze.height += 1;

        for (x, c) in line.chars().enumerate() {
            match c {
                '.' => (),
                '#' => {
                    maze.walls.insert(Point { x: x as i32, y: y as i32 });
                },
                'S' => maze.start = Point { x: x as i32, y: y as i32 },
                'E' => maze.end = Point { x: x as i32, y: y as i32 },
                _ => panic!("Invalid character in input"),
            }
        }
    }

    maze
}

#[derive(Copy, Clone, Eq, PartialEq)]
struct State {
    steps: i32,
    position: Position,
}

// Implement the ordering of the states to make this a min-heap
impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other.steps.cmp(&self.steps)
            .then_with(|| self.position.cmp(&other.position))
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

fn shortest_path(maze: &Maze) -> i32 {
    let mut visited: HashSet<Position> = HashSet::new();
    let mut heap = BinaryHeap::new();
    heap.push(State { steps: 0, position: Position::new(maze.start, Point { x: 1, y: 0 }) });

    loop {
        let state = heap.pop().unwrap();
        let steps = state.steps;
        let position = state.position;
        // println!("Visiting {:?}: {} steps", position, steps);
        // println!("heap: {:?}", heap);
        // println!("visited: {:?}", visited);
        if visited.contains(&position) {
            continue;
        }
        visited.insert(position);

        if position.location == maze.end {
            return steps;
        }

        let forward = position.forward();
        if !maze.walls.contains(&forward.location) && !visited.contains(&forward) {
            heap.push(State { steps: steps + 1, position: forward });
        }

        let left = position.turn_left();
        if !visited.contains(&left) {
            heap.push(State { steps: steps + 1000, position: left });
        }

        let right = position.turn_right();
        if !visited.contains(&right) {
            heap.push(State { steps: steps + 1000, position: right });
        }
    }
}

fn main() {
    let mut lines = INPUT.lines().peekable();
    let maze = get_maze(&mut lines);
    println!("{:?}", maze);

    let shortest = shortest_path(&maze);
    println!("{}", shortest);
}
