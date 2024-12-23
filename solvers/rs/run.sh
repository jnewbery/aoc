#!/bin/bash

cargo build --release
for f in target/release/20*; do
  if [ -x $f ]; then
    echo $f;
    $f;
  fi;
done
