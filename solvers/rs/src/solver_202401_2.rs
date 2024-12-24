static TEST: bool = false;

use std::collections::HashMap;

static _TEST_INPUT: &str = include_str!("../../../inputs/test/202401.txt");
static _INPUT: &str = include_str!("../../../inputs/full/202401.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

pub fn solve_202401_2() -> String {
    // Parse lines into hashmaps of counts
    let (counts1, counts2) = INPUT.lines().fold((HashMap::new(), HashMap::new()), |(mut acc1, mut acc2), line| {
        let parts: Vec<i32> = line
            .split_whitespace()
            .map(|s| s.parse::<i32>().expect("Failed to parse column"))
            .collect();
        *acc1.entry(parts[0]).or_insert(0) += 1;
        *acc2.entry(parts[1]).or_insert(0) += 1;
        (acc1, acc2)
    });

    // Calculate the product of the counts for each entry
    let result: i32 = counts1.iter()
        .filter_map(|(key, value1)| counts2.get(key).map(|value2| key * value1 * value2))
        .sum();

    // println!("{}", result);
    result.to_string()
}
