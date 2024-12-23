static TEST: bool = false;

use std::collections::HashSet;

static _TEST_INPUT: &str = include_str!("../../../inputs/test/202406.txt");
static _INPUT: &str = include_str!("../../../inputs/full/202406.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

type Location = (i32, i32);
type Direction = (i32, i32);

static DIRECTIONS: &[Direction] = &[
    (-1, 0),  // Up
    (0, 1),   // Right
    (1, 0),   // Down
    (0, -1),  // Left
];

fn turn_right(dir: &Direction) -> Direction {
    // Given a direction, return the direction after turning right.
    return DIRECTIONS[(DIRECTIONS.iter().position(|&d| d == *dir).unwrap() + 1) % DIRECTIONS.len()];
}

fn move_in_direction(loc: &Location, dir: &Direction) -> Location {
    // Given a location and a direction, return the new location after moving in that direction.
    return (loc.0 + dir.0, loc.1 + dir.1);
}

fn find_start_location(grid: &[&str]) -> Location {
    grid.iter()
        .enumerate()
        .find_map(|(row_idx, row)| {
            row.chars()
                .position(|c| c == '^')
                .map(|col_idx| (row_idx as i32, col_idx as i32))
        })
        .expect("No start location found")
}

fn makes_loop(lines: &Vec<&str>, loc: Location, dir: Direction, obstacle: Location, visited: &HashSet<(Location, Direction)>) -> bool {
    let mut loc = loc;
    let mut dir = dir;
    let mut new_visited: HashSet<(Location, Direction)> = HashSet::new();
    loop {
        if visited.contains(&(loc, dir)) || new_visited.contains(&(loc, dir)) {
            return true;
        }
        new_visited.insert((loc, dir));

        let next_location = move_in_direction(&loc, &dir);
        let next_char = lines.get(next_location.0 as usize).and_then(|row: &&str| row.chars().nth(next_location.1 as usize));
        match next_char {
            // If the next location is out of bounds, stop
            None => return false,
            // If the next location is a wall, turn right
            Some('#') => dir = turn_right(&dir),
            // If the next location contains the new obstacle, turn right
            Some('.') | Some('^') if next_location == obstacle => dir = turn_right(&dir),
            // If the next location is empty, move forward
            Some('.') | Some('^') => loc = next_location,
            // Cases above are exhaustive
            _ => panic!("Unexpected character at loc: {:?}", next_location),
        }
    }
}

fn main() {
    let lines = INPUT.lines().collect::<Vec<&str>>();
    let mut loc = find_start_location(&lines);
    let mut dir = DIRECTIONS[0];
    // println!("Start location: {:?}, direction: {:?}", loc, dir);

    let mut visited: HashSet<(Location, Direction)> = HashSet::new();
    let mut solution = 0;
    loop {
        // println!("Location: {:?}, Direction: {:?}, Visited: {:?}", loc, dir, visited.len());
        visited.insert((loc, dir));
        let next_location = move_in_direction(&loc, &dir);
        let next_char = lines.get(next_location.0 as usize).and_then(|row: &&str| row.chars().nth(next_location.1 as usize));
        match next_char {
            // If the next location is out of bounds, stop
            None => break,
            // If the next location is a wall, turn right
            Some('#') => dir = turn_right(&dir),
            // If the next location is empty, move forward
            Some('.') | Some('^') => {
                // If the next location hasn't been visited, and adding an obstacle at the next
                // location makes a loop, increment the solution
                if !(visited.iter().map(|(loc, _)| loc).collect::<Vec<_>>().contains(&&next_location)) && makes_loop(&lines, loc, turn_right(&dir), next_location, &visited) {
                    solution+=1;
                }
                loc = next_location
            },
            // Cases above are exhaustive
            _ => panic!("Unexpected character at loc: {:?}", next_location),
        }
    }
    // println!("Visited locations: {:?}", visited);
    // println!("Visited {:?} locations", visited.iter().map(|(loc, _)| loc).collect::<HashSet<_>>().len());
    println!("{:?}", solution);
}
