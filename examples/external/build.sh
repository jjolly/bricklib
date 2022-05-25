#!/bin/bash

if ! which cmake > /dev/null; then
  if which spack > /dev/null; then
    spack load cmake || exit 1
  else
    echo cmake not found
    exit 1
  fi
fi

mkdir build || exit 1
cd build
cmake .. || exit 1
cmake --build . || exit 1
./example || exit 1
