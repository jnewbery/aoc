use std::io;

static TEST_INPUT: &str = include_str!("202401_test_input.txt");
static INPUT: &str = include_str!("202401_input.txt");

fn main() -> io::Result<()> {

    // Create a vector to hold the two columns
    let mut columns: Vec<Vec<i32>> = vec![vec![], vec![]];

    // Read the file line by line
    for line in INPUT.lines() {
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

    // Sort the columns
    columns.iter_mut().for_each(|inner_vec| inner_vec.sort());

    // Zip the columns together to form rows
    let rows: Vec<Vec<i32>> = (0..columns[0].len())
        .map(|i| columns.iter().map(|inner_vec| inner_vec[i]).collect())
        .collect();

    // Calculate the sum of absolute differences
    let sum: i32 = rows
        .iter()
        .map(|v| (v[0] - v[1]).abs()) // Calculate absolute difference
        .sum(); // Sum all absolute differences

    // Print the parsed vectors
    // println!("Column 1: {:?}", columns[0]);
    // println!("Column 2: {:?}", columns[1]);
    // println!("Rows: {:?}", rows);
    println!("Sum: {:?}", sum);

    Ok(())
}
