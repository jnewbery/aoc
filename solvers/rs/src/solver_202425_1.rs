use itertools::Itertools;

pub fn solve_202425_1(input: &str) -> String {
    let mut locks: Vec<[u32; 5]> = Vec::new();
    let mut keys: Vec<[u32; 5]> = Vec::new();
    for schematic in input.lines().into_iter().chunks(8).into_iter() {
        let mut lock_key = [0; 5];
        for (i, row) in schematic.collect::<Vec<&str>>().iter().enumerate() {
            // println!("{:?}", row);
            for (j, c) in row.chars().enumerate() {
                if c == '#' {
                    lock_key[j] += 2u32.pow(i as u32);
                }
            }
        }
        // println!("{:?}", lock_key);
        if lock_key[0] & 2u32.pow(6) != 0 {
            locks.push(lock_key);
        } else {
            keys.push(lock_key);
        }
    }
    // println!("{} locks, {} keys", locks.len(), keys.len());
    // println!("Locks\n{:?}", locks);
    // println!("Keys\n{:?}", keys);
    let mut sol = 0;
    for (lock, key) in locks.iter().cartesian_product(keys.iter()) {
        if (0..5).all(|i| lock[i] & key[i] == 0) {
            sol += 1;
        }
    }
    // println!("{:?}", sol);
    return sol.to_string();
}
