static _TEST: bool = false;
static _TEST_INPUT: &str = include_str!("inputs/202414_test.txt");
static _INPUT: &str = include_str!("inputs/202414.txt");

const INPUT: &str = if _TEST { _TEST_INPUT } else { _INPUT };

type Point = (i32, i32);
type Robot = (Point, Point);  // (pos, vel)

static _TEST_GRID_SIZE: Point = (11, 7);
static _GRID_SIZE: Point = (101, 103);

const GRID_SIZE: Point = if _TEST { _TEST_GRID_SIZE } else { _GRID_SIZE };

fn positive_modulo(x: i32, n: i32) -> i32 {
    ((x % n) + n) % n
}

fn print_grid(grid: &Vec<Vec<bool>>) {
    for row in grid.iter() {
        for cell in row.iter() {
            print!("{}", if *cell { '#' } else { '.' });
        }
        println!();
    }
}

fn column_has_more_than_29(grid: &Vec<Vec<bool>>, col: i32) -> bool {
    grid.iter().filter(|row| row[col as usize]).count() >= 20
}

fn row_has_more_than_29(row: &Vec<bool>) -> bool {
    row.iter().filter(|cell| **cell).count() >= 20
}

fn main() {
    let mut robots: Vec<Robot> = Vec::new();
    for line in INPUT.lines() {
        let numbers = line.split(|c: char| !c.is_numeric() && c != '-').filter_map(|s| s.parse::<i32>().ok()).collect::<Vec<i32>>();
        let pos = (numbers[0], numbers[1]);
        let vel = (numbers[2], numbers[3]);
        robots.push((pos, vel));
    }

    for i in 1..(GRID_SIZE.0 * GRID_SIZE.1) {
        let mut grid: Vec<Vec<bool>> = vec![vec![false; GRID_SIZE.0 as usize]; GRID_SIZE.1 as usize];
        for robot in robots.iter_mut() {
            let new_pos = (positive_modulo(robot.0.0 + robot.1.0, GRID_SIZE.0), positive_modulo(robot.0.1 + robot.1.1, GRID_SIZE.1));
            robot.0 = new_pos;
            grid[new_pos.1 as usize][new_pos.0 as usize] = true;
        }
        // println!("{:?}", robots);

        // If the grid has more than 50 cells in the middle column, we have a solution
        if grid.iter().filter(|row| row_has_more_than_29(row) && column_has_more_than_29(&grid, GRID_SIZE.0 / 2)).count() > 0 {
            print_grid(&grid);
            println!("Solution: {}", i);
            break;
        }
    }
}
