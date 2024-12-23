static TEST: bool = false;

static _TEST_INPUT: &str = include_str!("../../../../inputs/test/201501.txt");
static _INPUT: &str = include_str!("../../../../inputs/full/201501.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

fn main() {
    if let Some((pos, _)) = INPUT.chars().enumerate().scan(0, |floor, (pos, c)| {
        match c {
            '(' => *floor += 1,
            ')' => *floor -= 1,
            _ => panic!("Invalid character: {}", c),
        }
        Some((pos, *floor))
    }).find(|&(_, floor)| floor == -1) {
        println!("{}", pos + 1);
    }
}
