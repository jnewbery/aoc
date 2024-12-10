static _TEST_INPUT: &str = include_str!("202409_test_input.txt");
static _INPUT: &str = include_str!("202409_input.txt");

use std::iter;

fn read_from_front(disk: &str) -> impl Iterator<Item = Option<i32>> {
    let mut chars = disk.chars();
    let mut current_repeats = 0;
    let mut id = 0;
    let mut is_file = true;

    iter::from_fn(move || {
        // If we have more repetitions to process, do so
        if current_repeats == 0 {
            current_repeats = chars.next()?.to_digit(10)?; // If no char, return None
            if !is_file {
                id += 1; // Only increment the file id after a gap
            }
            is_file = !is_file; // Toggle between file and gap
        }

        current_repeats -= 1;

        Some(if is_file { Some(id) } else { None })
    })
}

// fn read_from_back(disk: &str, id: i32) -> impl Iterator<Item = i32> {
// }

fn expand(disk: &str) -> Vec<Option<i32>> {
    let mut bytes: Vec<Option<i32>> = Vec::new();
    disk.chars().skip_while(|c| !c.is_digit(10)).
        fold((&mut bytes, 0, true), |acc, c| {
        if acc.2 {
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
    let disk = expand(_TEST_INPUT.trim());
    println!("{:?}", disk);
}
