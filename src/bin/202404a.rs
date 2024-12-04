use itertools::iproduct;

static _TEST_INPUT: &str = include_str!("202404_test_input.txt");
static _INPUT: &str = include_str!("202404_input.txt");

fn dfs(grid: &Vec<Vec<char>>, x: usize, y: usize) {
    let value = grid.get(y).unwrap().get(x).unwrap();
    println!("Character at ({}, {}): {}", x, y, value);
}

fn main() {
    let grid: Vec<Vec<char>> = _INPUT.lines()
        .map(|line| line.chars().collect())
        .collect();

    for (y, x) in iproduct!(0..grid.len(), 0..grid[0].len()) {
        dfs(&grid, x, y);
    }
}
