#! /bin/bash
#
# $Author: ee364d02 $
# $Date: 2013-09-11 14:42:25 -0400 (Wed, 11 Sep 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Lab04/interest.bash $
# $Revision: 58630 $

if (( $#!=1 ))
then
    echo "Usage: interest.bash <bank_statement.csv>"
    exit 1
fi


if  [[ ! -r $@ ]]
then
    echo "Error: $@ is not a readable file."
    exit 2
fi


sum=0



while read -a data
do
for t in $data
do
    IFS=','
    if [[ $t =~ "INTEREST" ]]
    then
	num=${data[5]%%.*}
	echo Interest for the month ${data[1]} is $num
	((sum=$num+$sum))
	year=${data[1]##*/}
    fi
done
  

done < $@


echo Interest for $year is $sum
exit 0
