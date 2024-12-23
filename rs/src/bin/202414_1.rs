static TEST: bool = false;

use std::collections::HashMap;

static _TEST_INPUT: &str = include_str!("inputs/202414_test.txt");
static _INPUT: &str = include_str!("inputs/202414.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

type Point = (i32, i32);

const GRID_SIZE: Point = if TEST { (11, 7) } else { (101, 103) };

fn positive_modulo(x: i32, n: i32) -> i32 {
    ((x % n) + n) % n
}

fn main() {
    let mut quads = HashMap::new();
    for line in INPUT.lines() {
        let numbers = line.split(|c: char| !c.is_numeric() && c != '-').filter_map(|s| s.parse::<i32>().ok()).collect::<Vec<i32>>();
        let pos = (numbers[0], numbers[1]);
        let vel = (numbers[2], numbers[3]);
        // println!("pos: {:?}, vel: {:?}", pos, vel);
        let new_pos = (positive_modulo(pos.0 + 100 * vel.0, GRID_SIZE.0), positive_modulo(pos.1 + 100 * vel.1, GRID_SIZE.1));
        // println!("new_pos: {:?}", new_pos);
        if new_pos.0 < (GRID_SIZE.0 -1) / 2 && new_pos.1 < (GRID_SIZE.1 - 1) / 2 {
            *quads.entry(0).or_insert(0) += 1;
        } else if new_pos.0 > (GRID_SIZE.0 - 1) / 2 && new_pos.1 < (GRID_SIZE.1 - 1) / 2 {
            *quads.entry(1).or_insert(0) += 1;
        } else if new_pos.0 < (GRID_SIZE.0 - 1) / 2 && new_pos.1 > (GRID_SIZE.1 - 1) / 2 {
            *quads.entry(2).or_insert(0) += 1;
        } else if new_pos.0 > (GRID_SIZE.0 - 1) / 2 && new_pos.1 > (GRID_SIZE.1 - 1) / 2 {
            *quads.entry(3).or_insert(0) += 1;
        }
    }
    // println!("{:?}", quads);
    
    let sol: i32 = quads.values().product();
    println!("{}", sol);

}
