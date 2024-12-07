use std::collections::HashSet;

static _TEST_INPUT: &str = include_str!("202407_test_input.txt");
static _INPUT: &str = include_str!("202407_input.txt");

fn test_line(line: &str) -> i64 {
    let mut operands = line.split(|c: char| !c.is_numeric() && c != '-')
        .filter_map(|s| s.parse::<i64>().ok());
    let target = operands.next().unwrap();

    let mut results: HashSet<i64> = HashSet::new();
    results.insert(operands.next().unwrap());

    for operand in operands {
        let mut new_results = HashSet::new();
        for result in results.iter() {
            if result + operand <= target {
                new_results.insert(result + operand);
            }
            if result * operand <= target {
                new_results.insert(result * operand);
            }
        }
        results = new_results;
    }

    if results.contains(&target) {
        return target;
    }

    0
}

fn main() {
    let sol = _INPUT.lines().map(|line| test_line(line)).sum::<i64>();
    println!("{:?}", sol);
}
