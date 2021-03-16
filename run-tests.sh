#!/bin/sh

tmp=`mktemp`

echo "Running predefined tests"

for d in `ls testdata`; do
    echo "Test $d"
    echo "Input:"
    cat testdata/$d/input.txt
    echo
    cat testdata/$d/input.txt | docker run -i --rm edge-detector > $tmp
    echo "Output:"
    cat $tmp
    if git diff -w --no-prefix --word-diff=color $tmp testdata/$d/expected-output.txt; then
        echo "OK"
    else
        echo "Failed"
        exit 1
    fi
    echo
done

echo "All tests finished"