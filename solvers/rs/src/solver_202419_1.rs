use std::collections::{HashSet, HashMap};

fn make_designs<'a>(towels: &HashSet<&'a str>, memoized: &mut HashMap<&'a str, bool>, design: &'a str) -> bool {
    // println!("Testing design: {:?}", design);

    if design.is_empty() {
        return true;
    }

    if let Some(&cached) = memoized.get(design) {
        return cached;
    }

    let success = (1..=design.len()).find(|&i| {
        let prefix = &design[..i];
        towels.contains(prefix) && make_designs(towels, memoized, &design[i..])
    }).is_some();

    memoized.insert(design, success);
    success
}

pub fn solve_202419_1(input: &str) -> String {
    let mut lines = input.lines();
    let towels: HashSet<&str> = lines
        .next()
        .unwrap()
        .split(',')
        .map(str::trim)
        .collect();
    // println!("{:?}", towels);

    lines.next(); // blank line

    let mut memoized: HashMap<&str, bool> = HashMap::new();

    let sol = lines
        .filter(|line| make_designs(&towels, &mut memoized, line))
        .count();
    // println!("{:?}", sol);
    sol.to_string()
}
