use std::collections::HashMap;

fn even_digits(n: i64) -> bool {
    n.abs().to_string().len() % 2 == 0
}

fn split_digits(n: i64) -> (i64, i64) {
    let chars = n.to_string().chars().collect::<Vec<char>>();
    let front = chars[0..chars.len() / 2].iter().collect::<String>().parse::<i64>().unwrap();
    let back = chars[chars.len() / 2..chars.len()].iter().collect::<String>().parse::<i64>().unwrap();
    (front, back)
}

fn blink_n_times(stones: &HashMap<i64, i64>, n: i64) -> i64 {
    // println!("{:?}", stones);
    if n == 0 {
        return stones.values().sum();
    }

    let new_stones = stones.iter().fold(HashMap::new(), |mut acc, (k, v)| {
        match k {
            0 => {
                *acc.entry(1).or_insert(0) += v;
            },
            _ if even_digits(*k)=> {
                let (front, back) = split_digits(*k);
                *acc.entry(front).or_insert(0) += v;
                *acc.entry(back).or_insert(0) += v;
            },
            _ => {
                *acc.entry(k * 2024).or_insert(0) += v;
            },
        }
        acc
    });
    blink_n_times(&new_stones, n - 1)
}

pub fn solve(input: &str) -> String {
    // Get count of stones from input
    let stones = input.split(|c: char| !c.is_numeric() && c != '-')
        .filter_map(|s| s.parse::<i64>().ok()).fold(HashMap::new(), |mut acc, s| {
            *acc.entry(s).or_insert(0) += 1;
            acc
        });
    // println!("{:?}", stones);

    let sol = blink_n_times(&stones, 25);
    // println!("{}", sol);
    sol.to_string()
}
