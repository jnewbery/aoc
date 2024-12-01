use std::io;

static _TEST_INPUT: &str = include_str!("202401_test_input.txt");
static _INPUT: &str = include_str!("202401_input.txt");

fn main() -> io::Result<()> {
      // Use fold to parse lines into columns
      let columns: Vec<Vec<i32>> = _INPUT.lines().fold(vec![vec![], vec![]], |mut acc, line| {
          // Split the line into two columns
          let parts: Vec<&str> = line.split_whitespace().collect();
  
          // Parse each part into an integer and push to the respective column
          let a = parts[0].parse::<i32>().expect("Failed to parse first column");
          let b = parts[1].parse::<i32>().expect("Failed to parse second column");
          acc[0].push(a);
          acc[1].push(b);
  
          acc
      });
  
      // Sort the columns
      let mut sorted_columns = columns.clone();
      sorted_columns.iter_mut().for_each(|inner_vec| inner_vec.sort());
  
      // Zip the columns together to form rows
      let rows: Vec<Vec<i32>> = (0..sorted_columns[0].len())
          .map(|i| sorted_columns.iter().map(|inner_vec| inner_vec[i]).collect())
          .collect();
  
      // Calculate the sum of absolute differences
      let sum: i32 = rows
          .iter()
          .map(|v| (v[0] - v[1]).abs()) // Calculate absolute difference
          .sum(); // Sum all absolute differences
  
      // Print the parsed vectors
      println!("Sum: {:?}", sum);
  
      Ok(())
  }
