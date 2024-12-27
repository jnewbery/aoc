fn solve_line(lines: &mut std::str::Lines) -> i64 {
    // println!("Solving puzzle: {:?}", lines);
    let a = lines.next().unwrap().split(|c: char| !c.is_numeric()).filter_map(|s| s.parse::<i64>().ok()).collect::<Vec<i64>>();
    let b = lines.next().unwrap().split(|c: char| !c.is_numeric()).filter_map(|s| s.parse::<i64>().ok()).collect::<Vec<i64>>();
    let prize = lines.next().unwrap().split(|c: char| !c.is_numeric()).filter_map(|s| {
        match s.parse::<i64>() {
            Ok(val) => Some(val + 10000000000000),
            Err(_) => None,
        }}).collect::<Vec<i64>>();
    // println!("a: {:?}, b: {:?}, prize: {:?}", a, b, prize);

    let a_b_det = a[0] * b[1] - a[1] * b[0];
    if a_b_det == 0 {
        // It's a rank 1 matrix. Panic!
        panic!("Rank 1 matrix");
    }

    let a_prize_det = a[0] * prize[1] - a[1] * prize[0];
    let b_prize_det = b[0] * prize[1] - b[1] * prize[0];

    // println!("a_b_det: {:?}, a_prize_det: {:?}, b_prize_det: {:?}", a_b_det, a_prize_det, b_prize_det);
    // println!("a_prize_det % a_b_det: {:?}, b_prize_det % a_b_det: {:?}", a_prize_det % a_b_det, b_prize_det % a_b_det);

    if a_prize_det % a_b_det != 0 || b_prize_det % a_b_det != 0 {
        // println!("Solution not an integer");
        return 0;
    }

    let a_buttons = (b[1] * prize[0] - b[0] * prize[1]) / a_b_det;
    // println!("a_buttons: {:?}", a_buttons);
    let b_buttons = (a[0] * prize[1] - a[1] * prize[0]) / a_b_det;
    // println!("b_buttons: {:?}", b_buttons);

    if a_buttons < 0 || b_buttons < 0 {
        return 0;
    }

    3 * a_buttons + b_buttons
}

pub fn solve(input: &str) -> String {
    let puzzles = &mut input.split("\n\n").map(|line| line.lines());

    let sol = puzzles.map(|mut lines| { solve_line(&mut lines) }).sum::<i64>();
    // println!("{}", sol);
    sol.to_string()
}
