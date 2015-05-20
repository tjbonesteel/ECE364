#! /bin/bash
#
# $Author: ee364d02 $
# $Date: 2013-09-04 14:04:52 -0400 (Wed, 04 Sep 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Lab03/analysis.bash $
# $Revision: 57895 $

if (( $#!=1 ))
then
    echo "Usage: analysis.bash <input file>"
    exit 1
fi


if  [[ ! -r $@ ]]
then
    echo "Error: $@ is not a readable file."
    exit 2
fi

readarray Data < benchmarks.txt
echo ${#Data[*]}




#for ((i = 2; i < (${#Ops[@]}-1); i++ ))
#do
#    let sum+=${Ops[i]}
#
#done
#let i=$i-2
#let Ops_AVG=sum/i
#echo $Ops_AVG




