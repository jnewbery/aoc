fn get_combo_operand(operand: u64, reg_a: &u64, reg_b: &u64, reg_c: &u64) -> u64 {
    match operand {
        0 | 1 | 2 | 3 => operand,
        4 => *reg_a,
        5 => *reg_b,
        6 => *reg_c,
        _ => panic!("Invalid operand: {}", operand),
    }
}

fn run_program(program: &Vec<u64>, mut reg_a: u64, mut reg_b: u64, mut reg_c: u64) -> Vec<u64> {
    let mut output = Vec::new();
    let mut instruction_pointer = 0;

    loop {
        if instruction_pointer >= program.len() {
            break;
        }
        let opcode = program[instruction_pointer];
        let operand = program[instruction_pointer + 1];
        // println!("P {:2}, Inst: {}|{}, reg: ({:8},{:8},{:8}), Output: {:?}", instruction_pointer, opcode, operand, reg_a, reg_b, reg_c, output);
        match opcode {
            0 => {
                reg_a = reg_a / (2 as u64).pow(get_combo_operand(operand, &reg_a, &reg_b, &reg_c) as u32);
            },
            1 => {
                reg_b ^= operand;
            },
            2 => {
                reg_b = get_combo_operand(operand, &reg_a, &reg_b, &reg_c) % 8;
            },
            3 => {
                if reg_a != 0 {
                    instruction_pointer = operand as usize;
                    continue;
                }
            },
            4 => {
                reg_b = reg_b ^ reg_c;
            },
            5 => {
                output.push(get_combo_operand(operand, &reg_a, &reg_b, &reg_c) % 8);
            },
            6 => {
                reg_b = reg_a / (2 as u64).pow(get_combo_operand(operand, &reg_a, &reg_b, &reg_c) as u32);
            },
            7 => {
                reg_c = reg_a / (2 as u64).pow(get_combo_operand(operand, &reg_a, &reg_b, &reg_c) as u32);
            },
            _ => panic!("Invalid opcode: {}", opcode),
        }
        instruction_pointer += 2;
    }
    output
}

pub fn solve(input: &str) -> String {
    let mut lines = input.lines();

    // registers
    lines.next();  // skip reg_a
    let reg_b = lines.next().unwrap().chars().filter(|c| c.is_digit(10)).collect::<String>().parse::<u64>().unwrap();
    let reg_c = lines.next().unwrap().chars().filter(|c| c.is_digit(10)).collect::<String>().parse::<u64>().unwrap();

    // empty line
    lines.next();

    // program
    let program = lines.next().unwrap().split(|c: char| !c.is_numeric()).filter_map(|s| s.parse::<u64>().ok()).collect::<Vec<u64>>();

    let mut reg_a = (8 as u64).pow(program.len() as u32 - 1);
    // println!("({:?},{:?},{:?}), {:?}", reg_a, reg_b, reg_c, program);

    loop {
        // println!("({:?},{:?},{:?})", reg_a, reg_b, reg_c);
        let output = run_program(&program, reg_a, reg_b, reg_c);
        // println!("{:16}: {:?}", reg_a, output);
        // println!("program         : {:?}", program);
        if output.len() > program.len() {
            panic!("Output too long: {:?}", output);
        }
        if output == program {
            // println!("{}", reg_a);
            return reg_a.to_string();
        }
        for i in 0..program.len() {
            let output_byte = output[output.len() - i - 1 as usize];
            // println!("{:2}: {:2} {:2}", i, output_byte, program[program.len() - i - 1 as usize]);
            if output_byte != program[program.len() - 1 - i as usize] {
                let increase = (8 as u64).pow(program.len() as u32 - i as u32 - 1);
                // println!("{:2}!={:2}. Increasing by {}\n", output_byte, program[program.len() - i - 1 as usize], increase);
                reg_a += increase;
                break;
            }
        }
    }
}
