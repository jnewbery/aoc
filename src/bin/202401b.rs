use std::io;
use std::collections::HashMap;

static _TEST_INPUT: &str = include_str!("202401_test_input.txt");
static _INPUT: &str = include_str!("202401_input.txt");

fn main() -> io::Result<()> {
    let mut counts1 = HashMap::new();
    let mut counts2 = HashMap::new();

    // Read the file line by line
    for line in _INPUT.lines() {
        let parts: Vec<&str> = line.split_whitespace().collect();
        if parts.len() == 2 {
            if let (Ok(a), Ok(b)) = (parts[0].parse::<i32>(), parts[1].parse::<i32>()) {
                *counts1.entry(a).or_insert(0) += 1;
                *counts2.entry(b).or_insert(0) += 1;
            } else {
                eprintln!("Warning: Could not parse line: {}", line);
            }
        } else {
            eprintln!("Warning: Incorrect format in line: {}", line);
        }
    }

    // Iterate over counts1 and calculate result
    let mut result = 0;
    for (key, value1) in &counts1 {
        if let Some(value2) = counts2.get(key) {
            result += key * value1 * value2;
        }
    }

    println!("Result: {}", result);

    Ok(())
}
