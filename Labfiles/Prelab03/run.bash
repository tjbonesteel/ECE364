#! /bin/bash
#
# $Author: ee364d02 $
# $Date: 2013-09-04 12:45:42 -0400 (Wed, 04 Sep 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab03/run.bash $
# $Revision: 57865 $


if [[  -e $file ]]
then
    echo ""$@" already exists. would you like to delete it?"
    exit 2
fi
