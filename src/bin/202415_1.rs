static TEST: bool = true;

static _TEST_INPUT: &str = include_str!("inputs/202415_test.txt");
static _INPUT: &str = include_str!("inputs/202415.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

// type Point = (i32, i32);
// enum cell {
//     Empty,
//     Wall,
//     Box,
// }

fn main() {
    println!("{}", INPUT);
}
