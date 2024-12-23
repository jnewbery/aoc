static TEST: bool = false;

static _TEST_INPUT: &str = include_str!("../../../../inputs/test/202403.txt");
static _INPUT: &str = include_str!("../../../../inputs/full/202403.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

use regex::Regex;

fn parse_mul_pairs(input: &str) -> Vec<(i32, i32)> {
    let re = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();
    let mut pairs = Vec::new();

    for cap in re.captures_iter(input) {
        if let (Some(n_match), Some(m_match)) = (cap.get(1), cap.get(2)) {
            let n: i32 = n_match.as_str().parse().unwrap();
            let m: i32 = m_match.as_str().parse().unwrap();
            pairs.push((n, m));
        }
    }

    pairs
}

fn main() {
    let pairs = parse_mul_pairs(INPUT);
    // println!("{:?}", pairs);
    let sol: i32 = pairs.iter().map(|(n, m)| n * m).sum();
    println!("{:?}", sol);
}
