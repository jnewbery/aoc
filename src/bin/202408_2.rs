use std::collections::{HashMap, HashSet};

static _TEST_INPUT: &str = include_str!("202408_test_input.txt");
static _INPUT: &str = include_str!("202408_input.txt");

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

fn get_antinodes_for_pair(ant1: (i32, i32), ant2: (i32, i32), bounds: (i32, i32)) -> Vec<(i32, i32)> {
    let (dx, dy) = (ant2.0 - ant1.0, ant2.1 - ant1.1);
    let mut antinodes = Vec::new();
    for i in 1.. {
        let (x, y) = (ant2.0 - dx * i, ant2.1 - dy * i);
        if (0..bounds.0).contains(&x) && (0..bounds.1).contains(&y) {
            antinodes.push((x, y));
        } else {
            break;
        }
    }
    antinodes
}

fn get_antinodes_for_freq(antennae: &Vec<(i32, i32)>, bounds: (i32, i32)) -> HashSet<(i32, i32)> {
    antennae
        .iter()
        .flat_map(|&ant1| antennae.iter().filter_map(move |&ant2| {
            if ant1 != ant2 {
                Some(get_antinodes_for_pair(ant1, ant2, bounds))
            } else {
                Some(Vec::new())
            }
        }))
        .flatten()
        .collect()
}

fn main() {
    let lines: Vec<&str> = _INPUT.lines().collect();
    let bounds = (lines[0].len() as i32, lines.len() as i32);
    let antennae = parse_map(lines);
    // println!("{:?}", antennae);
    // println!("{:?}", bounds);

    let sol = antennae
        .values()
        .flat_map(|v| get_antinodes_for_freq(v, bounds))
        .collect::<HashSet<(i32, i32)>>()
        .len();
    println!("{:?}", sol);
}
