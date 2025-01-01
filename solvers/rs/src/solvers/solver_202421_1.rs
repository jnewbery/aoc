use std::collections::HashMap;
use aoc::utils::Point;
use std::collections::HashSet;
use itertools::Itertools;

fn get_pairs(code: &str) -> Vec<(char, char)> {
    std::iter::once(('A', code.chars().next().unwrap()))  // Arm starts by pointing at 'A'
        .chain(code.chars().zip(code.chars().skip(1)))    // Add the rest
        .collect()
}

fn type_pair(pair: (Point, Point), numeric: bool) -> HashSet<String> {
    // let mut paths = type_pair(pair);
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
    let mut paths: Vec<_> = path.clone().into_iter().permutations(path.len()).unique().collect();

    if numeric {
        // Prune out paths that visit (0, 0) (ie all 'v's followed by all '>'s or all '<'s followed by all '^'s)
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
    } else {  // Directional
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
    }

    paths.into_iter().map(|p| p.into_iter().collect::<String>() + "A").collect()
}

fn type_code(
    code: &str,
    depth: u32,
    numeric: bool,
    directional_keypad: &HashMap<char, Point>,
    numeric_keypad: &HashMap<char, Point>,
    cache: &mut HashMap<(String, u32, bool), u32>) -> u32
{
    // println!("type_code({}, {}, {})", code, depth, numeric);
    if cache.contains_key(&(code.to_string(), depth, numeric)) {
        return *cache.get(&(code.to_string(), depth, numeric)).unwrap();
    } else if depth == 0 {
        return code.len() as u32;
    }
    let mut length = 0;
    let pairs = get_pairs(&code);
    for pair in pairs {
        // println!("solving {:?}", pair);
        let strings = if numeric {
            type_pair((*numeric_keypad.get(&pair.0).unwrap(), *numeric_keypad.get(&pair.1).unwrap()), true)
        } else {
            type_pair((*directional_keypad.get(&pair.0).unwrap(), *directional_keypad.get(&pair.1).unwrap()), false)
        };
        // println!("strings: {:?}", strings);

        length += strings.iter().map(|s| {
            let result = type_code(&s, depth - 1, false, directional_keypad, numeric_keypad, cache);
            result
        }).min().unwrap();
    }
    cache.insert((code.to_string(), depth, numeric), length);
    length
}

fn solve_line(
    line: &str,
    numeric_keypad: &HashMap<char, Point>,
    directional_keypad: &HashMap<char, Point>,
    cache: &mut HashMap<(String, u32, bool), u32>) -> u32
{
    let numeric_part = line.chars().filter(|c| c.is_numeric()).collect::<String>().parse::<u32>().unwrap();
    let path_len = type_code(line, 3, true, directional_keypad, numeric_keypad, cache);
    // println!("numeric_part: {}, path_len: {}, score: {}", numeric_part, path_len, numeric_part * path_len);
    numeric_part * path_len
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
    let mut score: u32 = 0;
    let mut cache: HashMap<(String, u32, bool), u32> = HashMap::new();
    for line in lines {
        // println!("Solving line: {}", line);
        score += solve_line(line, &numeric_keypad, &directional_keypad, &mut cache);
    }
    // println!("{:?}", score);
    score.to_string()
}
