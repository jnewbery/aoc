static _TEST_INPUT: &str = include_str!("inputs/202413_test.txt");
static _INPUT: &str = include_str!("inputs/202413.txt");

fn solve(lines: &mut std::str::Lines) -> i32 {
    // println!("Solving puzzle: {:?}", lines);
    let a = lines.next().unwrap().split(|c: char| !c.is_numeric()).filter_map(|s| s.parse::<i32>().ok()).collect::<Vec<i32>>();
    let b = lines.next().unwrap().split(|c: char| !c.is_numeric()).filter_map(|s| s.parse::<i32>().ok()).collect::<Vec<i32>>();
    let prize = lines.next().unwrap().split(|c: char| !c.is_numeric()).filter_map(|s| s.parse::<i32>().ok()).collect::<Vec<i32>>();
    println!("a: {:?}, b: {:?}, prize: {:?}", a, b, prize);

    let a_b_det = a[0] * b[1] - a[1] * b[0];
    if a_b_det == 0 {
        // It's a rank 1 matrix. Panic!
        println!("Rank 1 matrix");
        panic!();
    }

    let a_prize_det = a[0] * prize[1] - a[1] * prize[0];
    let b_prize_det = b[0] * prize[1] - b[1] * prize[0];

    println!("a_b_det: {:?}, a_prize_det: {:?}, b_prize_det: {:?}", a_b_det, a_prize_det, b_prize_det);
    println!("a_prize_det % a_b_det: {:?}, b_prize_det % a_b_det: {:?}", a_prize_det % a_b_det, b_prize_det % a_b_det);

    if a_prize_det % a_b_det != 0 || b_prize_det % a_b_det != 0 {
        println!("Solution not an integer");
        return 0;
    }

    let a_buttons = (b[1] * prize[0] - b[0] * prize[1]) / a_b_det;
    println!("a_buttons: {:?}", a_buttons);
    let b_buttons = (a[0] * prize[1] - a[1] * prize[0]) / a_b_det;
    println!("b_buttons: {:?}", b_buttons);

    if a_buttons < 0 || a_buttons > 100 || b_buttons < 0 || b_buttons > 100 {
        return 0;
    }

    3 * a_buttons + b_buttons
}

fn main() {
    let puzzles = &mut _INPUT.split("\n\n").map(|line| line.lines());

    let sol = puzzles.map(|mut lines| { solve(&mut lines) }).sum::<i32>();
    println!("Solution: {}", sol);
}
