use std::collections::HashMap;

type Point = (i32, i32);

// const GRID_SIZE: Point = if TEST { (11, 7) } else { (101, 103) };

fn positive_modulo(x: i32, n: i32) -> i32 {
    ((x % n) + n) % n
}

pub fn solve_202414_1(input: &str) -> String {
    let grid_size: Point = if input[0..3] == *"p=0" { (11, 7) } else { (101, 103) };  // hardcoded for the input
    let mut quads = HashMap::new();
    for line in input.lines() {
        let numbers = line.split(|c: char| !c.is_numeric() && c != '-').filter_map(|s| s.parse::<i32>().ok()).collect::<Vec<i32>>();
        let pos = (numbers[0], numbers[1]);
        let vel = (numbers[2], numbers[3]);
        // println!("pos: {:?}, vel: {:?}", pos, vel);
        let new_pos = (positive_modulo(pos.0 + 100 * vel.0, grid_size.0), positive_modulo(pos.1 + 100 * vel.1, grid_size.1));
        // println!("new_pos: {:?}", new_pos);
        if new_pos.0 < (grid_size.0 -1) / 2 && new_pos.1 < (grid_size.1 - 1) / 2 {
            *quads.entry(0).or_insert(0) += 1;
        } else if new_pos.0 > (grid_size.0 - 1) / 2 && new_pos.1 < (grid_size.1 - 1) / 2 {
            *quads.entry(1).or_insert(0) += 1;
        } else if new_pos.0 < (grid_size.0 - 1) / 2 && new_pos.1 > (grid_size.1 - 1) / 2 {
            *quads.entry(2).or_insert(0) += 1;
        } else if new_pos.0 > (grid_size.0 - 1) / 2 && new_pos.1 > (grid_size.1 - 1) / 2 {
            *quads.entry(3).or_insert(0) += 1;
        }
    }
    // println!("{:?}", quads);
    
    let sol: i32 = quads.values().product();
    // println!("{}", sol);
    sol.to_string()
}
