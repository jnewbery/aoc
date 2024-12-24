use std::cmp::Ordering;
use std::collections::BinaryHeap;
use std::collections::HashSet;
use aoc::utils::Point;

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

fn shortest_path(walls: &HashSet<Point>, grid_size: usize) -> i32 {
    let mut visited: HashSet<Point> = HashSet::new();
    let mut heap = BinaryHeap::new();
    heap.push(State { steps: 0, point: Point { x: 0, y: 0 } });

    loop {
        let state = heap.pop().unwrap();
        let steps = state.steps;
        let point = state.point;
        // println!("Visiting {:?}: {} steps", position, steps);
        // println!("heap: {:?}", heap);
        // println!("visited: {:?}", visited);
        if visited.contains(&point) {
            continue;
        }
        visited.insert(point);

        if point == (Point { x: grid_size as i32 - 1, y: grid_size as i32 - 1 }) {
            return steps;
        }

        for dir in DIRECTIONS {
            let next = Point { x: point.x + dir.0, y: point.y + dir.1 };
            if !walls.contains(&next) && !visited.contains(&next) && next.x >= 0 && next.y >= 0 && next.x < grid_size as i32 && next.y < grid_size as i32 {
                heap.push(State { steps: steps + 1, point: next });
            }
        }
    }
}

pub fn solve_202418_1(input: &str) -> String {
    let grid_size = if input[0..3] == *"5,4" { 7 } else { 71 };
    let num_bytes = if input[0..3] == *"5,4" { 12 } else { 1024 };
    let walls: HashSet<Point> = input.lines()
        .take(num_bytes as usize) // Process only grid_size lines
        .map(|line| {
            let coords: Vec<u32> = line.split(',').map(|s| s.parse::<u32>().unwrap()).collect();
            Point {x: coords[0] as i32, y: coords[1] as i32}
        })
        .collect();
    // println!("{:?}", walls);

    let result = shortest_path(&walls, grid_size);
    // println!("{}", result);
    result.to_string()
}
