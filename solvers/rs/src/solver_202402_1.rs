static TEST: bool = false;

static _TEST_INPUT: &str = include_str!("../../../inputs/test/202402.txt");
static _INPUT: &str = include_str!("../../../inputs/full/202402.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

fn is_safe(vec: &Vec<i32>) -> bool {
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

pub fn solve_202402_1() -> String {
    let ret = INPUT
        .lines()
        .map(|line| {
            line.split_whitespace().map(|s| s.parse::<i32>().expect("Failed to parse column")).collect()
        })
        .filter(|vec| is_safe(vec))
        .count();

    // println!("{:?}", ret);
    ret.to_string()
}
