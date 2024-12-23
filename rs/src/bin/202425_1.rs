static TEST: bool = true;

static _TEST_INPUT: &str = include_str!("../../../inputs/test/202425.txt");
static _INPUT: &str = include_str!("../../../inputs/full/202425.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

fn main() {
    println!("{}", INPUT);
}
