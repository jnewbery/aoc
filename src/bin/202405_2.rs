use std::collections::HashSet;

static _TEST_INPUT: &str = include_str!("202405_test_input.txt");
static _INPUT: &str = include_str!("202405_input.txt");

fn get_pairs(lines: &mut std::str::Lines) -> Vec<(i32, i32)> {
    let mut pairs = Vec::new();

    // Iterate over the lines until a blank line is found
    while let Some(line) = lines.next() {
        if line.is_empty() {
            // println!("Encountered a blank line, stopping.");
            break;
        }

        // Split the line by '|'
        let (left, right) = line.split_once('|').expect("Failed to split line");
        let left: i32 = left.trim().parse().expect("Failed to parse key");
        let right: i32 = right.trim().parse().expect("Failed to parse value");

        pairs.push((left, right));
    }

    pairs
}

fn sort_pairs(mut pairs: HashSet<(i32, i32)>) -> Vec<i32> {
    // Given a vector of pairs (a, b) indicating that a comes before
    // b in the sorted vector, return the sorted vector
    // println!("Sorting pairs: {:?}", pairs);
    let mut sorted_values = Vec::new();
    while !pairs.is_empty() {
        let fronts: HashSet<i32> = pairs.iter().map(|pair| pair.0).collect();
        let backs: HashSet<i32> = pairs.iter().map(|pair| pair.1).collect();

        if pairs.len() == 1 {
            // Handle the final pair case
            let pair = pairs.iter().next().unwrap();
            sorted_values.push(pair.0);
            sorted_values.push(pair.1);
            break;
        }

        let &next = fronts.difference(&backs).next().expect("Pairs don't give a unique ordering");
        // Find elements in `fronts` that are not in `backs` (no dependencies)
        sorted_values.push(next);

        // Remove pairs starting with the `next` element
        pairs = pairs
            .into_iter()
            .filter(|&(a, _)| a != next)
            .collect();

    }

    sorted_values
}

fn test_single_line(line: &str, pairs: &Vec<(i32, i32)>) -> i32 {
    println!("Processing line: {}", line);
    
    let mut relevant_pairs = HashSet::new();

    // Split the line by ','
    let values = line.split(',').map(|value_str| value_str.trim().parse().expect("Failed to parse value")).collect::<Vec<i32>>();
    println!("Values: {:?}", values);

    for pair in pairs {
        if values.contains(&pair.0) && values.contains(&pair.1) {
            relevant_pairs.insert(*pair);
        }
    }

    // Sort the relevant_pairs
    let ordered_values = sort_pairs(relevant_pairs);
    println!("Ordered values: {:?}", ordered_values);

    if ordered_values == values {
        return 0;
    }

    ordered_values[(ordered_values.len() - 1) / 2]
}

fn main() {
    let mut lines = _INPUT.lines();

    // Call the function to process lines until a blank line is found
    let pairs = get_pairs(&mut lines);
    // println!("{:?}", pairs);

    // Apply test_single_line function to the remaining lines
    let sol = lines.map(|line| test_single_line(line, &pairs)).sum::<i32>();
    println!("Solution: {}", sol);
}
