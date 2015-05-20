#! /bin/bash
#
# $Author: ee364d02 $
# $Date: 2013-09-04 14:04:52 -0400 (Wed, 04 Sep 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Lab03/sorting.bash $
# $Revision: 57895 $

if (( $#!=1 ))
then
    echo "Usage: sorting.bash <input file>"
    exit 1
fi

if  [[ ! -r $@ ]]
then
    echo "Error: $@ is not a readable file."
    exit 2
fi


echo "Your choices are:"
echo "1) First 10 People"
echo "2) Last 5 names by highest zipcodes"
echo "3) Address of 6th-10th by revers e-mail"
echo "4) First 12 companies"
echo "5) Pick number of People"
echo "6) Exit"
read -a choice
echo "Your Choice: ${choice[0]}"

if (( ${choice[0]} = 5 ))
then
    echo "How many people would you like to view? "
    read -a numPeople
    
    cut -d',' -
