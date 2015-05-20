#!/usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-02 13:17:59 -0400 (Wed, 02 Oct 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab07/sensors.py $
# $Revision: 60441 $

import sys
import os

if len(sys.argv) != 2:
    print "Usage: ./sensors.py <input file>"
    exit(1)

fileIN = sys.argv[1]


######### FILE TESTS #############
#EXISTS
if not os.path.exists(fileIN):
    print "%s is not a readable file." % (fileIN)
    exit(1)

#ORDINARY FILE
if not os.path.isfile(fileIN):
    print "%s is not a readable file!" % (fileIN)
    exit(1)

#READABLE
if not os.access(fileIN,os.R_OK):
    print "%s is not a readable file" % (fileIN)
    exit(1)
###################################

fileINObj = open(fileIN, "r")
tempSum=0
tempMin=0
tempMax=0
tempCount=0


sensors={}
for line in fileINObj:
    line = line.strip()
    lineList = line.split(":")
    sensorVals=lineList[1].split(",")
    for i in sensorVals:
        sensorNums=float(i)
    if sensors.get(lineList[0],"notFound") == "notFound":
        sensors[lineList[0]]=sensorVals
    else:
        sensors[lineList[0]].append(sensorVals)

print sensors.keys()


