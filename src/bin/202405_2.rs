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

fn test_single_line(line: &str, pairs: &Vec<(i32, i32)>) -> i32 {
    // println!("Processing line: {}", line);

    // Split the line by ','
    let values = line.split(',').map(|value_str| value_str.trim().parse().expect("Failed to parse value")).collect::<Vec<i32>>();

    for pair in pairs {
        if values.contains(&pair.0) && values.contains(&pair.1) {
            // If the index of pair.1 is before the index of pair.0, return 0
            if values.iter().position(|&x| x == pair.1) < values.iter().position(|&x| x == pair.0) {
                return 0;
            } 
        }
    }

    values[(values.len() - 1) / 2]
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
