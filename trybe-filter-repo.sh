#!/bin/bash

### GIT FILTER-REPO ###

## NÃO EXECUTE ESSE SCRIPT DIRETAMENTE
## Esse script foi feito para uso do
## script 'trybe-publisher' fornecido 
## pela Trybe.

[[ $# == 1 ]] && \
[[ $1 == "trybe-security-parameter" ]] && \
git filter-repo \
    --path .trybe \
    --path .github \
    --path trybe.yml \
    --path README.md \
    --path trybe-filter-repo.sh \
    --path tests/trybe \
    --path tests/actions/test_deepest_file.py \
    --path tests/actions/test_find_file_by_name.py \
    --path tests/actions/test_find_file_by_name.py \
    --invert-paths --force --quiet
