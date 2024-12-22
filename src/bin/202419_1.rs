static TEST: bool = false;

use std::collections::{HashSet, HashMap};

static _TEST_INPUT: &str = include_str!("inputs/202419_test.txt");
static _INPUT: &str = include_str!("inputs/202419.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

fn make_designs(towels: &HashSet<&str>, memoized: &mut HashMap<String, bool>, design: &str) -> bool {
    println!("Testing design: {:?}", design);
    if design.len() == 0 { 
        return true;
    } else if memoized.contains_key(design) {
        return memoized[design];
    }
    for i in 1..=design.len() {
        // println!("Looking for towel: {:?}", &design[..i]);
        if towels.contains(&design[..i]) {
            // println!("Found towel: {:?}. Remaining design: {:?}", &design[..i], &design[i..]);
            if make_designs(towels, memoized, &design[i..]) {
                memoized.insert(design.to_string(), true);
                return true;
            }
        }
    }
    memoized.insert(design.to_string(), false);
    false
}

fn main() {
    let mut lines = INPUT.lines();
    let towels = lines.next().unwrap().split(',').map(|towel| towel.trim()).collect::<HashSet<&str>>();
    println!("{:?}", towels);

    lines.next(); // blank line

    let mut memoized: HashMap<String, bool> = HashMap::new();

    let sol = lines.filter(|line| make_designs(&towels, &mut memoized, line)).count();
    println!("{:?}", sol);
}
