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

let solve content =
  let integers = read_integers_from_file content in
  let result = List.fold_left (fun acc mass -> acc + (mass / 3) - 2) 0 integers in
  string_of_int result