use std::io;
use std::collections::HashMap;

static _TEST_INPUT: &str = include_str!("202401_test_input.txt");
static _INPUT: &str = include_str!("202401_input.txt");

fn main() -> io::Result<()> {
    // Parse the input into two hashmaps
    let (counts1, counts2) = _INPUT.lines().fold((HashMap::new(), HashMap::new()), |(mut acc1, mut acc2), line| {
        let parts: Vec<&str> = line.split_whitespace().collect();
        let a = parts[0].parse::<i32>().expect("Failed to parse first column");
        let b = parts[1].parse::<i32>().expect("Failed to parse second column");
        *acc1.entry(a).or_insert(0) += 1;
        *acc2.entry(b).or_insert(0) += 1;
        (acc1, acc2)
    });

    // Calculate the product of the counts of the two columns
    let result: i32 = counts1.iter()
        .filter_map(|(key, value1)| counts2.get(key).map(|value2| key * value1 * value2))
        .sum();

    println!("Result: {}", result);

    Ok(())
}
