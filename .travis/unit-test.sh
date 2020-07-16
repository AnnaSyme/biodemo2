#!/bin/bash

set -e
errors=0

# Run unit tests
python biodemo2/biodemo2_test.py || {
    echo "'python python/biodemo2/biodemo2_test.py' failed"
    let errors+=1
}

# Check program style
pylint -E biodemo2/*.py || {
    echo 'pylint -E biodemo2/*.py failed'
    let errors+=1
}

[ "$errors" -gt 0 ] && {
    echo "There were $errors errors found"
    exit 1
}

echo "Ok : Python specific tests"
