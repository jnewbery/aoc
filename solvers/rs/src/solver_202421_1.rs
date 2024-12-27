use std::collections::HashMap;
use aoc::utils::Point;
use std::collections::HashSet;
use itertools::Itertools;

fn get_pairs(code: &str) -> Vec<(char, char)> {
    std::iter::once(('A', code.chars().next().unwrap()))  // Arm starts by pointing at 'A'
        .chain(code.chars().zip(code.chars().skip(1)))    // Add the rest
        .collect()
}

fn type_pair(pair: (Point, Point)) -> Vec<Vec<char>> {
    // println!("{:?} -> {:?}", from, to);
    let from_point: Point = pair.0;
    let to_point = pair.1;
    // println!("{:?} -> {:?}", from_point, to_point);
    let mut path: Vec<char> = Vec::new();
    if from_point.y < to_point.y {
        path.extend((from_point.y..to_point.y).map(|_| '^'));
    } else if from_point.y > to_point.y {
        path.extend((to_point.y..from_point.y).map(|_| 'v'));
    }
    if from_point.x < to_point.x {
        path.extend((from_point.x..to_point.x).map(|_| '>'));
    } else if from_point.x > to_point.x {
        path.extend((to_point.x..from_point.x).map(|_| '<'));
    }
    path.clone().into_iter().permutations(path.len()).unique().collect()
}

fn type_directional_pair(pair: (Point, Point)) -> HashSet<String> {
    let mut paths = type_pair(pair);

    // Prune out paths that visit (0, 1) (ie all 'v's followed by all '>'s)
    if pair.0.x == 0 && pair.1.y == 1 {
        paths.retain(|p| {
            if p.windows(2).all(|c| c == ['^', '^'] || c == ['^', '>'] || c == ['>', '>']) {
                return false;
            }
            true
        });
    } else if pair.0.y == 1 && pair.1.x == 0 {
        paths.retain(|p| {
            if p.windows(2).all(|c| c == ['<', '<'] || c == ['<', 'v'] || c == ['v', 'v']) {
                return false;
            }
            true
        });
    }

    paths.into_iter().map(|p| p.into_iter().collect()).collect()
}

fn type_directional_code(codes: &HashSet<String>, directional_keypad: &HashMap<char, Point>) -> HashSet<String> {
    let mut paths: HashSet<String> = HashSet::new();
    for code in codes {
        // Construct pairs of buttons that the arm must move between
        let pairs = get_pairs(&code);

        // For each pair, calculate the path the arm must take
        let pair_paths: Vec<HashSet<String>> = pairs
            .iter()
            .map(|pair| type_directional_pair((*directional_keypad.get(&pair.0).unwrap(), *directional_keypad.get(&pair.1).unwrap())))
            .collect();
        paths.extend(pair_paths.iter().map(|set| set.iter()).multi_cartesian_product().map(|v| v.into_iter().join("A") + "A"));
    }
    paths
}

fn type_numeric_pair(pair: (char, char), numeric_keypad: &HashMap<char, Point>) -> HashSet<String> {
    let from_point = *numeric_keypad.get(&pair.0).unwrap();
    let to_point = *numeric_keypad.get(&pair.1).unwrap();
    let pair = (from_point, to_point);
    let mut paths = type_pair(pair);

    // Prune out paths that visit (0, 0) (ie all 'v's followed by all '>'s)
    if pair.0.x == 0 && pair.1.y == 0 {
        paths.retain(|p| {
            // println!("Testing {:?}", p.windows(2).collect::<Vec<_>>());
            if p.windows(2).all(|c| c == ['v', 'v'] || c == ['v', '>'] || c == ['>', '>']) {
                return false;
            }
            true
        });
    } else if pair.0.y == 0 && pair.1.x == 0 {
        paths.retain(|p| {
            // println!("Testing {:?}", p.windows(2).collect::<Vec<_>>());
            if p.windows(2).all(|c| c == ['<', '<'] || c == ['<', '^'] || c == ['^', '^']) {
                return false;
            }
            true
        });
    }

    paths.into_iter().map(|p| p.into_iter().collect::<String>() + "A").collect()
}

fn solve_line(line: &str, numeric_keypad: &HashMap<char, Point>, directional_keypad: &HashMap<char, Point>) -> i32 {
    let numeric_part = line.chars().filter(|c| c.is_numeric()).collect::<String>().parse::<i32>().unwrap();
    let mut paths_lens = 0;
    for pair in get_pairs(&line) {
        // println!("{:?}", pair);
        let strings = type_numeric_pair(pair, numeric_keypad);
        // println!("{:?}", strings);
        let strings = type_directional_code(&strings, &directional_keypad);
        // println!("{:?}", strings);
        let strings = type_directional_code(&strings, &directional_keypad);
        // println!("{:?}", strings);
        let sols_len = strings.into_iter().map(|s| s.len()).min().unwrap();
        // println!("{}", sols_len);
        paths_lens += sols_len;
    }
    // println!("numeric_part: {}, paths_lens: {}, score: {}", numeric_part, paths_lens, numeric_part * paths_lens as i32);
    numeric_part * paths_lens as i32
}

pub fn solve(input: &str) -> String {
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

    let lines = input.lines();
    let mut score = 0;
    for line in lines {
        // println!("Solving line: {}", line);
        score += solve_line(line, &numeric_keypad, &directional_keypad);
    }
    // println!("{:?}", score);
    score.to_string()
}
