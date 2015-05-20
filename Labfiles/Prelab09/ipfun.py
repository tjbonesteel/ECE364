#!/usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-16 12:15:00 -0400 (Wed, 16 Oct 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab09/ipfun.py $
# $Revision: 61424 $

import sys
import os
import re

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

ipReg = "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
for line in fileINObj:
    line = line.strip()
    separate = line.split(":")
    
    try:
        port = int(separate[1])
        print separate[0]
        if re.match(ipReg,separate[0]):
            if 0 < port < 36768:
                if port < 1024:
                    print ("%s - Valid (root privileges required)") % (line)
                else:
                    print ("%s - Valid") % (line)
            else:
                print ("%s - Invalid Port Number") % (line)
        else:
            print ("%s - Invalid IP Address") % (line)
    except ValueError:
        print ("%s - Invalid Port Number") % (line)
        
    
    
