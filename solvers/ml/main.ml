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
  match puzzle with
  | "2019011" -> Solver_2019011.solve file_content
  | "2019012" -> Solver_2019012.solve file_content
  | _ -> Printf.eprintf "Unknown solver: %s\n" puzzle
