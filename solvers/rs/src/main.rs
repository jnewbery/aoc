use clap::{ArgAction,Parser};
use std::collections::HashMap;
use std::time::Instant;
use serde_json::json;

pub mod solver_201501_1;
pub mod solver_201501_2;
pub mod solver_202401_1;
pub mod solver_202401_2;
pub mod solver_202402_1;
pub mod solver_202402_2;
pub mod solver_202403_1;
pub mod solver_202403_2;
pub mod solver_202404_1;
pub mod solver_202404_2;
pub mod solver_202405_1;
pub mod solver_202405_2;
pub mod solver_202406_1;
pub mod solver_202406_2;
pub mod solver_202407_1;
pub mod solver_202407_2;
pub mod solver_202408_1;
pub mod solver_202408_2;
pub mod solver_202409_1;
pub mod solver_202409_2;
pub mod solver_202410_1;
pub mod solver_202410_2;
pub mod solver_202411_1;
pub mod solver_202411_2;
pub mod solver_202412_1;
pub mod solver_202412_2;
pub mod solver_202413_1;
pub mod solver_202413_2;
pub mod solver_202414_1;
pub mod solver_202414_2;
pub mod solver_202415_1;
pub mod solver_202415_2;
pub mod solver_202416_1;
pub mod solver_202416_2;
pub mod solver_202417_1;
pub mod solver_202417_2;
pub mod solver_202418_1;
pub mod solver_202418_2;
pub mod solver_202419_1;
pub mod solver_202419_2;
pub mod solver_202420_1;
pub mod solver_202420_2;
pub mod solver_202421_1;

use crate::solver_201501_1::solve_201501_1;
use crate::solver_201501_2::solve_201501_2;
use crate::solver_202401_1::solve_202401_1;
use crate::solver_202401_2::solve_202401_2;
use crate::solver_202402_1::solve_202402_1;
use crate::solver_202402_2::solve_202402_2;
use crate::solver_202403_1::solve_202403_1;
use crate::solver_202403_2::solve_202403_2;
use crate::solver_202404_1::solve_202404_1;
use crate::solver_202404_2::solve_202404_2;
use crate::solver_202405_1::solve_202405_1;
use crate::solver_202405_2::solve_202405_2;
use crate::solver_202406_1::solve_202406_1;
use crate::solver_202406_2::solve_202406_2;
use crate::solver_202407_1::solve_202407_1;
use crate::solver_202407_2::solve_202407_2;
use crate::solver_202408_1::solve_202408_1;
use crate::solver_202408_2::solve_202408_2;
use crate::solver_202409_1::solve_202409_1;
use crate::solver_202409_2::solve_202409_2;
use crate::solver_202410_1::solve_202410_1;
use crate::solver_202410_2::solve_202410_2;
use crate::solver_202411_1::solve_202411_1;
use crate::solver_202411_2::solve_202411_2;
use crate::solver_202412_1::solve_202412_1;
use crate::solver_202412_2::solve_202412_2;
use crate::solver_202413_1::solve_202413_1;
use crate::solver_202413_2::solve_202413_2;
use crate::solver_202414_1::solve_202414_1;
use crate::solver_202414_2::solve_202414_2;
use crate::solver_202415_1::solve_202415_1;
use crate::solver_202415_2::solve_202415_2;
use crate::solver_202416_1::solve_202416_1;
use crate::solver_202416_2::solve_202416_2;
use crate::solver_202417_1::solve_202417_1;
use crate::solver_202417_2::solve_202417_2;
use crate::solver_202418_1::solve_202418_1;
use crate::solver_202418_2::solve_202418_2;
use crate::solver_202419_1::solve_202419_1;
use crate::solver_202419_2::solve_202419_2;
use crate::solver_202420_1::solve_202420_1;
use crate::solver_202420_2::solve_202420_2;
use crate::solver_202421_1::solve_202421_1;

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
    verbose: bool,
}

fn get_functions() -> HashMap<std::string::String, fn() -> std::string::String> {
    let mut functions: HashMap<std::string::String, fn() -> std::string::String> = HashMap::new();
    functions.insert("201501_1".to_string(), solve_201501_1);
    functions.insert("201501_2".to_string(), solve_201501_2);
    functions.insert("202401_1".to_string(), solve_202401_1);
    functions.insert("202401_2".to_string(), solve_202401_2);
    functions.insert("202402_1".to_string(), solve_202402_1);
    functions.insert("202402_2".to_string(), solve_202402_2);
    functions.insert("202403_1".to_string(), solve_202403_1);
    functions.insert("202403_2".to_string(), solve_202403_2);
    functions.insert("202404_1".to_string(), solve_202404_1);
    functions.insert("202404_2".to_string(), solve_202404_2);
    functions.insert("202405_1".to_string(), solve_202405_1);
    functions.insert("202405_2".to_string(), solve_202405_2);
    functions.insert("202406_1".to_string(), solve_202406_1);
    functions.insert("202406_2".to_string(), solve_202406_2);
    functions.insert("202407_1".to_string(), solve_202407_1);
    functions.insert("202407_2".to_string(), solve_202407_2);
    functions.insert("202408_1".to_string(), solve_202408_1);
    functions.insert("202408_2".to_string(), solve_202408_2);
    functions.insert("202409_1".to_string(), solve_202409_1);
    functions.insert("202409_2".to_string(), solve_202409_2);
    functions.insert("202410_1".to_string(), solve_202410_1);
    functions.insert("202410_2".to_string(), solve_202410_2);
    functions.insert("202411_1".to_string(), solve_202411_1);
    functions.insert("202411_2".to_string(), solve_202411_2);
    functions.insert("202412_1".to_string(), solve_202412_1);
    functions.insert("202412_2".to_string(), solve_202412_2);
    functions.insert("202413_1".to_string(), solve_202413_1);
    functions.insert("202413_2".to_string(), solve_202413_2);
    functions.insert("202414_1".to_string(), solve_202414_1);
    functions.insert("202414_2".to_string(), solve_202414_2);
    functions.insert("202415_1".to_string(), solve_202415_1);
    functions.insert("202415_2".to_string(), solve_202415_2);
    functions.insert("202416_1".to_string(), solve_202416_1);
    functions.insert("202416_2".to_string(), solve_202416_2);
    functions.insert("202417_1".to_string(), solve_202417_1);
    functions.insert("202417_2".to_string(), solve_202417_2);
    functions.insert("202418_1".to_string(), solve_202418_1);
    functions.insert("202418_2".to_string(), solve_202418_2);
    functions.insert("202419_1".to_string(), solve_202419_1);
    functions.insert("202419_2".to_string(), solve_202419_2);
    functions.insert("202420_1".to_string(), solve_202420_1);
    functions.insert("202420_2".to_string(), solve_202420_2);
    functions.insert("202421_1".to_string(), solve_202421_1);
    functions
}

fn main() {
    let args = Args::parse();

    let functions = get_functions();

    let verbose = args.verbose;

    if let Some(year) = args.year {
        if let Some(day) = args.day {
            if let Some(part) = args.part {
                let key = format!("{:04}{:02}_{}", year, day, part);
                if let Some(func) = functions.get(&key) {
                    let start = Instant::now();
                    let solution: String = func();
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
                    // println!("No function found for key: {}", key);
                }
            }
        }
    }
}
