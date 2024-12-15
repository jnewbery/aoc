static _TEST: bool = false;
static _TEST_INPUT: &str = include_str!("inputs/201501_test.txt");
static _INPUT: &str = include_str!("inputs/201501.txt");

const INPUT: &str = if _TEST { _TEST_INPUT } else { _INPUT };

fn main() {
    let sol = INPUT.trim().chars().map(|c| match c {
        '(' => 1,
        ')' => -1,
        _ => {
            panic!("Invalid character: {}", c);
        }
    }).sum::<i32>();
    println!("Solution: {}", sol);
}
