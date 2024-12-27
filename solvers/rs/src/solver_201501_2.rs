pub fn solve(input: &str) -> String {
    if let Some((pos, _)) = input.chars().enumerate().scan(0, |floor, (pos, c)| {
        match c {
            '(' => *floor += 1,
            ')' => *floor -= 1,
            _ => panic!("Invalid character: {}", c),
        }
        Some((pos, *floor))
    }).find(|&(_, floor)| floor == -1) {
        // println!("{}", pos + 1);
        return (pos + 1).to_string();
    } else {
        panic!("Basement not found");
    }
}
