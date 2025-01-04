### Configuration files

- `cookie.txt` contains the session cookie for the Advent of Code website. This
  is used to download inputs.
- `manifest.toml` contains the solver implementations to run. This is used by
  the `run.py` script. Each section is a year, and individual lines are days, eg:

  ```toml
  [2019]
  1 = "rs"
  2 = "py"
  3 = "ml"
  ```
