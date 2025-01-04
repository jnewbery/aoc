Ocaml solvers for advent of code puzzles.

## Building

To build the solutions, run:

```sh
just build
```

(or `just`).

### Requirements

- [Ocaml](https://ocaml.org/), [Opam](https://opam.ocaml.org/) and [Dune](https://dune.build/)
  - `brew install ocaml opam dune` on macOS
  - opam must be initialized:
    ```sh
    opam init
    eval $(opam env)
    ```
- [`ppx_blob`](https://opam.ocaml.org/packages/ppx_blob/)
  - `opam install ppx_blob`
- [Just](https://github.com/casey/just)
  - `brew install just` on macOS

Cargo will install other dependencies as needed.

## Execution

To run a solver for a particular day, run:

```sh
just run <YYYYDDP>
```

To see all options, pass `-h` as an argument:

```sh
just run -h
```
