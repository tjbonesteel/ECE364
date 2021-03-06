#! /usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-28 22:36:56 -0400 (Mon, 28 Oct 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab11/assemblyCheck.py $
# $Revision: 62036 $

import os
import sys
import math
import re

if len(sys.argv) != 2:
    print "Usage: ./sensors.py <input file>"
    exit(1)

fileIN = sys.argv[1]


######### FILE TESTS #############
#EXISTS
if not os.path.exists(fileIN):
    print "%s is not a readable file." % (fileIN)
    exit(2)

#ORDINARY FILE
if not os.path.isfile(fileIN):
    print "%s is not a readable file!" % (fileIN)
    exit(2)

#READABLE
if not os.access(fileIN,os.R_OK):
    print "%s is not a readable file" % (fileIN)
    exit(2)
###################################

fileINObj = open(fileIN, "r")

instReg = "(lw|sw|add|sub|mul|div|beq|jmp)"
reg1 = "(\$t[0-7])"
reg2 = "(\![0-9]+)"
lnCount = 0
for line in fileINObj:
        lnCount = lnCount + 1
        i = 0
        line = line.strip()
        tLine = line.split(" ")
        inst = tLine[0]
        match1 = re.search(instReg,inst)
        if match1:
            tLine = tLine[1]
            tLine = tLine.split(",")
            count = len(tLine)
            
            while i < count:
                match2 = re.search(reg1,tLine[i])
                match3 = re.search(reg2,tLine[i])
                if not match2:
                    if not match3:
                        print "Error: invalid line %d" % (lnCount)
                    elif (i == 0):
                        print "Error: invalid line %d" % (lnCount)
                
                i = i + 1
        else:
            print "Error: invalid line %d" % (lnCount)

exit(0)
