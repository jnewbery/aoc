static TEST: bool = false;

use regex::Regex;

static _TEST_INPUT: &str = include_str!("inputs/202403_test.txt");
static _INPUT: &str = include_str!("inputs/202403.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

fn main() {
    const REGEX_PATTERN: &str = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)";
    let re = Regex::new(REGEX_PATTERN).unwrap();

    let mut count = 0;
    let mut enabled = true;

    for cap in re.captures_iter(INPUT) {
        match cap.get(0).map(|m| m.as_str()) {
            Some(m) if m.starts_with("mul(") && enabled => {
                if let (Some(n_match), Some(m_match)) = (cap.get(1), cap.get(2)) {
                    let n = n_match.as_str().parse::<i32>().unwrap();
                    let m = m_match.as_str().parse::<i32>().unwrap();
                    count += n * m;
                }
            }
            Some("do()") => {
                enabled = true;
            }
            Some("don't()") => {
                enabled = false;
            }
            _ => {}
        }
    }
    println!("{:?}", count);
}
