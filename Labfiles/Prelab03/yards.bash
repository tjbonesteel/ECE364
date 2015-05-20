#! /bin/bash
#
# $Author: ee364d02 $
# $Date: 2013-09-04 12:26:53 -0400 (Wed, 04 Sep 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab03/yards.bash $
# $Revision: 57860 $


if (( $#!=1 ))
then
    echo "Usage: yards.bash <filename>"
    exit 1
fi


if  [[ ! -r $@ ]]
then
    echo "Error: $@ is not a readable file."
    exit 2
fi   

 
sum=0
var=0
best=0
conf=$(sed -n '1p' $@)
ACC=($conf)

for ((i = 1; i < ${#ACC[@]}; i++ ))
do
    let sum+=${ACC[i]}
    
    (( var += (1/${#ACC[@]}) * (${ACC[i]} - $sum)**2 ))

done
i=$i-1
let avg=sum/i
echo "ACC Schools averaged $avg yards receiving with a variance of $var"




if (($avg > $best ))
then
    best=$avg
fi


conf=$(sed -n '2p' $@)
Big10=($conf)
sum=0
var=0



for ((i = 1; i < ${#Big10[@]}; i++ ))
do
    let sum+=${Big10[i]}
    
    (( var += (1/${#Big10[@]}) * (${Big10[i]} - $sum)**2 ))

done
i=$i-1
let avg=sum/i
echo "Big10 Schools averaged $avg yards receiving with a variance of $var"

if (($avg > $best ))
then
    best=$avg
fi

conf=$(sed -n '3p' $@)
Big12=($conf)
sum=0
var=0



for ((i = 1; i < ${#Big12[@]}; i++ ))
do
    let sum+=${Big12[i]}
    
    (( var += (1/${#Big12[@]}) * (${Big12[i]} - $sum)**2 ))

done
i=$i-1
let avg=sum/i
echo "Big12 Schools averaged $avg yards receiving with a variance of $var"

if (($avg > $best ))
then
    best=$avg
fi

conf=$(sed -n '4p' $@)
BigEast=($conf)
sum=0
var=0



for ((i = 1; i < ${#BigEast[@]}; i++ ))
do
    let sum+=${BigEast[i]}
    
    (( var += (1/${#BigEast[@]}) * (${BigEast[i]} - $sum)**2 ))

done
i=$i-1
let avg=sum/i
echo "BigEast Schools averaged $avg yards receiving with a variance of $var"

if (($avg > $best ))
then
    best=$avg
fi



conf=$(sed -n '5p' $@)
Pac10=($conf)
sum=0
var=0



for ((i = 1; i < ${#Pac10[@]}; i++ ))
do
    let sum+=${Pac10[i]}
    
    (( var += (1/${#Pac10[@]}) * (${Pac10[i]} - $sum)**2 ))

done
i=$i-1
let avg=sum/i
echo "Pac10 Schools averaged $avg yards receiving with a variance of $var"
if (($avg > $best ))
then
    best=$avg
fi



conf=$(sed -n '6p' $@)
SEC=($conf)
sum=0
var=0



for ((i = 1; i < ${#SEC[@]}; i++ ))
do
    let sum+=${SEC[i]}
    
    (( var += (1/${#SEC[@]}) * (${SEC[i]} - $sum)**2 ))

done
i=$i-1
let avg=sum/i
echo "SEC Schools averaged $avg yards receiving with a variance of $var"
if (($avg > $best ))
then
    best=$avg
fi

echo "The largest average yardage was $best"
