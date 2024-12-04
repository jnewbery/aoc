static _TEST_INPUT: &str = include_str!("202403b_test_input.txt");
static _INPUT: &str = include_str!("202403_input.txt");

use regex::Regex;

fn main() {
    let re = Regex::new(r"mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)").unwrap();

    let sol = re.captures_iter(_INPUT).fold((0, true), |(count, enabled), cap| {
        match cap.get(0).map(|m| m.as_str()) {
            Some(m) if m.starts_with("mul(") && enabled => {
                let n = cap.get(1).unwrap().as_str().parse::<i32>().unwrap();
                let m = cap.get(2).unwrap().as_str().parse::<i32>().unwrap();
                // println!("Matched mul: ({}, {})", n, m);
                (count + n * m, enabled)
            }
            Some("do()") => {
                // println!("Matched: do()");
                (count, true)

            }
            Some("don't()") => {
                // println!("Matched: don't()");
                (count, false)
            }
            _ => (count, enabled)
        }
    }).0;
    println!("{:?}", sol);
}
