#! /bin/bash
#
# $Author: ee364d02 $
# $Date: 2013-09-11 12:32:13 -0400 (Wed, 11 Sep 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab04/wgrep.bash $
# $Revision: 58580 $
IFS=':'
set $(egrep -n $1 $2)
lineNum=$1


let min=$lineNum-1
let max=$lineNum+1

echo $(tail -n +${min} data | head -n 3)
exit 0
