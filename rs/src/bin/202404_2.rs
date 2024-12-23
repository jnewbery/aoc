static TEST: bool = false;

use itertools::iproduct;

static _TEST_INPUT: &str = include_str!("inputs/202404_test.txt");
static _INPUT: &str = include_str!("inputs/202404.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

// Define the diagonal directions, starting from the top-left corner and going clockwise.
static DIAGONALS: &[(i32, i32)] = &[ 
    (-1, -1), // Top-left
    (1, -1),  // Top-right
    (1, 1),   // Bottom-right
    (-1, 1),  // Bottom-left
];

fn get_cell(grid: &Vec<Vec<char>>, x: i32, y: i32) -> Option<char> {
    // Given a grid and coordinates, return the cell value if the coordinates are valid.
    if x < 0 || y < 0 {
        return None;
    }
    grid.get(y as usize).and_then(|row| row.get(x as usize)).copied()
}

fn rotate_pattern(pattern: &Vec<char>, rotations: usize) -> Vec<char> {
    // Given a vector of characters, rotate it by `rotations` to the left.
    let len = pattern.len();
    let mut rotated = pattern.clone();
    rotated.rotate_left(rotations % len);
    rotated
}

fn valid(grid: &Vec<Vec<char>>, x: usize, y: usize) -> i32 {
    // Determine whether the cell at (x,y) contains an 'A' and
    // has 'M' and 'S' in the diagonal cells.
    if get_cell(grid, x as i32, y as i32) != Some('A') {
        return 0;
    }

    let cells: Vec<char> = DIAGONALS.iter()
        .filter_map(|(dx, dy)| get_cell(grid, x as i32 + dx, y as i32 + dy))
        .collect();

    // Define the valid patterns for the diagonal cells. Order is important - the
    // two M's must be adjacent, and the two S's must be adjacent. If not, the
    // M's would be opposite each other, so we wouldn't have a valid pattern.
    let base_pattern = vec!['M', 'M', 'S', 'S'];
    let valid_patterns: Vec<Vec<char>> = (0..base_pattern.len())
        .map(|i| rotate_pattern(&base_pattern, i))
        .collect();

    if valid_patterns.iter().any(|pattern| pattern == &cells) {
        return 1;
    }

    0
}

fn main() {
    let grid: Vec<Vec<char>> = INPUT.lines()
        .map(|line| line.chars().collect())
        .collect();

    let sum: i32 = iproduct!(0..grid.len(), 0..grid[0].len())
        .map(|(y, x)| valid(&grid, x, y))
        .sum();

    println!("{}", sum);
}
