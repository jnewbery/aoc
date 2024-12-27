use std::collections::HashMap;

const PRUNE_MASK: u64 = (16777216 - 1) as u64;
const ROUNDS: usize = 2000;

fn calculate_next_secret_number(secret_number: u64) -> u64 {
    let secret_number = ((secret_number << 6) ^ secret_number) & PRUNE_MASK;
    let secret_number = ((secret_number >> 5) ^ secret_number) & PRUNE_MASK;
    let secret_number = ((secret_number << 11) ^ secret_number) & PRUNE_MASK;
    secret_number
}

fn calculate_seq_scores(secret_number: u64) -> HashMap<[i32; 4], u32> {
    let secret_numbers = std::iter::successors(Some(secret_number), |prev| {
        Some(calculate_next_secret_number(*prev))
    }).take(ROUNDS + 1);
    let prices = secret_numbers.map(|n| { n % 10 }).collect::<Vec<_>>();
    // println!("prices: {:?}", prices);
    let deltas = prices.windows(2).map(|w| w[1] as i32 - w[0] as i32).collect::<Vec<_>>();
    // println!("deltas: {:?}", deltas);
    let mut scores: HashMap<[i32; 4], u32> = HashMap::new();
    for (i, window) in deltas.windows(4).enumerate() {
        if i + 4 < prices.len() {
            if let [a, b, c, d] = window {
                let array = [*a as i32, *b as i32, *c as i32, *d as i32];
                if !scores.contains_key(&array) {
                    scores.insert(array, prices[i + 4] as u32);
                }
            }
        }
    }
    scores
}

pub fn solve(input: &str) -> String {
    let scores = input.lines().map(|line| {
        calculate_seq_scores(line.parse().unwrap())
    }).collect::<Vec<_>>();
    // println!("scores: {:?}", scores);
    let mut combined = HashMap::new();
    for seq in scores {
        for (key, value) in seq {
            let entry = combined.entry(key).or_insert(0);
            *entry += value;
        }
    }
    // println!("combined scores: {:?}", combined);
    combined.values().max().unwrap().to_string()
}
