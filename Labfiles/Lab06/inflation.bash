#! /bin/bash
#
# $Author: ee364d02 $
# $Date: 2013-09-25 15:16:31 -0400 (Wed, 25 Sep 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Lab06/inflation.bash $
# $Revision: 59899 $

if (( $numArg < 2 ))
then
    echo "Usage: inflation.bash <grade_file> <school1> <school2>"
    exit 1
fi

if [[ ! -r $arg1 ]]
then
    echo "error: $arg1 is not a readable file."
    exit 2
fi
