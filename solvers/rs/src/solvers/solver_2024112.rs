use std::collections::HashMap;

fn split_digits_if_even(n: i64) -> Option<(i64, i64)> {
    // If the decimal representation of n has an even number of digits,
    // return a tuple of the front and back halves
    let chars = n.to_string().chars().collect::<Vec<char>>();
    if chars.len() % 2 != 0 {
        return None;
    }
    let front = chars[0..chars.len() / 2].iter().collect::<String>().parse::<i64>().unwrap();
    let back = chars[chars.len() / 2..chars.len()].iter().collect::<String>().parse::<i64>().unwrap();
    Some((front, back))
}

fn blink_n_times(stones: &HashMap<i64, i64>, n: i64) -> i64 {
    // Return the number of stones after n blinks
    // println!("{:?}", stones);
    if n == 0 {
        // We done
        return stones.values().sum();
    }

    let new_stones = stones.iter().fold(HashMap::new(), |mut acc, (k, v)| {
        if k == &0 {
            *acc.entry(1).or_insert(0) += v;
        } else if let Some((front, back)) = split_digits_if_even(*k) {
            *acc.entry(front).or_insert(0) += v;
            *acc.entry(back).or_insert(0) += v;
        } else {
            *acc.entry(k * 2024).or_insert(0) += v;
        }
        acc
    });

    // tail recurse
    blink_n_times(&new_stones, n - 1)
}

pub fn solve(input: &str) -> String {
    // Prime the pump
    let stones = input.split(|c: char| !c.is_numeric())
        .filter_map(|s| s.parse::<i64>().ok()).fold(HashMap::new(), |mut acc, s| {
            *acc.entry(s).or_insert(0) += 1;
            acc
        });
    // println!("{:?}", stones);

    // let 'er rip
    let sol = blink_n_times(&stones, 75);
    // println!("{}", sol);
    sol.to_string()
}
