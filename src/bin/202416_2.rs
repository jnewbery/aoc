static TEST: bool = false;

use std::cmp::Ordering;
use std::collections::BinaryHeap;
use std::iter::Peekable;
use std::collections::HashSet;
use aoc::utils::{Point, Position};
use std::fmt;

static _TEST_INPUT: &str = include_str!("inputs/202416_test.txt");
static _INPUT: &str = include_str!("inputs/202416.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

struct Maze {
    width: i32,
    height: i32,
    path: HashSet<Point>,
    walls: HashSet<Point>,
    start: Point,
    end: Point,
}

// Implement print for warehouse
impl fmt::Debug for Maze {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        for y in 0..self.height {
            for x in 0..self.width {
                let point = Point { x, y };
                if self.walls.contains(&point) {
                    write!(f, "#")?;
                } else if self.path.contains(&point) {
                    write!(f, "O")?;
                } else if self.start == point {
                    write!(f, "S")?;
                } else if self.end == point {
                    write!(f, "E")?;
                } else {
                    write!(f, " ")?;
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
        path: HashSet::new(),
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

#[derive(Clone, Eq, PartialEq)]
struct State {
    steps: i32,
    position: Position,
    path: HashSet<Point>,
}

// Implement the ordering of the states to make this a min-heap
impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other.steps.cmp(&self.steps)
            .then_with(|| self.position.cmp(&other.position))
            .then_with(|| self.path.clone().into_iter().cmp(other.path.clone().into_iter()))
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

fn shortest_path(maze: &mut Maze) {
    let mut visited: HashSet<Position> = HashSet::new();
    let mut heap = BinaryHeap::new();
    heap.push(State { steps: 0, position: Position::new(maze.start, Point { x: 1, y: 0 }), path: HashSet::from([maze.start]) });
    let mut best_score: Option<i32> = None;

    loop {
        let state = heap.pop().unwrap();
        let steps = state.steps;
        let position = state.position;
        let path = state.path;

        if let Some(mut next_state) = heap.peek_mut() {
            if next_state.steps == steps && next_state.position == position {
                // Merge the set of visited points if there are multiple ways
                // to reach here at the same cost.
                path.iter().for_each(|p| {
                    next_state.path.insert(*p);
                });
                continue;
            }
        }
        if visited.contains(&position) {
            continue;
        }
        if let Some(score) = best_score {
            // The next best position has a higher cost than the best score.
            // We can stop searching.
            if steps > score {
                return;
            }
        }

        if position.location == maze.end {
            // We've reached the end, but there may be other ways to get here.
            for p in path.iter() {
                maze.path.insert(*p);
            }
            maze.path.insert(maze.end);
            best_score = Some(steps);
            continue;
        }
        visited.insert(position);

        let forward = position.forward();
        if !maze.walls.contains(&forward.location) && !visited.contains(&forward) {
            let mut path = path.clone();
            path.insert(position.location);
            heap.push(State { steps: steps + 1, position: forward, path });
        }

        let left = position.turn_left();
        if !visited.contains(&left) {
            let mut path = path.clone();
            path.insert(position.location);
            heap.push(State { steps: steps + 1000, position: left, path });
        }

        let right = position.turn_right();
        if !visited.contains(&right) {
            let mut path = path.clone();
            path.insert(position.location);
            heap.push(State { steps: steps + 1000, position: right, path });
        }
    }
}

fn main() {
    let mut lines = INPUT.lines().peekable();
    let mut maze = get_maze(&mut lines);
    // println!("{:?}", maze);

    shortest_path(&mut maze);
    // println!("{:?}", maze);
    println!("{:?}", maze.path.len());
}
