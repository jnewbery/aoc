use regex::Regex;

pub fn solve_202403_2(input: &str) -> String {
    const REGEX_PATTERN: &str = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)";
    let re = Regex::new(REGEX_PATTERN).unwrap();

    let mut count = 0;
    let mut enabled = true;

    for cap in re.captures_iter(input) {
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
    // println!("{:?}", count);
    count.to_string()
}
