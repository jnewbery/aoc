static TEST: bool = false;

use std::cmp::Ordering;
use std::collections::BinaryHeap;
use std::collections::HashSet;
use aoc::utils::Point;

static _TEST_INPUT: &str = include_str!("../../../inputs/test/202418.txt");
static _INPUT: &str = include_str!("../../../inputs/full/202418.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };
const GRID_SIZE: usize = if TEST {7} else {71};

const DIRECTIONS: [(i32, i32); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];

#[derive(Copy, Clone, Eq, PartialEq)]
struct State {
    steps: i32,
    point: Point,
}

// Implement the ordering of the states to make this a min-heap
impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other.steps.cmp(&self.steps)
            .then_with(|| self.point.cmp(&other.point))
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

fn shortest_path(walls: &HashSet<Point>) -> bool {
    let mut visited: HashSet<Point> = HashSet::new();
    let mut heap = BinaryHeap::new();
    heap.push(State { steps: 0, point: Point { x: 0, y: 0 } });

    loop {
        let state = heap.pop();
        if state.is_none() {
            return false;
        }
        let state = state.unwrap();
        let steps = state.steps;
        let point = state.point;
        // println!("Visiting {:?}: {} steps", position, steps);
        // println!("heap: {:?}", heap);
        // println!("visited: {:?}", visited);
        if visited.contains(&point) {
            continue;
        }
        visited.insert(point);

        if point == (Point { x: GRID_SIZE as i32 - 1, y: GRID_SIZE as i32 - 1 }) {
            return true;
        }

        for dir in DIRECTIONS {
            let next = Point { x: point.x + dir.0, y: point.y + dir.1 };
            if !walls.contains(&next) && !visited.contains(&next) && next.x >= 0 && next.y >= 0 && next.x < GRID_SIZE as i32 && next.y < GRID_SIZE as i32 {
                heap.push(State { steps: steps + 1, point: next });
            }
        }
    }
}

pub fn solve_202418_2() -> String {
    let walls: Vec<Point> = INPUT.lines()
        .map(|line| {
            let coords: Vec<u32> = line.split(',').map(|s| s.parse::<u32>().unwrap()).collect();
            Point {x: coords[0] as i32, y: coords[1] as i32}
        })
        .collect();
    // println!("{:?}", walls);

    let (mut min, mut max) = (0, walls.len() as i32);

    // Binary search for the first wall that blocks the path
    while min + 1 < max {
        let mid = (min + max) / 2;
        // println!("min: {}, max: {}, mid: {}", min, max, mid);
        let result = shortest_path(&walls[0..mid as usize].iter().cloned().collect());
        match result {
            true => {
                // println!("Result: {}", steps);
                min = mid;
            },
            false => {
                // println!("No path found");
                max = mid;
            }
        }
    }
    // println!("{},{}", walls[min as usize].x, walls[min as usize].y);
    format!("{},{}", walls[min as usize].x, walls[min as usize].y)
}
