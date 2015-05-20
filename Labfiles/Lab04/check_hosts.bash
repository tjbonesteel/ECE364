#! /bin/bash
#
# $Author: ee364d02 $
# $Date: 2013-09-11 15:17:49 -0400 (Wed, 11 Sep 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Lab04/check_hosts.bash $
# $Revision: 58653 $

if (( $#!=1 ))
then
    echo "Usage: check_hosts.bash <hostfile>"
    exit 1
fi


if  [[ ! -r $@ ]]
then
    echo "Error: $@ is not a readable file."
    exit 2
fi

lineNum=1
regex1=([0-2]*[0-9]*[0-9]\.){3}[0-2]*[0-9]*[0-9]

IFS=';,'

while read -a data
do

for t in $data
do
    
    if [[ ${data[0]} != regex1 ]]
    then
	echo ${data[0]}
	echo Line $lineNum: bad IP Address
    fi
    ((lineNum=$lineNum+1))
done

done < $@
