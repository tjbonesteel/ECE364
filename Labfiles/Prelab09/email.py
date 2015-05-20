#! /usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-16 10:54:46 -0400 (Wed, 16 Oct 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab09/email.py $
# $Revision: 61374 $
import re

fileIN = open("Part2.in", "r")

for line in fileIN:
    str = re.sub(r"@purdue.edu","@ecn.purdue.edu",line)
    str = re.sub(r"\n","/100",str)
    print str

