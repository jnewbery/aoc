static TEST: bool = false;

static _TEST_INPUT: &str = include_str!("../../../inputs/test/202415.txt");
static _INPUT: &str = include_str!("../../../inputs/full/202415.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

#[derive(Debug, Clone, Copy, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

#[derive(Debug, PartialEq)]
enum Cell {
    Empty,
    Wall,
    WarehouseBox,
}

// Implement addition on Point
impl std::ops::Add for Point {
    type Output = Point;

    fn add(self, other: Point) -> Point {
        Point { x: self.x + other.x, y: self.y + other.y }
    }
}

// Implement multiplication by a scalar on points (i32, i32)
impl std::ops::Mul<i32> for Point {
    type Output = Point;

    fn mul(self, scalar: i32) -> Self {
        Point { x: self.x * scalar, y: self.y * scalar }
    }
}

// Implement scalar multiplication on points (i32, i32)
impl std::ops::Mul<Point> for i32 {
    type Output = Point;

    fn mul(self, point: Point) -> Point {
        Point { x:self * point.x, y:self * point.y }
    }
}

fn _print_grid(grid: &Vec<Vec<Cell>>, reindeer: &Point) {
    for (y, row) in grid.iter().enumerate() {
        for (x, cell) in row.iter().enumerate() {
            if *reindeer == (Point { x: x as i32, y: y as i32 }) {
                print!("@");
                continue;
            }
            match cell {
                Cell::Empty => print!("."),
                Cell::Wall => print!("#"),
                Cell::WarehouseBox => print!("O"),
            }
        }
        println!();
    }
}

fn get_grid(lines: &mut std::str::Lines) -> (Vec<Vec<Cell>>, Point) {
    let mut reindeer = Point { x: 0, y: 0 };
    let mut grid: Vec<Vec<Cell>> = Vec::new();


    // Iterate over the lines until a blank line is found
    while let Some(line) = lines.next() {
        if line.is_empty() {
            // println!("Encountered a blank line, stopping.");
            break;
        }
        grid.push(Vec::new());
        let row_num = grid.len();
        let grid_line = grid.last_mut().unwrap();

        // while let Some(c) = line.chars().next() {
        for c in line.chars() {
            match c {
                '.' => grid_line.push(Cell::Empty),
                '#' => grid_line.push(Cell::Wall),
                'O' => grid_line.push(Cell::WarehouseBox),
                '@' => {
                    reindeer = Point { x: grid_line.len() as i32, y: (row_num - 1) as i32 };
                    grid_line.push(Cell::Empty);
                }
                _ => panic!("Invalid character in input"),
            }
        }
    }

    (grid, reindeer)
}

fn move_reindeer(lines: std::str::Lines, grid: &mut Vec<Vec<Cell>>, reindeer: &mut Point) {
    for line in lines {
        for c in line.chars() {
            let direction = match c {
                '^' => Point { x: 0, y: -1 },
                '>' => Point { x: 1, y: 0 },
                'v' => Point { x: 0, y: 1 },
                '<' => Point { x: -1, y: 0 },
                _ => panic!("Invalid character in input"),
            };

            for i in 1.. {
                let new_pos = *reindeer + direction * i;
                match grid[new_pos.y as usize][new_pos.x as usize] {
                    Cell::Wall => {
                        // println!("Wall at {:?}", new_pos);
                        break;
                    }
                    Cell::WarehouseBox => {
                        // println!("Box at {:?}", new_pos);
                        continue;
                    }
                    Cell::Empty => {
                        // println!("Empty at {:?}", new_pos);
                        grid[new_pos.y as usize][new_pos.x as usize] = Cell::WarehouseBox;
                        grid[(reindeer.y + direction.y) as usize][(reindeer.x + direction.x) as usize] = Cell::Empty;
                        grid[reindeer.y as usize][reindeer.x as usize] = Cell::Empty;
                        *reindeer = *reindeer + direction;
                        break;
                    }
                }
            }
            // println!("{:?}", c);
            // _print_grid(&grid, &reindeer);
            // println!();
        }
    }
}

fn score_grid(grid: &Vec<Vec<Cell>>){
    let mut score = 0;
    for (y, row) in grid.iter().enumerate() {
        for (x, cell) in row.iter().enumerate() {
            if *cell == Cell::WarehouseBox {
                score += 100 * y + x
            }
        }
    }
    println!("Score: {}", score);
}

fn main() {
    let mut lines = INPUT.lines();
    let (mut grid, mut reindeer) = get_grid(&mut lines);

    // _print_grid(&grid, &reindeer);
    // println!();

    move_reindeer(lines, &mut grid, &mut reindeer);

    score_grid(&grid);
}
