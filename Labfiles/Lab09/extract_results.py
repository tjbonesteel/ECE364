#!/usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-16 15:22:23 -0400 (Wed, 16 Oct 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Lab09/extract_results.py $
# $Revision: 61502 $

import sys
import os
import re

if len(sys.argv) != 4:
    print "Usage: extract_results.py <input file> <course> <min_percentage>"
    exit(1)

fileIN = sys.argv[1]
course = sys.argv[2]

#READABLE
if not os.access(fileIN,os.R_OK):
    print "Error: %s is not a readable file." % (fileIN)
    exit(2)

#ORDINARY FILE
if not os.path.isfile(fileIN):
    print "Error: %s is not a readable file." % (fileIN)
    exit(2)

perReg = ".*(/d+)"

fileINObj = open(fileIN, "r")
found = 0

courseReg = "<PATH.*" + course
counter = 1



for line in fileINObj:
    line = line.strip()
    
    v = re.search(r".*(<VAL>).*(?P<val>(\d+))",line)
    if v:
        valLine = line.split(">")
        
   
    m = re.search(courseReg,line)
    if m:
        sline = line.split("/")
        per = sline[4]
        t = re.search(r".*\((?P<percent>(\d+))",per)
        if t:
            print t.group('percent')
        if counter % 2 != 0:
           
            student1 = sline[2]
            
        if counter % 2 == 0:
            student2 = sline[2]
            print ("User1: %s User2: %s Lines Matched: %s") % (student1,student2,valLine[1])
            
        counter = counter + 1
        found = 1
    
exit(0)
