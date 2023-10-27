#!/usr/bin/env bash
find . -name "results.txt" -exec rm {} \;
for f in *.py; do
    python -m timeit -n 100 "$(cat $f)" > $f.result;
    echo $f - "$(tail -n 1 $f.result)" >> results.txt;
    rm $f.result
done
cat results.txt