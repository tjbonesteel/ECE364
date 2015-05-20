#! /usr/bin/evn python2.6
# $Author: ee364d02 $
# $Date: 2013-09-18 01:21:20 -0400 (Wed, 18 Sep 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab05/test_if.py $
# $Revision: 58980 $
import sys

arg = sys.argv[1]
arg1 = int(arg)

if arg1 < 7:
    print "Low value"
elif arg1 > 7:
    print "High value"
else:
    print "Neither"
