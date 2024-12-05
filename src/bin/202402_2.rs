static _TEST_INPUT: &str = include_str!("202402_test_input.txt");
static _INPUT: &str = include_str!("202402_input.txt");

fn is_safe(vec: &[i32]) -> bool {
    vec.windows(2)
        .map(|pair| pair[1] - pair[0]) // Compute the differences
        .try_fold(None, |is_inc, diff| match is_inc {
            // is_inc indicates whether the sequence is increasing or decreasing
            // - OK(None) is uninitialized
            // - OK(Some(true)) is increasing
            // - OK(Some(false)) is decreasing
            // - Err(()) is not monotonic
            None if [1, 2, 3].contains(&diff) => Ok(Some(true)), // Initialize to increasing
            None if [-1, -2, -3].contains(&diff) => Ok(Some(false)), // Initialize to decreasing

            Some(true) if [1, 2, 3].contains(&diff) => Ok(Some(true)), // Continue increasing
            Some(false) if [-1, -2, -3].contains(&diff) => Ok(Some(false)), // Continue decreasing

            _ => Err(()),
        })
        .is_ok()
}

fn missing_element_iterator(vec: Vec<i32>) -> impl Iterator<Item = Vec<i32>> {
    (0..vec.len()).map(move |i| {
        let mut new_vec = Vec::with_capacity(vec.len() - 1);
        new_vec.extend_from_slice(&vec[..i]);
        new_vec.extend_from_slice(&vec[i + 1..]);
        new_vec
    })
}

fn main() {
    let sol = _INPUT
        .lines()
        .map(|line| {
            let vec: Vec<i32> = line.split_whitespace().map(|s| s.parse::<i32>().unwrap()).collect();
            if missing_element_iterator(vec).any(|vec| is_safe(&vec)) {
                1
            } else {
                0
            }
        })
        .sum::<i32>();

    println!("sol: {:?}", sol);
}
