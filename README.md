### Advent of Code

Solvers for [Advent of Code](https://adventofcode.com/) puzzles.

#### Files

- `inputs/` contains test and full inputs for each day. Full inputs are
  gitexcluded, so you'll need to download them using the `get_inputs.py`
  script.
- `solvers/` contains solvers for each day. Different languages have their
  own subdirectories.
- `solutions/` contains solutions for my inputs. Users have different inputs
  and solutions, so don't copy them. You can use the `add_sultion.py` script
  to add your own solutions.
- `/.config` contains configuration files.

#### Execution

To run the solvers, run:

```sh
uv run run_solvers.py YYYYDDP [-i <implementation>] [-t]
```

Where `YYYYDDP` is the puzzle identifier. Any prefix is acceptable, eg
`./run.py 2019` will run all 2019 puzzles, and `./run.py 201901` will run
both parts of day 1 of 2019. The `-i` flag can be used to specify the
implementation to run, and the `-t` flag can be used to run the tests.

To print previously saved results from `results/*.json`, run:

```sh
uv run print_results.py YYYYDDP [-t] [-f <table|grid>]
```
