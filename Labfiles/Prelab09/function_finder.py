#!/usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-16 13:03:21 -0400 (Wed, 16 Oct 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab09/function_finder.py $
# $Revision: 61432 $

import sys
import os
import re

if len(sys.argv) != 2:
    print "Usage: function_finder.py <input file>"
    exit(1)

fileIN = sys.argv[1]


######### FILE TESTS #############
#EXISTS
if not os.path.exists(fileIN):
    print "Error: could not read %s." % (fileIN)
    exit(1)

#ORDINARY FILE
if not os.path.isfile(fileIN):
    print "Error: could not read %s." % (fileIN)
    exit(1)

#READABLE
if not os.access(fileIN,os.R_OK):
    print "Error: Could not read %s." % (fileIN)
    exit(1)
###################################

fileINObj = open(fileIN, "r")


for line in fileINObj:
    ind = 0
    line = line.strip()
    m = re.search(r"^\s*def (\S+)\s*\((\s*\S+\s*(?:,\s*\S+))*\):$",line)
    if m:
        function_Name = m.group(1)
        print function_Name
        paramList = m.group(2)
        paramList = paramList.split(",")
        arg = paramList[0].strip()
        for item in paramList:
            item = paramList[ind].strip()
            print ("Arg%d: %s") % (ind+1,item)
            ind = ind + 1
