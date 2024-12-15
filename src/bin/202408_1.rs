static TEST: bool = true;

use std::collections::{HashMap, HashSet};

static _TEST_INPUT: &str = include_str!("inputs/202408_test.txt");
static _INPUT: &str = include_str!("inputs/202408.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

fn parse_map(input: Vec<&str>) -> HashMap<char, Vec<(i32, i32)>> {
    let mut map = HashMap::new();
    for (y, line) in input.iter().enumerate() {
        for (x, c) in line.chars().enumerate() {
            if c != '.' {
                map.entry(c).or_insert(Vec::new()).push((x as i32, y as i32));
            }
        }
    }
    map
}

fn get_antinode(ant1: (i32, i32), ant2: (i32, i32), bounds: (i32, i32)) -> Result<(i32, i32), ()> {
    let (x, y) = (2 * ant1.0 - ant2.0, 2 * ant1.1 - ant2.1);
    if (0..bounds.0).contains(&x) && (0..bounds.1).contains(&y) {
        Ok((x, y))
    } else {
        Err(())
    }
}

fn get_antinodes(antennae: &Vec<(i32, i32)>, bounds: (i32, i32)) -> HashSet<(i32, i32)> {
    antennae
        .iter()
        .flat_map(|&ant1| antennae.iter().filter_map(move |&ant2| {
            if ant1 != ant2 {
                get_antinode(ant1, ant2, bounds).ok()
            } else {
                None
            }
        }))
        .collect()
}

fn main() {
    let lines: Vec<&str> = INPUT.lines().collect();
    let bounds = (lines[0].len() as i32, lines.len() as i32);
    let antennae = parse_map(lines);
    // println!("{:?}", antennae);
    // println!("{:?}", bounds);

    let sol = antennae
        .values()
        .flat_map(|v| get_antinodes(v, bounds))
        .collect::<HashSet<(i32, i32)>>()
        .len();
    println!("{:?}", sol);
}
