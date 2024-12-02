static _TEST_INPUT: &str = include_str!("202402_test_input.txt");
static _INPUT: &str = include_str!("202402_input.txt");

fn is_safe(vec: Vec<i32>) -> bool {
    // println!("Checking vec: {:?}", vec);
    vec.windows(2)
        .map(|pair| pair[1] - pair[0]) // Compute the differences
        .fold(Ok(None), |is_inc, diff| match is_inc {
            // is_inc indicates whether the sequence is increasing or decreasing
            // - OK(None) is uninitialized
            // - OK(Some(true)) is increasing
            // - OK(Some(false)) is decreasing
            // - Err(()) is not monotonic
            Ok(None) if [1,2,3].contains(&diff) => Ok(Some(true)), // Initialize to increasing
            Ok(None) if [-1,-2,-3].contains(&diff) => Ok(Some(false)), // Initialize to decreasing

            Ok(Some(true)) if [1,2,3].contains(&diff) => Ok(Some(true)), // Continue increasing
            Ok(Some(false)) if [-1,-2,-3].contains(&diff) => Ok(Some(false)), // Continue decreasing

            _ => Err(()),
        })
        .is_ok()
}

fn main() {
    let mut ret = 0;
    for line in _INPUT.lines() {
        let vec: Vec<i32> = line.split_whitespace().map(|s| s.parse::<i32>().expect("Failed to parse column")).collect();
        if is_safe(vec) {
            // println!("safe!");
            ret += 1;
        } else {
            // println!("unsafe!");
        }

    }

    println!("ret: {:?}", ret);
}
