#! /usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-09 00:57:32 -0400 (Wed, 09 Oct 2013) $
# $HeadURL: svn+ssh://ece
# $Revision: 60856 $

import os
import sys

inFile = sys.argv[1]

if len(sys.argv) != 2:
    print ("Usage: Parse.py <filename>;")
    exit(1)
try:
    fp = open(inFile, "r")
except IOError as e:
    sys.stderr.write("%s is not a readable file.\n" % (inFile))

for line in fp:
    total = 0
    count = 0
    avg = 0
    strings = ""
    line = line.split()

    for x in line:
        try:
            x = float(x)
            total+= x
            count+= 1
        except ValueError:
            strings+=x
            strings+=" "

    
    if total != 0:
        avg = total/count
        print ("%.3f %s") % (avg,strings)
    else:
        print ("%s") % (strings)
