# /bin/bash

APP_ROOT="$( dirname "${BASH_SOURCE[0]}" )"

for i in $(ls $APP_ROOT | grep environment\.yml)
do 
    conda env create -f $APP_ROOT/$i
done