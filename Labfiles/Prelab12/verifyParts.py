#! /usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-30 13:18:33 -0400 (Wed, 30 Oct 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab11/bitWorker.py $
# $Revision: 62157 $

import os
import re
import math
import sys

if len(sys.argv) != 2:
	sys.stderr.write("usgae: parseTransactions.py <accounts filename> <transactions filename>\n")
	sys.exit(1)

if not os.path.isfile(sys.argv[1]) or not os.access(sys.argv[1], os.R_OK):
	sys.stderr.write("error: %s is not a readable file.\n" % (sys.argv[1],))
	sys.exit(2)
file = sys.argv[1]
good = ".good"
bad = ".bad"
fileOutGood = str(file) + good
fileOutBad = str(file) + bad

#if not os.path.isfile(fileOutGood):
#    sys.stderr.write("error: %s already exists.\n" % (fileOutGood,))
#    sys.exit(2)
#
#if not os.path.isfile(fileOutBad):
#    sys.stderr.write("error: %s already exists.\n" % (fileOutBad,))
#    sys.exit(2)
#
infile = open(sys.argv[1], "r")

outfileGood = open(fileOutGood,"w")
outfileBad = open(fileOutBad, "w")

regex1 = "^[0-9]{2}[A-Z][0-9]{4}(\-(NJ|IN|FL)20(0[7-9]|1[0-3]))?(\*)?$"
regex2 = "^[0-9]+$"



for line in infile:
    line = line.strip()
    sline = line.split(",")
    partNum = sline[0]
    quantity = sline[2]
    
    if re.match(regex1, partNum):
        if re.match(regex2, quantity):
            outfileGood.write(line+"\n")
        else:
            outfileBad.write(line+"\n")
    else:
        outfileBad.write(line+"\n")
    
