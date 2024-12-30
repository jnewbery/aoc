use std::collections::HashSet;

#[derive(Debug, PartialEq, Eq)]
enum Operator {
    And,
    Or,
    Xor,
}

#[derive(Debug)]
struct Gate {
    inputs: Vec<String>,
    output: String,
    operator: Operator,
}

pub fn solve(input: &str) -> String {
    let mut gates: Vec<Gate> = Vec::new();
    for line in input.lines() {
        if line.contains("->") {
            match line.split_whitespace().collect::<Vec<&str>>().as_slice() {
                [input1, operator, input2, "->", output] => {
                    let operator = match *operator {
                        "AND" => Operator::And,
                        "OR" => Operator::Or,
                        "XOR" => Operator::Xor,
                        _ => panic!("Invalid operator"),
                    };
                    gates.push(Gate {
                        inputs: vec![input1.to_string(), input2.to_string()],
                        output: output.to_string(),
                        operator
                    });
                },
                _ => panic!("Invalid input"),
            }
        }
    }
    let mut bad_gates: HashSet<String> = HashSet::new();
    // println!("{:?}", gates);
    for gate in gates.iter() {
        let input1 = &gate.inputs[0];
        let input2 = &gate.inputs[1];
        if gate.output.chars().next().unwrap() == 'z' && !(gate.output == "z45" || gate.operator == Operator::Xor) {
            bad_gates.insert(gate.output.to_string());
        } else if gate.operator == Operator::Xor && !(input1.chars().next().unwrap() == 'x' || input2.chars().next().unwrap() == 'x' || gate.output.chars().next().unwrap() == 'z') {
            bad_gates.insert(gate.output.to_string());
        } else if gate.operator == Operator::And && input1.as_str() != "x00" && input2.as_str() != "x00" {
            for subgate in gates.iter() {
                if subgate.inputs.contains(&gate.output) && subgate.operator != Operator::Or {
                    bad_gates.insert(gate.output.to_string());
                }
            }
        } else if gate.operator == Operator::Xor {
            for subgate in gates.iter() {
                if subgate.inputs.
                    contains(&gate.output) && subgate.operator == Operator::Or {
                    bad_gates.insert(gate.output.to_string());
                }
            }
        }
    }
    let mut bad_gates: Vec<String> = bad_gates.into_iter().collect();
    bad_gates.sort();
    return bad_gates.join(",");
}
