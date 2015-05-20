#! /bin/bash
#
# $Author: ee364d02 $
# $Date: 2013-09-11 12:32:13 -0400 (Wed, 11 Sep 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab04/wgrep.bash $
# $Revision: 58580 $

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

IFS=',;'
