#!/usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-16 15:22:10 -0400 (Wed, 16 Oct 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Lab09/sensor_to_xml.py $
# $Revision: 61500 $

import sys
import os
import re

if len(sys.argv) != 3:
    print "Usage: ./sensor_to_xml.py <input file> <output file>"
    exit(1)

fileIN = sys.argv[1]
fileOUT = sys.argv[2]

try:
    fileINObj = open(fileIN, "r")
except IOError as e:
    print ("Error when opening input file: %s") % (e)
    exit(2)
try:
    fileOUTObj = open(fileOUT, "w")
except IOError as e:
    print ("Error when opening output file: %s") % (e)
    exit (3)



fileOUTObj.write("<sensor>\n")
for line in fileINObj:
    line = line.strip()
    two = line.split(":")
    name = two[0]
    vals = two[1]
    m = re.search(r"(?P<state>(FL|RI|NY|NJ))(?P<type>[P|T|R])(?P<id>(\d*)\-([(\w)]{4})?)",name)
    if m:
        state = m.group('state')
        typ = m.group('type')
        id1 = m.group('id')
        fileOUTObj.write((" <sensor state=\"%s\" type=\"%s\" id=\"%s>\"\n") % (state,typ,id1))
        
        vals = vals.split(",")
        for val in vals:
            n = re.search("(-)?(\d)+\.(\d)+",val)
            if n:
                fileOUTObj.write(("   <val>%s</val>\n") % (val))
            

fileOUTObj.write("</sensor>\n")

fileINObj.close()
fileOUTObj.close()
exit(0)
