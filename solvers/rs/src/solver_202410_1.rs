static TEST: bool = false;

use std::collections::HashSet;
use itertools::iproduct;

static _TEST_INPUT: &str = include_str!("../../../inputs/test/202410.txt");
static _INPUT: &str = include_str!("../../../inputs/full/202410.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

type Coord = (i32, i32);

#[derive(Debug)]
struct Cell {
    height: i32,
    // The summits that can be reached by this cell. None if not calculated yet.
    summits: Option<HashSet<Coord>>,
}

static DIRECTIONS: &[Coord] = &[(0, 1), (1, 0), (0, -1), (-1, 0)];

fn climb(cells: &mut Vec<Vec<Cell>>, x: i32, y: i32) -> HashSet<Coord> {
    if let Some(summits) = cells[y as usize][x as usize].summits.clone() {
        return summits;
    }
    else if cells[y as usize][x as usize].height == 9 {
        return HashSet::from([(x as i32, y as i32)]);
    }
    let summits = DIRECTIONS.iter().map(|(dx, dy)| {
        let new_x = x + dx;
        let new_y = y + dy;
        if new_x < 0 || new_x >= cells[0].len() as i32 || new_y < 0 || new_y >= cells.len() as i32 {
            return HashSet::new();
        } else if cells[new_y as usize][new_x as usize].height != cells[y as usize][x as usize].height + 1 {
            return HashSet::new();
        }
        climb(cells, new_x, new_y)
    }).fold(HashSet::new(), |mut acc, s| {
        acc.extend(&s);
        acc
    });

    cells[y as usize][x as usize].summits = Some(summits.clone());

    summits
}

pub fn solve_202410_1() -> String {
    let mut cells: Vec<Vec<Cell>> = INPUT.lines().map(|line| {
        line.chars().map(|c| Cell { height: c.to_digit(10).unwrap() as i32, summits: None }).collect()
    }).collect();

    // println!("{:?}", cells);

    let score: usize = iproduct!(0..cells[0].len() as i32, 0..cells.len() as i32)
        .filter_map(|(x, y)| {
            if cells[y as usize][x as usize].height == 0 {
                // Perform the climb operation outside the direct reference to `cells[y][x]`.
                cells[y as usize][x as usize].summits = Some(climb(&mut cells, x, y));
                cells[y as usize][x as usize].summits.as_ref().map(|summits| summits.len())
            } else {
                None
            }
        })
        .sum();

    // println!("{:?}", score);
    score.to_string()
}
