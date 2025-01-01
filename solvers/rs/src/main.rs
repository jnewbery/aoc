pub mod solvers;

use clap::{ArgAction,Parser};
use serde_json::json;
use std::fs;
use std::time::Instant;
use std::path::Path;
use solvers::get_functions;

#[derive(Parser, Debug)]
#[command(name = "AoC solver")]
#[command(about = "Solve an advent of code puzzle", long_about = None)]
struct Args {
    #[arg(short, long)]
    year: Option<u32>,
    #[arg(short, long)]
    day: Option<u32>,
    #[arg(short, long)]
    part: Option<u32>,
    #[arg(short, long, action = ArgAction::SetTrue)]
    test: bool,
    #[arg(short, long, action = ArgAction::SetTrue)]
    verbose: bool,
}

fn main() {
    let args = Args::parse();

    let functions = get_functions();

    let verbose = args.verbose;

    let year = args.year.expect("Year is required");
    let day = args.day.expect("Day is required");
    let part = args.part.expect("Part is required");
    let key = format!("{:04}{:02}_{}", year, day, part);
    if let Some(func) = functions.get(&key) {
        let input_file = if args.test {
            if Path::new(&format!("../../inputs/test/{:04}{:02}_{}.txt", year, day, part)).exists() {
                format!("../../inputs/test/{:04}{:02}_{}.txt", year, day, part)
            } else {
                format!("../../inputs/test/{:04}{:02}.txt", year, day)
            }
        } else {
            format!("../../inputs/full/{:04}{:02}.txt", year, day)
        };
        let input_string = fs::read_to_string(input_file).expect("Could not read input file");

        let start = Instant::now();
        let solution: String = func(&input_string);
        let execution_time = start.elapsed();
        let result = json!({
            "solution": solution,
            "execution_time": execution_time.as_micros(),
        });

        if verbose {
            println!("{}", serde_json::to_string_pretty(&result).unwrap());
        } else {
            println!("{}", solution);
        }
    } else {
        std::process::exit(38);
    }
}
