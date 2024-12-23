static TEST: bool = false;

use std::collections::{HashMap, HashSet};

static _TEST_INPUT: &str = include_str!("../../../inputs/test/202405.txt");
static _INPUT: &str = include_str!("../../../inputs/full/202405.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

fn get_constraints(lines: &mut std::str::Lines) -> HashMap<i32, HashSet<i32>> {
    let mut hashmap = HashMap::new();

    // Iterate over the lines until a blank line is found
    while let Some(line) = lines.next() {
        if line.is_empty() {
            // println!("Encountered a blank line, stopping.");
            break;
        }

        // Split the line by '|'
        let (left, right) = line.split_once('|').expect("Failed to split line");
        let key: i32 = left.trim().parse().expect("Failed to parse key");
        let value: i32 = right.trim().parse().expect("Failed to parse value");

        // Insert the value into the set for the corresponding key
        hashmap.entry(key).or_insert_with(HashSet::new).insert(value);
    }

    hashmap
}

fn test_single_line(line: &str, constraints: &HashMap<i32, HashSet<i32>>) -> i32 {
    // println!("Processing line: {}", line);
    let mut seen = HashSet::new();

    // Split the line by ','
    let values = line.split(',').map(|value_str| value_str.trim().parse().expect("Failed to parse value")).collect::<Vec<i32>>();
    for value in &values {

        // Lookup the value in constraints
        if let Some(constraint_set) = constraints.get(&value) {
            // Check for overlap between constraint_set and seen
            if !seen.is_disjoint(constraint_set) {
                // println!("Found overlap between constraint_set and seen for value: {}", value);
                return 0;
            }
        }

        // Add the value to the seen set
        seen.insert(*value);
    }

    values[(values.len() - 1) / 2]
}

fn main() {
    let mut lines = INPUT.lines();

    // Call the function to process lines until a blank line is found
    let constraints = get_constraints(&mut lines);
    // println!("Constructed HashMap: {:?}", constraints);

    // Apply test_single_line function to the remaining lines
    let sol = lines.map(|line| test_single_line(line, &constraints)).sum::<i32>();
    println!("{}", sol);
}
