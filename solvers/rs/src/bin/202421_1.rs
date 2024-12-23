static TEST: bool = false;

use std::collections::HashMap;
use aoc::utils::Point;

static _TEST_INPUT: &str = include_str!("../../../../inputs/test/202421.txt");
static _INPUT: &str = include_str!("../../../../inputs/full/202421.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

fn get_pairs(code: &str) -> Vec<(char, char)> {
    std::iter::once(('A', code.chars().next().unwrap()))  // Arm starts by pointing at 'A'
        .chain(code.chars().zip(code.chars().skip(1)))    // Add the rest
        .collect()
}

fn type_numeric_code(code: &str, numeric_keypad: &HashMap<char, Point>) -> String {
    // Construct pairs of buttons that the arm must move between
    let pairs = get_pairs(code);

    // For each pair, calculate the path the arm must take
    let mut path: Vec<char> = Vec::new();
    for pair in pairs {
        let (from, to) = pair;
        // println!("{:?} -> {:?}", from, to);
        let mut from_point: Point = *numeric_keypad.get(&from).unwrap();
        let to_point = numeric_keypad.get(&to).unwrap();
        // println!("{:?} -> {:?}", from_point, to_point);
        while from_point != *to_point {
            if from_point.y < to_point.y {
                path.push('^');
                from_point.y += 1;
            } else if from_point.y > to_point.y {
                path.push('v');
                from_point.y -= 1;
            } else if from_point.x < to_point.x {
                path.push('>');
                from_point.x += 1;
            } else if from_point.x > to_point.x {
                path.push('<');
                from_point.x -= 1;
            }
        }
        path.push('A');
    }
    path.iter().collect()
}

fn type_directional_code(code: &str, numeric_keypad: &HashMap<char, Point>) -> String {
    // Construct pairs of buttons that the arm must move between
    let pairs = get_pairs(code);

    // For each pair, calculate the path the arm must take
    let mut path: Vec<char> = Vec::new();
    for pair in pairs {
        if pair == ('A', '<') {
            path.push('v');
            path.push('<');
            path.push('<');
            continue;
        }
        if pair == ('>', 'A') {
            path.push('>');
            path.push('>');
            path.push('^');
            continue;
        }
        let (from, to) = pair;
        // println!("{:?} -> {:?}", from, to);
        let mut from_point: Point = *numeric_keypad.get(&from).unwrap();
        let to_point = numeric_keypad.get(&to).unwrap();
        // println!("{:?} -> {:?}", from_point, to_point);
        while from_point != *to_point {
            if from_point.x < to_point.x {
                path.push('>');
                from_point.x += 1;
            } else if from_point.x > to_point.x {
                path.push('<');
                from_point.x -= 1;
            } else if from_point.y < to_point.y {
                path.push('^');
                from_point.y += 1;
            } else if from_point.y > to_point.y {
                path.push('v');
                from_point.y -= 1;
            }
        }
        path.push('A');
    }
    path.iter().collect()
}


fn main() {
    let mut numeric_keypad: HashMap<char, Point> = HashMap::new();
    for i in 1..=9 {
        numeric_keypad.insert((i + '0' as u8) as char, Point { x: ((i - 1) % 3) as i32, y: ((i-1) / 3 + 1) as i32 });
    }
    numeric_keypad.insert('0', Point { x: 1, y: 0 });
    numeric_keypad.insert('A', Point { x: 2, y: 0 });
    // println!("{:?}", numeric_keypad);

    let mut directional_keypad: HashMap<char, Point> = HashMap::new();
    directional_keypad.insert('^', Point { x: 1, y: 1 });
    directional_keypad.insert('A', Point { x: 2, y: 1 });
    directional_keypad.insert('<', Point { x: 0, y: 0 });
    directional_keypad.insert('v', Point { x: 1, y: 0 });
    directional_keypad.insert('>', Point { x: 2, y: 0 });
    // println!("{:?}", directional_keypad);

    let lines = INPUT.lines();
    let mut score = 0;
    for line in lines {
        let numeric_part = line.chars().filter(|c| c.is_numeric()).collect::<String>().parse::<i32>().unwrap();
        // let sol = type_code(&type_code(&type_code(line, &numeric_keypad), &directional_keypad), &directional_keypad);
        // println!("{:?}", line);
        let sol = &type_numeric_code(line, &numeric_keypad);
        // println!("{}", sol);
        let sol = &type_directional_code(sol, &directional_keypad);
        // println!("{}", sol);
        let sol = &type_directional_code(sol, &directional_keypad);
        // println!("{}", sol);
        score += numeric_part * (sol.len() as i32);
        // println!("{:?}: {:?} ({:?}) -> {}", line, sol, sol.len(), numeric_part * (sol.len() as i32));
    }
    println!("{:?}", score);
}
