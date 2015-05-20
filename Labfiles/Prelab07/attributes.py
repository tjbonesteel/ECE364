#!/usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-01 22:39:47 -0400 (Tue, 01 Oct 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab07/attributes.py $
# $Revision: 60325 $


import sys
import os

if len(sys.argv) != 2:
    print "Usage: ./attributes.py"
    exit(1)
file = sys.argv[1]

#EXISTS
if os.path.exists(file):
    print "%s exists" % (file)
else:
    print "%s does not exist" % (file)
    exit(1)

#DIRECTORY
if os.path.isdir(file):
    print"%s is a directory" % (file)
else:
    print "%s is not a directory" % (file)

#ORDINARY FILE
if os.path.isfile(file):
    print "%s is an ordinary file" % (file)
else:
    print "%s is not an ordinary file" % (file)

#READABLE
if os.access(file,os.R_OK):
    print "%s is readable" % (file)
else:
    print "%s is not readable" % (file)

#WRITABLE
if os.access(file,os.W_OK):
    print "%s is writable" % (file)
else:
    print "%s is not writbale" % (file)
#EXECUTABLE
if os.access(file,os.X_OK):
    print "%s is executable" % (file)
else:
    print "%s is not executbale" % (file)
exit(0)

