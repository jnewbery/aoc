static TEST: bool = true;

use std::collections::HashSet;

static _TEST_INPUT: &str = include_str!("inputs/202407_test.txt");
static _INPUT: &str = include_str!("inputs/202407.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

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

            let con: i64 = format!("{}{}", result.to_string(), operand.to_string()).parse().unwrap();
            if con <= target {
                new_results.insert(con);
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
    let sol = INPUT.lines().map(|line| test_line(line)).sum::<i64>();
    println!("{:?}", sol);
}
