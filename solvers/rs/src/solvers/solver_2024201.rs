use aoc::utils::Point;
use std::collections::{HashSet, HashMap};

const DIRECTIONS: [(i32, i32); 4] = [(0, -1), (0, 1), (-1, 0), (1, 0)];
const TWO_AWAY: [(i32, i32); 8] = [(0, -2), (1, -1), (2, 0), (1, 1), (0, 2), (-1, 1), (-2, 0), (-1, -1)];

struct Maze {
    width: i32,
    height: i32,
    walls: HashSet<Point>,
    start: Point,
    end: Point,
}

fn _print_maze(maze: &Maze, distances: &HashMap<Point, i32>) {
    for y in 0..maze.height {
        for x in 0..maze.width {
            let point = Point { x, y };
            if maze.walls.contains(&point) {
                print!("#");
            } else if maze.start == point {
                print!("S");
            } else if maze.end == point {
                print!("E");
            } else if let Some(distance) = distances.get(&point) {
                print!("{}", distance % 10);
            } else {
                print!(".");
            }
        }
        println!(); // Newline at the end of each row
    }
    println!(); // Extra newline at the end
}

fn get_maze(lines: std::str::Lines) -> Maze {
    let mut maze = Maze {
        width: 0,
        height: 0,
        walls: HashSet::new(),
        start: Point { x: 0, y: 0 },
        end: Point { x: 0, y: 0 },
    };

    for (y, line) in lines.enumerate() {
        maze.height += 1;
        maze.width = line.len() as i32;

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

pub fn solve(input: &str) -> String {
    let min_saving = if input.len() < 1000 { 1 } else { 100 };
    let maze = get_maze(input.lines());
    let mut distances: HashMap<Point, i32> = HashMap::new();
    distances.insert(maze.end, 0);
    // _print_maze(&maze, &distances);

    // BFS to find the distance from the end to every other point
    let mut frontier: HashSet<Point> = HashSet::new();
    frontier.insert(maze.end);
    while !frontier.is_empty() {
        let mut new_frontier: HashSet<Point> = HashSet::new();
        for point in frontier {
            // println!("{:?}", point);
            for (dx, dy) in DIRECTIONS.iter() {
                let new_point = Point { x: point.x + dx, y: point.y + dy };
                if maze.walls.contains(&new_point) {
                    continue;
                }
                if distances.contains_key(&new_point) {
                    continue;
                }
                distances.insert(new_point, distances[&point] + 1);
                new_frontier.insert(new_point);
            }
        }
        frontier = new_frontier;
    }
    // _print_maze(&maze, &distances);

    let mut cheats: HashSet<(Point, Point, i32)> = HashSet::new();
    for (point, distance) in &distances {
        for (dx, dy) in TWO_AWAY.iter() {
            let new_point = Point { x: point.x + dx, y: point.y + dy };
            if maze.walls.contains(&new_point) {
                continue;
            }
            if let Some(&new_distance) = distances.get(&new_point) {
                if new_distance < distance - 2{
                    // println!("cheat from old point {:?} (distance {}) -> new point {:?} (distance {}), saving {}", point, distance, new_point, new_distance, distance - new_distance - 2);
                    cheats.insert((*point, new_point, distance - new_distance - 2));
                }
            }
        }
    }
    // sort the cheats by distance and print them
    // let mut cheats: Vec<_> = cheats.into_iter().collect();
    // cheats.sort_by_key(|(_, _, distance)| -distance);
    // for cheat in &cheats {
    //     println!("{:?}", cheat);
    // }

    let sol = cheats.iter().filter(|(_, _, distance)| { *distance >= min_saving }).count();
    // println!("{:?}", sol);
    sol.to_string()
}
