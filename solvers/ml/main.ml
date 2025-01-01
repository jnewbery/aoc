let test_content_201901_1 = [%blob "inputs/test/201901_1.txt"]
let test_content_201901_2 = [%blob "inputs/test/201901_2.txt"]
let full_content_201901 = [%blob "inputs/full/201901.txt"]

let () =
  let args = Array.to_list Sys.argv in
  let year = List.nth args 1 in
  let day = List.nth args 2 in
  let part = List.nth args 3 in
  let file_content =
    if List.exists ((=) "-t") args then
      if part = "1" then
        test_content_201901_1
      else
        test_content_201901_2
    else
      full_content_201901
  in
  let solver_name = Printf.sprintf "%s%s_%s" year day part in
  match solver_name with
  | "201901_1" -> Solver_201901_1.solve file_content
  | "201901_2" -> Solver_201901_2.solve file_content
  | _ -> Printf.eprintf "Unknown solver: %s\n" solver_name
