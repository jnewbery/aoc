use itertools::iproduct;

static _TEST_INPUT: &str = include_str!("202410_test_input.txt");
static _INPUT: &str = include_str!("202410_input.txt");

type Coord = (i32, i32);

#[derive(Debug)]
struct Cell {
    height: i32,
    // The summits that can be reached by this cell. None if not calculated yet.
    rating: Option<i32>,
}

static DIRECTIONS: &[Coord] = &[(0, 1), (1, 0), (0, -1), (-1, 0)];

fn climb(cells: &mut Vec<Vec<Cell>>, x: i32, y: i32) -> i32 {
    if let Some(rating) = cells[y as usize][x as usize].rating {
        return rating;
    }
    else if cells[y as usize][x as usize].height == 9 {
        return 1;
    }
    let rating = DIRECTIONS.iter().map(|(dx, dy)| {
        let new_x = x + dx;
        let new_y = y + dy;
        if new_x < 0 || new_x >= cells[0].len() as i32 || new_y < 0 || new_y >= cells.len() as i32 {
            return 0;
        } else if cells[new_y as usize][new_x as usize].height != cells[y as usize][x as usize].height + 1 {
            return 0;
        }
        climb(cells, new_x, new_y)
    }).sum();

    cells[y as usize][x as usize].rating = Some(rating);

    rating
}

fn main() {
    let mut cells: Vec<Vec<Cell>> = _INPUT.lines().map(|line| {
        line.chars().map(|c| Cell { height: c.to_digit(10).unwrap() as i32, rating: None }).collect()
    }).collect();

    // println!("{:?}", cells);

    let score: i32 = iproduct!(0..cells[0].len() as i32, 0..cells.len() as i32)
        .filter_map(|(x, y)| {
            if cells[y as usize][x as usize].height == 0 {
                // Perform the climb operation outside the direct reference to `cells[y][x]`.
                cells[y as usize][x as usize].rating = Some(climb(&mut cells, x, y));
                Some(cells[y as usize][x as usize].rating.unwrap() as i32)
            } else {
                Some(0)
            }
        })
        .sum();

    println!("{:?}", score);
}
