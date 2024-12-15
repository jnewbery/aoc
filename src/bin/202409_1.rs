static TEST: bool = true;

use std::iter;

static _TEST_INPUT: &str = include_str!("inputs/202409_test.txt");
static _INPUT: &str = include_str!("inputs/202409.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

fn read_from_front<'a>(disk: &'a str) -> impl Iterator<Item = Option<i32>> + 'a {
    let mut chars = disk.chars();
    let mut current_repeats = chars.next().unwrap().to_digit(10).unwrap();
    let mut id = 0;
    let mut is_file = true;

    iter::from_fn(move || {
        // If we have more repetitions to process, do so
        // println!("read_from_front: {} {}", current_repeats, id);
        while current_repeats == 0 {
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

fn read_from_back<'a>(disk: &'a str) -> impl Iterator<Item = Option<i32>> + 'a {
    let mut chars = disk.chars().rev();
    let mut current_repeats = chars.next().unwrap().to_digit(10).unwrap();
    let mut id = ((disk.len() as i32) - 1) / 2;
    let mut is_file = true;

    iter::from_fn(move || {
        // If we have more repetitions to process, do so
        // println!("read_from_back: {} {}", current_repeats, id);
        while current_repeats == 0 {
            current_repeats = chars.next()?.to_digit(10)?; // If no char, return None
            if !is_file {
                id -= 1; // Only increment the file id after a gap
            }
            is_file = !is_file; // Toggle between file and gap
        }

        current_repeats -= 1;

        Some(if is_file { Some(id) } else { None })
    })
}

fn expand(disk: &str) -> Vec<i32> {
    let mut front_iter = read_from_front(disk);
    let mut back_iter = read_from_back(disk);
    let disk_len = disk.chars().map(|c| c.to_digit(10).unwrap()).step_by(2).sum::<u32>() as i32;
    // println!("Disk length: {}", disk_len);
    let mut compressed_disk: Vec<i32> = Vec::new();
    let mut front = front_iter.next();
    let mut back = back_iter.next();
    while compressed_disk.len() < disk_len as usize {
        match (front.unwrap(), back.unwrap()) {
            (Some(f), _) => {
                compressed_disk.push(f);
                front = front_iter.next();
            },
            (None, Some(b)) => {
                compressed_disk.push(b);
                front = front_iter.next();
                back = back_iter.next();
            }
            (None, None) => {
                back = back_iter.next();
            }
        }
    }
    compressed_disk
}

fn main() {
    let disk = expand(INPUT.trim());
    // println!("{:?}", disk);
    let sol = disk.iter().enumerate().fold(0 as i64, |acc, (i, x)| acc + (x * i as i32) as i64);
    println!("{}", sol);
}
