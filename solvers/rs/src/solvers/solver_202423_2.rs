use fxhash::{FxHashMap, FxHashSet};
use itertools::Itertools;

fn bron_kerbosch(
    graph: &FxHashMap<String, Vec<String>>,
    r: &mut Vec<String>,
    p: &Vec<String>,
    x: &Vec<String>,
    cliques: &mut FxHashSet<Vec<String>>,
) {
    if p.is_empty() && x.is_empty() {
        cliques.insert(r.clone());
        return;
    }
    let mut p = p.clone();
    while !p.is_empty() {
        let v = p.pop().unwrap();
        let mut r = r.clone();
        r.push(v.clone());
        let mut p = p.clone();
        let mut x = x.clone();
        p.retain(|x| graph.get(&v).unwrap().contains(x));
        x.retain(|x| graph.get(&v).unwrap().contains(x));
        bron_kerbosch(graph, &mut r, &p, &x, cliques);
        x.push(v);
    }
}

pub fn solve(input: &str) -> String {
    let mut graph: FxHashMap<String, Vec<String>> = FxHashMap::default();
    for line in input.lines() {
        // println!("{:?}", line);
        let mut parts = line.split("-");
        let a = parts.next().unwrap().to_string();
        let b = parts.next().unwrap().to_string();
        graph.entry(a.clone()).or_insert(Vec::new()).push(b.clone());
        graph.entry(b.clone()).or_insert(Vec::new()).push(a.clone());
    }

    let mut cliques: FxHashSet<Vec<String>> = FxHashSet::default();
    bron_kerbosch(
        &graph,
        &mut Vec::new(),
        &graph.keys().cloned().collect(),
        &Vec::new(),
        &mut cliques,
    );
    cliques
        .into_iter()
        .max_by_key(|clique| clique.len())
        .unwrap()
        .into_iter()
        .sorted()
        .collect::<Vec<String>>()
        .join(",")
}
