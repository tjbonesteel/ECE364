#! /bin/bash
#
# $Author: ee364d02 $
# $Date: 2013-09-24 20:57:32 -0400 (Tue, 24 Sep 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab06/file_packager.bash $
# $Revision: 59757 $

numParam=$#

if [ $numParam != 2 ]
then
    echo "Usage: file_packager.bash <directory> <file type>"
    exit 1
fi

if [ ! -r $1 ]
then
    echo "$1 is not a readable directory"
    exit 2
fi    

directory=$(mktemp -d XXXXX)
if [ $? != 0 ]
then
    echo "Error: Could not create working directory."
    exit 3
fi

filesARR=$(find $1)

fileExt=$2
regex="[a-z]{1}.$fileExt"

for i in $filesARR
do
    file=$i
    str=${file##*/}
    if [[ $str =~ $regex ]]
    then
	
	if [[ -e $directory/$str ]]
	then
	    echo "Warning: $str was already added to the archive."
	else
	    cp $file $directory
	fi
    fi

done

tar -cf files.tar $directory
if [ $? != 0 ]
then
    echo "failed to create tar archive files.tar"
    exit 4
fi

gzip files.tar

if [ $? != 0 ]
then
    echo "failed to zip tar archive files.tar"
    exit 5
fi

