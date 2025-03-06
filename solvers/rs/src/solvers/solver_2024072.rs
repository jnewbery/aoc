// Implementation working from target backwards through operands for more aggressive pruning
use std::collections::HashSet;

fn test_line(line: &str) -> i64 {
    let operands = line.split(|c: char| !c.is_numeric() && c != '-')
        .filter_map(|s| s.parse::<i64>().ok())
        .collect::<Vec<i64>>();
    
    if operands.is_empty() {
        return 0;
    }
    
    let target = operands[0];
    if operands.len() == 1 {
        return target; // Only the target, no operations to perform
    }
    
    // Reverse the operands (except target) to work backwards
    let operands = &operands[1..];
    
    // Start with the target as our only possible result
    let mut possible_results: HashSet<i64> = HashSet::new();
    possible_results.insert(target);
    
    // Work backwards through the operands
    for i in (1..operands.len()).rev() {
        let operand = operands[i];
        let mut new_results = HashSet::new();
        
        for result in possible_results {
            // Addition (reverse is subtraction)
            if result > operand {
                new_results.insert(result - operand);
            }
            
            // Multiplication (reverse is division)
            if result % operand == 0 {
                new_results.insert(result / operand);
            }
            
            // Concatenation (reverse is checking if result ends with operand)
            let operand_str = operand.to_string();
            let result_str = result.to_string();
            if result_str.ends_with(&operand_str) {
                let prefix_len = result_str.len() - operand_str.len();
                if prefix_len > 0 {
                    if let Ok(prefix_val) = result_str[..prefix_len].parse::<i64>() {
                        new_results.insert(prefix_val);
                    }
                }
            }
        }
        
        possible_results = new_results;
        if possible_results.is_empty() {
            return 0; // Early termination if no valid paths
        }
    }
    
    // Check if the first operand is in our final set of possible results
    if possible_results.contains(&operands[0]) {
        return target;
    }
    
    0
}

pub fn solve(input: &str) -> String {
    let sol = input.lines().map(|line| test_line(line)).sum::<i64>();
    // println!("{:?}", sol);
    sol.to_string()
}
