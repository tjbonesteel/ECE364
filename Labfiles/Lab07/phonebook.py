#!/usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-02 15:09:45 -0400 (Wed, 02 Oct 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Lab07/phonebook.py $
# $Revision: 60493 $

import sys
import os

if len(sys.argv) != 2:
    print "Usage: ./phonebook.py <filename>"
    exit(1)

fileIN = sys.argv[1]
######### FILE TESTS #############
#READABLE
if not os.access(fileIN,os.R_OK):
    print "%s is not a readable file" % (fileIN)
    exit(2)
###################################

areaCodes={'219':'valparaiso','317':'indianapolis','812':'chicago','216':'cleveland','313':'detroit'}
phoneBooks={}
fileObj = open(fileIN, "r")

for line in fileObj:
    line = line.strip()
    lineTest = line.split()
    phone = lineTest[1]
    code = phone[:3]
    for key in areaCodes:
        if code == key:
            name = areaCodes.get(key)
            if not phoneBooks.has_key(name):
                phoneBooks[name]=[line]
            else:
                phoneBooks[name].append(line)
               
bookCount = 0
for key in phoneBooks:
    bookCount = bookCount + 1
    fileName = key + ".dat"
    fileOut = open(fileName, "w")
    people = phoneBooks[key]
    for i in people:
        fileOut.write(i+"\n")

print "Wrote phonebooks for %d regions" % (bookCount)

exit(0)
