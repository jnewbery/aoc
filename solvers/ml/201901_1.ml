#load "unix.cma"

let read_integers_from_file filename =
  let input_channel = open_in filename in
  (* Read the entire file into a string *)
  let content = really_input_string input_channel (in_channel_length input_channel) in
  close_in input_channel;
  (* Split on newlines to get a list of strings *)
  let string_list = 
    content 
    |> String.split_on_char '\n'  (* Split by newlines first *)
  in
  (* Filter out empty strings and convert to integers *)
  string_list
  |> List.filter (fun s -> String.trim s <> "")  (* Remove empty strings *)
  |> List.map int_of_string  (* Convert to integers *)

let () =
  let args = Array.to_list Sys.argv in
  let file_path =
    if List.exists ((=) "-t") args then
      "../../inputs/test/201901_1.txt"
    else
      "../../inputs/full/201901_1.txt"
  in
  let start_time = Unix.gettimeofday () in
  let integers = read_integers_from_file file_path in
  let fuel = List.fold_left (fun acc mass -> acc + (mass / 3) - 2) 0 integers in
  let end_time = Unix.gettimeofday () in
  let execution_time = (end_time -. start_time) *. 1_000_000.0 in (* Convert to microseconds *)
  Printf.printf "{\"solution\": \"%d\", \"execution_time\": %.0f}\n" fuel execution_time
