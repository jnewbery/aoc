use std::collections::HashMap;

#[derive(Debug, Clone)]
struct Gate {
    inputs: (String, String),
    operator: fn(bool, bool) -> bool,
}

#[derive(Debug)]
enum Input {
    WireVariant(bool),
    GateVariant(Gate),
}

fn resolve_wire<'a>(wire: &'a str, wires: &'a mut HashMap<String, Input>) -> bool {
    let gate: Gate = match wires.get(wire).unwrap() {
        Input::WireVariant(val) => {
            // println!("{}: {}", wire, val);
            return *val;
        },
        Input::GateVariant(gate) => {
            gate.clone()
        }
    };

    let (input1, input2) = &gate.inputs;
    let input1_val = match wires.get(input1.as_str()).unwrap() {
        Input::WireVariant(val) => *val,
        Input::GateVariant(_) => {
            resolve_wire(input1, wires)
        },
    };
    let input2_val = match wires.get(input2.as_str()).unwrap() {
        Input::WireVariant(val) => *val,
        Input::GateVariant(_) => {
            resolve_wire(input2, wires)
        },
    };
    let output = (gate.operator)(input1_val, input2_val);
    wires.insert(wire.to_string(), Input::WireVariant(output));
    return output;
}

pub fn solve(input: &str) -> String {
    if input.len() < 100 {
        return "No part 2".to_string();
    }
    let mut wires: HashMap<String, Input> = HashMap::new();
    for line in input.lines() {
        if line.contains(":") {
            let parts: Vec<&str> = line.split_whitespace().collect();
            let wire = &parts[0][..parts[0].len() - 1];
            let value = parts[1];
            if value == "1" {
                wires.insert(wire.to_string(), Input::WireVariant(true));
            } else if value == "0" {
                wires.insert(wire.to_string(), Input::WireVariant(false));
            } 
        } else if line.contains("->") {
            match line.split_whitespace().collect::<Vec<&str>>().as_slice() {
                [input1, "AND", input2, "->", output] => {
                    wires.insert(output.to_string(), Input::GateVariant(Gate {
                        inputs: (input1.to_string(), input2.to_string()),
                        operator: |a, b| a & b,
                    }));
                },
                [input1, "OR", input2, "->", output] => {
                    wires.insert(output.to_string(), Input::GateVariant(Gate {
                        inputs: (input1.to_string(), input2.to_string()),
                        operator: |a, b| a | b,
                    }));
                },
                [input1, "XOR", input2, "->", output] => {
                    wires.insert(output.to_string(), Input::GateVariant(Gate {
                        inputs: (input1.to_string(), input2.to_string()),
                        operator: |a, b| a ^ b,
                    }));
                },
                _ => panic!("Invalid input"),
            }
        }
    }
    // println!("{:?}", wires);

    for wire in wires.keys().cloned().collect::<Vec<String>>() {
        resolve_wire(&wire, &mut wires);
    }
    // println!("{:?}", wires);
    // println!("{:?}", wires.len());

    let mut z_wires: Vec<(String, u32)> = wires.iter().filter(|(key, _)| key.starts_with("z")).map(|(k, v)| (k.clone(), match v {
        Input::WireVariant(val) => if *val { 1 } else { 0 },
        Input::GateVariant(_) => panic!("Invalid input"),
    })).collect::<Vec<(String, u32)>>();
    z_wires.sort_by_key(|(key, _)| key.clone());
    z_wires.reverse();
    // println!("{:?}", z_wires.iter().map(|(_, val)| format!("{}", val)).collect::<Vec<String>>().join(""));
    let sol = z_wires.iter().fold(0 as u64, |acc, (_, val)| 2 * acc + (*val as u64));

    return sol.to_string();
}
