pub fn solve_201501_1(input: &str) -> String {
    let sol = input.trim().chars().map(|c| match c {
        '(' => 1,
        ')' => -1,
        _ => {
            panic!("Invalid character: {}", c);
        }
    }).sum::<i32>();
    // println!("{}", sol);
    return sol.to_string();
}
