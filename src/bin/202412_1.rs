use itertools::iproduct;
use std::collections::HashSet;

static _TEST_INPUT: &str = include_str!("inputs/202412_test.txt");
static _INPUT: &str = include_str!("inputs/202412.txt");

type Coord = (i32, i32);

const DIRECTIONS: [Coord; 4] = [(0, 1), (0, -1), (1, 0), (-1, 0)];

fn is_out_of_bounds(coord: Coord, grid: &Vec<Vec<char>>) -> bool {
    coord.0 < 0 || coord.0 >= grid.len() as i32 || coord.1 < 0 || coord.1 >= grid[0].len() as i32
}

fn walk(grid: &Vec<Vec<char>>, visited: &mut HashSet<Coord>, coord: Coord, crop: char) -> (i32, i32) {
    // Return the number of edges and nodes visited
    // println!("Visiting coord {:?}", coord);
    if is_out_of_bounds(coord, grid) {
        // println!("Out of bounds, build a fence");
        return (1, 0);
    }

    // println!("Crop: {}",  grid[coord.0 as usize][coord.1 as usize]);
    if grid[coord.0 as usize][coord.1 as usize] != crop {
        // println!("Walked into a different field. Build a fence");
        return (1, 0);
    }

    if visited.contains(&coord) {
        // println!("Already visited this node");
        return (0, 0);
    }

    visited.insert(coord);

    DIRECTIONS.iter().fold((0, 1), |acc, direction| {  // Start with 0 fences and 1 cell (this one) visited
        let (fences, cells) = acc;
        let new_coord = (coord.0 + direction.0, coord.1 + direction.1);
        let (new_fences, new_cells) = walk(grid, visited, new_coord, crop);
        (fences + new_fences, cells + new_cells)
    })
}

fn main() {
    // Parse the square of chars
    let grid: Vec<Vec<char>> = _INPUT.lines().map(|line| line.chars().collect()).collect();

    let score = iproduct!(0..grid.len() as i32, 0..grid[0].len() as i32).fold((HashSet::new(), 0), |mut acc, coord| {
        let (visited, score) = &mut acc;
        let (new_fences, new_cells) = walk(&grid, visited, coord, grid[coord.0 as usize][coord.1 as usize]);
        *score += new_fences * new_cells;
        acc
    }).1;

    println!("Score: {}", score);
}
