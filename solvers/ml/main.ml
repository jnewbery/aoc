let test_content_201901_1 = [%blob "inputs/test/201901_1.txt"]
let test_content_201901_2 = [%blob "inputs/test/201901_2.txt"]
let full_content_201901 = [%blob "inputs/full/201901.txt"]

let () =
  let args = Array.to_list Sys.argv in
  let puzzle = List.nth args 1 in
  let file_content =
    if List.exists ((=) "-t") args then
      if String.get puzzle 6 = '1' then
        test_content_201901_1
      else
        test_content_201901_2
    else
      full_content_201901
  in

  let time_solve solver input =
    let start_time = Unix.gettimeofday () in
    let solution = solver input in
    let end_time = Unix.gettimeofday () in
    let execution_time = (end_time -. start_time) *. 1_000_000.0 in (* Convert to microseconds *)
    (solution, execution_time)
  in

  let print_result result duration json_output =
    if json_output then
      Printf.printf "{\"solution\": \"%s\", \"execution_time\": %.2f}\n" result duration
    else
      Printf.printf "%s\n" result
  in

  let json_output = List.exists ((=) "-v") args in
  match puzzle with
  | "2019011" -> 
      let (result, duration) = time_solve Solver_2019011.solve file_content in
      print_result result duration json_output
  | "2019012" -> 
      let (result, duration) = time_solve Solver_2019012.solve file_content in
      print_result result duration json_output
  | _ -> Printf.eprintf "Unknown solver: %s\n" puzzle
