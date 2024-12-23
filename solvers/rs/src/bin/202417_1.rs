static TEST: bool = false;

static _TEST_INPUT: &str = include_str!("../../../../inputs/test/202417.txt");
static _INPUT: &str = include_str!("../../../../inputs/full/202417.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

fn get_combo_operand(operand: u32, reg_a: &u32, reg_b: &u32, reg_c: &u32) -> u32 {
    match operand {
        0 | 1 | 2 | 3 => operand,
        4 => *reg_a,
        5 => *reg_b,
        6 => *reg_c,
        _ => panic!("Invalid operand: {}", operand),
    }
}

fn run_program(program: &Vec<u32>, mut reg_a: u32, mut reg_b: u32, mut reg_c: u32) -> Vec<u32> {
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
                // let combo_operand = get_combo_operand(operand, reg_a, reg_b, reg_c);
                reg_a = reg_a / (2 as u32).pow(get_combo_operand(operand, &reg_a, &reg_b, &reg_c));
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
                reg_b = reg_a / (2 as u32).pow(get_combo_operand(operand, &reg_a, &reg_b, &reg_c));
            },
            7 => {
                reg_c = reg_a / (2 as u32).pow(get_combo_operand(operand, &reg_a, &reg_b, &reg_c));
            },
            _ => panic!("Invalid opcode: {}", opcode),
        }
        instruction_pointer += 2;
    }
    output
}

fn main() {
    let mut lines = INPUT.lines();

    // registers
    let reg_a = lines.next().unwrap().chars().filter(|c| c.is_digit(10)).collect::<String>().parse::<u32>().unwrap();
    let reg_b = lines.next().unwrap().chars().filter(|c| c.is_digit(10)).collect::<String>().parse::<u32>().unwrap();
    let reg_c = lines.next().unwrap().chars().filter(|c| c.is_digit(10)).collect::<String>().parse::<u32>().unwrap();

    // empty line
    lines.next();

    // program
    let program = lines.next().unwrap().split(|c: char| !c.is_numeric()).filter_map(|s| s.parse::<u32>().ok()).collect::<Vec<u32>>();
    // println!("{:?}, {:?}, {:?}, {:?}", reg_a, reg_b, reg_c, program);

    let output = run_program(&program, reg_a, reg_b, reg_c);
    // println!("{:?}, {:?}, {:?}, {:?}", reg_a, reg_b, reg_c, output);

    let sol = output
        .iter()
        .map(|n| n.to_string())
        .collect::<Vec<String>>()
        .join(",");

    println!("{}", sol);
}
