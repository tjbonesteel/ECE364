#! /bin/bash
#
# $Author: ee364d02 $
# $Date: 2013-08-28 15:18:00 -0400 (Wed, 28 Aug 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Lab02/finalize_grades.bash $
# $Revision: 57461 $
file="$@.finalized"
numStudents='wc -l $@'

if (( $#!=1 ))
then
    echo "Usage: assign_grades.bash <roster file>"
    exit 1
fi


if  [[ ! -r $@ ]]
then
    echo "Error: $@ is not a readable file."
    exit 2
fi

if [[  -e $file ]]
then
    echo "Error: Output File "$@".grades already exists"
    exit 2
fi

if [[ ! -w `pwd` ]]
then
    echo "Error: Current directory is not writable."
    exit 2
fi
cut -d' ' -f4,5 $@ | cut -d'@' -f1
