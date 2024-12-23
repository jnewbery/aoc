static TEST: bool = false;

use std::collections::HashSet;

static _TEST_INPUT: &str = include_str!("inputs/202405_test.txt");
static _INPUT: &str = include_str!("inputs/202405.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

fn get_pairs(lines: &mut std::str::Lines) -> Vec<(i32, i32)> {
    lines.take_while(|line| !line.is_empty())
        .map(|line| {
            let (left, right) = line.split_once('|').expect("Failed to split line");
            let left: i32 = left.trim().parse().expect("Failed to parse left integer");
            let right: i32 = right.trim().parse().expect("Failed to parse right integer");
            (left, right)
        })
        .collect()
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

        // Find elements in `fronts` that are not in `backs` (no dependencies)
        let &next = fronts.difference(&backs).next().expect("Pairs don't give a unique ordering");
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
    // println!("Processing line: {}", line);
    
    // Split the line by ','
    let values = line.split(',').map(|value_str| value_str.trim().parse().expect("Failed to parse value")).collect::<Vec<i32>>();
    // println!("Values: {:?}", values);

    let relevant_pairs: HashSet<_> = pairs.iter()
        .filter(|pair| values.contains(&pair.0) && values.contains(&pair.1))
        .copied()
        .collect();

    // Get an ordered list off values that respect the ordering of pairs
    let ordered_values = sort_pairs(relevant_pairs);
    // println!("Ordered values: {:?}", ordered_values);

    if ordered_values == values {
        return 0;
    }

    ordered_values[(ordered_values.len() - 1) / 2]
}

fn main() {
    let mut lines = INPUT.lines();

    // Call the function to process lines until a blank line is found
    let pairs = get_pairs(&mut lines);
    // println!("{:?}", pairs);

    // Apply test_single_line function to the remaining lines
    let sol = lines.map(|line| test_single_line(line, &pairs)).sum::<i32>();
    println!("{}", sol);
}
