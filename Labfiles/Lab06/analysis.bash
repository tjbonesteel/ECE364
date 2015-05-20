#! /bin/bash
#
# $Author: ee364d02 $
# $Date: 2013-09-25 15:24:53 -0400 (Wed, 25 Sep 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Lab06/analysis.bash $
# $Revision: 59922 $

arg1=$1
arg2=${2}
numArg=$#
zone1=0
zone2=0
zone3=0
zone4=0
zone5=0

if (( $numArg != 2 ))
then
    echo "Usage: ./analysis.bash <input_file> <charity_flag>"
    exit 1
fi

if [[ ! -r $arg1 ]]
then
    echo "error: $arg1 is not a readable file."
    exit 2
fi
IFS=","
while read -a data
do
   
    dataPoint=${data[($arg2+1)]}

    point=${dataPoint}
    
    if (( $point > 0 && $point < 20 ))
    then
	let zone1=zone1+1
    fi
if (( $point >= 20 && $point < 40 ))
    then
	let zone2=zone2+1
    fi

if (( $point >= 40 && $point < 60 ))
    then
	let zone3=zone3+1
    fi
if (( $point >= 60 && $point < 80 ))
    then
	let zone4=zone4+1
    fi
if (( $point >= 80 && $point < 100 ))
    then
	let zone5=zone5+1
    fi
done < $arg1
echo -e "0-19: $zone1\n20-39: $zone2\n40-59: $zone3\n60-79: $zone4\n80-100: $zone5" > histogram.txt

exit 0

