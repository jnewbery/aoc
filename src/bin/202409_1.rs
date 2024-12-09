static _TEST_INPUT: &str = include_str!("202409_test_input.txt");
static _INPUT: &str = include_str!("202409_input.txt");

fn expand(disk: &str) -> Vec<Option<i32>> {
    let mut bytes: Vec<Option<i32>> = Vec::new();
    disk.chars().skip_while(|c| !c.is_digit(10)).
        fold((&mut bytes, 0, true), |acc, c| {
        // if c isn't a digit, exit
        if !c.is_digit(10) {
            return acc;
        } else if acc.2 {
            println!("{} {}", acc.1, c);
            acc.0.extend(std::iter::repeat(Some(acc.1)).take(c.to_digit(10).unwrap() as usize));
            (acc.0, acc.1 + 1, false)
        } else {
            println!("{} {}", acc.1, c);
            acc.0.extend(std::iter::repeat(None).take(c.to_digit(10).unwrap() as usize));
            (acc.0, acc.1, true)
        }
    }).0.to_vec()
}

fn main() {
    let disk = expand(_TEST_INPUT);
    println!("{:?}", disk);
}
