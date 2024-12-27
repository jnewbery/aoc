use std::collections::{HashMap, HashSet};

pub fn solve(input: &str) -> String {
    let mut pairs: HashMap<String, Vec<String>> = HashMap::new();
    let mut trios: HashSet<[String; 3]> = HashSet::new();
    for line in input.lines() {
        // println!("{:?}", line);
        let mut parts = line.split("-");
        let a = parts.next().unwrap().to_string();
        let b = parts.next().unwrap().to_string();
        pairs.entry(a.clone()).or_insert(Vec::new()).push(b.clone());
        pairs.entry(b.clone()).or_insert(Vec::new()).push(a.clone());
        for c in pairs.get(&a).unwrap() {
            if pairs.get(c).unwrap().contains(&b) {
                if !a.starts_with('t') && !b.starts_with('t') && !c.starts_with('t') {
                    continue;
                }
                let mut new_trio = [a.clone(), b.clone(), c.clone()];
                new_trio.sort();
                trios.insert(new_trio);
            }
        }
    }
    // println!("{:?} terminals", pairs.keys().len());
    // println!("{:?} pairs", pairs.values().map(Vec::len).sum::<usize>());
    // println!("{:?} trios", trios.len());
    trios.len().to_string()
}
