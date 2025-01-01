const PRUNE_MASK: u64 = (16777216 - 1) as u64;

fn calculate_next_secret_number(secret_number: u64) -> u64 {
    let secret_number = ((secret_number << 6) ^ secret_number) & PRUNE_MASK;
    let secret_number = ((secret_number >> 5) ^ secret_number) & PRUNE_MASK;
    let secret_number = ((secret_number << 11) ^ secret_number) & PRUNE_MASK;
    secret_number
}

fn calculate_nth_secret_number(secret_number: u64, n: u64) -> u64 {
    let mut secret_number = secret_number;
    for _ in 0..n {
        secret_number = calculate_next_secret_number(secret_number);
    }
    secret_number
}

pub fn solve(input: &str) -> String {
    input.lines().map(|line| {
        let secret_number: u64 = line.parse().unwrap();
        let secret_number = calculate_nth_secret_number(secret_number, 2000);
        secret_number
    }).sum::<u64>().to_string()
}
