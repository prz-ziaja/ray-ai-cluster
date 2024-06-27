# /bin/bash

APP_ROOT="$( dirname "${BASH_SOURCE[0]}" )"
echo $APP_ROOT

for i in $(ls $APP_ROOT | grep requirements\.txt | cut -d"-" -f1)
do 
    echo conda create -n $i python=3.11
    echo conda activate $i 
    echo conda install --file $APP_ROOT/$i-requirements.txt
done