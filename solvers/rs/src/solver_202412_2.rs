static TEST: bool = false;

use itertools::iproduct;
use std::collections::HashSet;

static _TEST_INPUT: &str = include_str!("../../../inputs/test/202412.txt");
static _INPUT: &str = include_str!("../../../inputs/full/202412.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

type Coord = (i32, i32);
// A fence is a tuple of:
// - the coordinate of the cell _inside_ the field
// - the direction the fence faces out from the field
type Fence = (Coord, Coord);

const DIRECTIONS: [Coord; 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];

fn turn_left(direction: Coord) -> Coord {
    DIRECTIONS[(DIRECTIONS.iter().position(|&d| d == direction).unwrap() + 1) % 4]
}

fn turn_right(direction: Coord) -> Coord {
    DIRECTIONS[(DIRECTIONS.iter().position(|&d| d == direction).unwrap() + 3) % 4]
}

fn is_out_of_bounds(coord: Coord, grid: &Vec<Vec<char>>) -> bool {
    coord.0 < 0 || coord.0 >= grid.len() as i32 || coord.1 < 0 || coord.1 >= grid[0].len() as i32
}

fn walk(grid: &Vec<Vec<char>>, visited: &mut HashSet<Coord>, coord: Coord, crop: char) -> (HashSet<Fence>, i32) {
    // Return the set of fences and number of cells visited

    if visited.contains(&coord) {
        // println!("Already visited this node");
        return (HashSet::new(), 0);
    }

    visited.insert(coord);

    DIRECTIONS.iter().fold((HashSet::new(), 1), |acc, direction| {  // Start with no fences and 1 cell (this one) visited
        let (mut fences, cells) = acc;
        let new_coord = (coord.0 + direction.0, coord.1 + direction.1);
        if is_out_of_bounds(new_coord, grid) {
            // println!("Out of bounds, build a fence");
            fences.insert((coord, *direction));
            return (fences, cells);
        } else if grid[new_coord.0 as usize][new_coord.1 as usize] != crop {
            // println!("Walked into a different field. Build a fence");
            fences.insert((coord, *direction));
            return (fences, cells);
        }
        let (new_fences, new_cells) = walk(grid, visited, new_coord, crop);
        (fences.union(&new_fences).copied().collect(), cells + new_cells)
    })
}

fn count_sides(fences: &mut HashSet<Fence>) -> i32 {
    // Given a set of fences, calculate the number of connected sides.
    // A side is a sequence of fences that are connected and face the same direction
    let mut sides = 0;
    while let Some(fence) = fences.iter().next().cloned() {
        fences.remove(&fence);
        sides += 1;
        // Remove all fences that are to the left and facing in the same direction of the one we just removed
        let left = turn_left(fence.1);
        for i in 1.. {
            let next = (fence.0.0 + i * left.0, fence.0.1 + i * left.1);
            if !fences.contains(&(next, fence.1)) {
                break;
            }
            fences.remove(&(next, fence.1));
        }
        // Remove all fences that are to the right and facing in the same direction of the one we just removed
        let right = turn_right(fence.1);
        for i in 1.. {
            let next = (fence.0.0 + i * right.0, fence.0.1 + i * right.1);
            if !fences.contains(&(next, fence.1)) {
                break;
            }
            fences.remove(&(next, fence.1));
        }
    }
    // println!("Sides: {}", sides);
    sides
}

pub fn solve_202412_2() -> String {
    // Parse the square of chars
    let grid: Vec<Vec<char>> = INPUT.lines().map(|line| line.chars().collect()).collect();
    let mut visited = HashSet::new();

    let mut sol = 0;
    for (i, j) in iproduct!(0..grid.len() as i32, 0..grid[0].len() as i32) {
        if visited.contains(&(i, j)) {
            continue;
        }
        // println!("Checking cell ({}, {}), crop: {}", i, j, grid[i as usize][j as usize]);

        // Explore this field
        let (mut fences, cells) = walk(&grid, &mut visited, (i, j), grid[i as usize][j as usize]);
        // println!("Visited {} cells", visited.len());
        // println!("Cells: {}", cells);

        // Count the number of sides, given the set of fences
        let sides = count_sides(&mut fences);
        sol += cells * sides;
    }

    // println!("{}", sol);
    sol.to_string()
}
