use std::collections::HashSet;

static _TEST_INPUT: &str = include_str!("202406_test_input.txt");
static _INPUT: &str = include_str!("202406_input.txt");

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

fn move_in_direction(location: &Location, dir: &Direction) -> Location {
    // Given a location and a direction, return the new location after moving in that direction.
    return (location.0 + dir.0, location.1 + dir.1);
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

fn main() {
    let lines = _INPUT.lines().collect::<Vec<&str>>();
    let mut location = find_start_location(&lines);
    let mut dir = DIRECTIONS[0];
    // println!("Start location: {:?}, direction: {:?}", location, dir);

    let mut visited: HashSet<Location> = HashSet::new();
    loop {
        visited.insert(location);
        let next_location = move_in_direction(&location, &dir);
        let next_char = lines.get(next_location.0 as usize).and_then(|row: &&str| row.chars().nth(next_location.1 as usize));
        match next_char {
            // If the next location is out of bounds, stop
            None => break,
            Some('#') => {
                // If the next location is a wall, turn right
                dir = turn_right(&dir);
            }
            Some('.') | Some('^') => {
                // If the next location is empty, move forward
                location = next_location;
            }
            _ => panic!("Unexpected character at location: {:?}", next_location),
        }
    }
    println!("Visited locations: {:?}", visited.len());
}
