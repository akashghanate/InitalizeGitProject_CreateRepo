#!/bin/bash

# create function for the shell command
function create(){
    source .env
    python create.py $1
    cd $path$1
    git init
    git remote add origin https://github.com/$username/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master   
}
