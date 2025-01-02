let read_integers_from_file content =
  (* Split on newlines to get a list of strings *)
  let string_list = 
    content 
    |> String.split_on_char '\n'  (* Split by newlines first *)
  in
  (* Filter out empty strings and convert to integers *)
  string_list
  |> List.filter (fun s -> String.trim s <> "")  (* Remove empty strings *)
  |> List.map int_of_string  (* Convert to integers *)

let repeatedly_apply_and_sum op pred x =
  let rec aux acc current first_call =
    if pred current then acc
    else aux (if first_call then acc else acc + current) (op current) false
  in
  aux 0 x true

let sum_transformed_list lst op pred =
  lst
  |> List.map (repeatedly_apply_and_sum op pred)
  |> List.fold_left (+) 0

let solve content =
  let start_time = Unix.gettimeofday () in
  let integers = read_integers_from_file content in
  let fuel = sum_transformed_list integers (fun x -> x / 3 - 2) ((>=) 0) in
  let end_time = Unix.gettimeofday () in
  let execution_time = (end_time -. start_time) *. 1_000_000.0 in (* Convert to microseconds *)
  Printf.printf "{\"solution\": \"%d\", \"execution_time\": %.0f}\n" fuel execution_time
