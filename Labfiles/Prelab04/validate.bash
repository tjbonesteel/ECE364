#!/bin/bash


regex1=^[A-Z][a-z]*$
regex2=^[a-z]+$
regex3=^[A-Za-z]+$
regex4=^[0-9a-zA-Z]+$

IFS=$'\n_'
filename=$(<$@)

for t in $filename
do 
    

    if [[ $t =~ $regex1 ]]
    then
        echo \"$t\" is capitalized.
        
    elif [[ $t =~ $regex2 ]]
    then
        echo \"$t\" is lower case.
    elif [[ $t =~ $regex3 ]]
    then
	echo \"$t\" is mixed case.
    elif [[ $t =~ $regex4 ]]
    then
	echo \"$t\" is alphanumeric.
    else
	echo \"$t\" is weird.
    fi
done
