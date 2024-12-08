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

fn get_antinode(ant1: (i32, i32), ant2: (i32, i32), bounds: (i32, i32)) -> Result<(i32, i32), ()> {
    let x = 2 * ant1.0 - ant2.0;
    if x < 0 || x >= bounds.0 {
        return Err(());
    }
    let y = 2 * ant1.1 - ant2.1;
    if y < 0 || y >= bounds.1 {
        return Err(());
    }
    return Ok((x, y));
}

fn get_antinodes(antennae: &Vec<(i32, i32)>, bounds: (i32, i32)) -> HashSet<(i32, i32)> {
    let mut antinodes = HashSet::new();
    for pair in antennae.iter().flat_map(|&x| antennae.iter().filter_map(move |&y| if x != y { Some((x, y)) } else { None })) {
        match get_antinode(pair.0, pair.1, bounds) {
            Ok(antinode) => {
                antinodes.insert(antinode);
            },
            Err(_) => {},
        }
    }
    antinodes
}

fn main() {
    let lines: Vec<&str> = _INPUT.lines().collect();
    let bounds = (lines[0].len() as i32, lines.len() as i32);
    let antennae = parse_map(lines);
    // println!("{:?}", antennae);
    // println!("{:?}", bounds);

    let antinodes = antennae.iter().map(|(_, v)| get_antinodes(v, bounds)).fold(HashSet::new(), |acc, x| acc.union(&x).cloned().collect());
    // println!("{:?}", antinodes);
    println!("{:?}", antinodes.len());
}
