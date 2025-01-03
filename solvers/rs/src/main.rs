pub mod solvers;

use clap::{ArgAction,Parser};
use serde_json::json;
use std::time::Instant;
use solvers::{get_functions, get_input};

#[derive(Parser, Debug)]
#[command(name = "AoC solver")]
#[command(about = "Solve an advent of code puzzle", long_about = None)]
struct Args {
    puzzle: Option<u32>,

    /// Run solver on test input. Defaults to false.
    #[arg(short, long, action = ArgAction::SetTrue)]
    test: bool,

    /// Print solution and execution information as JSON. Defaults to false.
    #[arg(short, long, action = ArgAction::SetTrue)]
    verbose: bool,
}

fn main() {
    let args = Args::parse();

    let puzzle = args.puzzle.expect("Puzzle number <YYYYDDP> is required").to_string();

    let functions = get_functions();
    let func = functions.get(&puzzle).unwrap_or_else(|| {
        eprintln!("Could not find function for puzzle: {}", puzzle);
        std::process::exit(38);
    });

    let all_inputs = get_input();
    let inputs = all_inputs.get(&args.test).expect("Could not get inputs");
    let input_string = inputs.get(&puzzle).expect("Could not get input");

    let start = Instant::now();
    let solution: String = func(&input_string);
    let execution_time = start.elapsed();
    let result = json!({
        "solution": solution,
        "execution_time": execution_time.as_micros(),
    });

    if args.verbose {
        println!("{}", serde_json::to_string_pretty(&result).unwrap());
    } else {
        println!("{}", solution);
    }
}
