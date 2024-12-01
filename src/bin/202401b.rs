use std::io;
use std::collections::HashMap;

static TEST_INPUT: &str = include_str!("202401_test_input.txt");
static INPUT: &str = include_str!("202401_input.txt");

fn main() -> io::Result<()> {

    // Create a vector to hold the two columns
    let mut columns: Vec<Vec<i32>> = vec![vec![], vec![]];

    // Read the file line by line
    for line in TEST_INPUT.lines() {
        // Split the line into two columns
        let parts: Vec<&str> = line.split_whitespace().collect();

        // Ensure there are exactly two columns
        if parts.len() == 2 {
            // Parse each part into an integer and push to the respective column
            if let (Ok(a), Ok(b)) = (parts[0].parse::<i32>(), parts[1].parse::<i32>()) {
                columns[0].push(a);
                columns[1].push(b);
            } else {
                eprintln!("Warning: Could not parse line: {}", line);
            }
        } else {
            eprintln!("Warning: Incorrect format in line: {}", line);
        }
    }

    let counts1 = columns[0].clone().into_iter().fold(HashMap::new(), |mut acc, num| {
        *acc.entry(num).or_insert(0) += 1;
        acc
    });

    let counts2 = columns[1].clone().into_iter().fold(HashMap::new(), |mut acc, num| {
        *acc.entry(num).or_insert(0) += 1;
        acc
    });

    // Print the parsed vectors
    println!("counts1: {:?}", counts1);
    println!("counts2: {:?}", counts2);

    Ok(())
}
