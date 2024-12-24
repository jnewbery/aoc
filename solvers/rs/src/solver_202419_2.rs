static TEST: bool = false;

use std::collections::{HashSet, HashMap};

static _TEST_INPUT: &str = include_str!("../../../inputs/test/202419.txt");
static _INPUT: &str = include_str!("../../../inputs/full/202419.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

fn make_designs<'a>(towels: &HashSet<&'a str>, memoized: &mut HashMap<&'a str, u64>, design: &'a str) -> u64 {
    // println!("Testing design: {:?}", design);
    if design.is_empty() {
        return 1;
    }

    if let Some(&cached) = memoized.get(design) {
        return cached;
    }

    let ways = (1..=design.len())
        .filter(|&i| towels.contains(&design[..i]))
        .map(|i| make_designs(towels, memoized, &design[i..]))
        .sum();

    memoized.insert(design, ways);
    ways
}

pub fn solve_202419_2() -> String {
    let mut lines = INPUT.lines();
    let towels: HashSet<&str> = lines
        .next()
        .unwrap()
        .split(',')
        .map(str::trim)
        .collect();
    // println!("{:?}", towels);

    lines.next(); // blank line

    let mut memoized: HashMap<&str, u64> = HashMap::new();

    let sol = lines
        .map(|line| make_designs(&towels, &mut memoized, line))
        .sum::<u64>();
    // println!("{:?}", sol);
    sol.to_string()
}
