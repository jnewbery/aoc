static TEST: bool = false;

use itertools::iproduct;

static _TEST_INPUT: &str = include_str!("../../../inputs/test/202404.txt");
static _INPUT: &str = include_str!("../../../inputs/full/202404.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

fn get_directions() -> Vec<(i32, i32)> {
    iproduct!(-1..=1, -1..=1)
        .filter(|&(x, y)| !(x == 0 && y == 0))
        .map(|(x, y)| (x, y))
        .collect()
}

fn dfs(grid: &Vec<Vec<char>>, x: usize, y: usize, target: &str, dir: &(i32, i32)) -> i32 {
    let value = match grid.get(y).and_then(|row| row.get(x)) {
        Some(&c) => c,
        None => {
            // Out of bounds!
            return 0;
        }
    };

    if value != target.chars().next().unwrap() {
        // cell content does not match target
        return 0;
    }

    if target.len() == 1 {
        // target fully matched
        return 1
    }

    dfs(grid, (x as i32 + dir.0) as usize, (y as i32 + dir.1) as usize, &target[1..], dir)
}

fn main() {
    let target = "XMAS";
    let grid: Vec<Vec<char>> = INPUT.lines()
        .map(|line| line.chars().collect())
        .collect();

    let sum: i32 = iproduct!(0..grid.len(), 0..grid[0].len(), get_directions())
        .map(|(y, x, dir)| dfs(&grid, x, y, &target, &dir))
        .sum();

    println!("{}", sum);
}
