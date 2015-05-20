#! /usr/bin/evn python2.6
# $Author: ee364d02 $
# $Date: 2013-09-18 14:49:03 -0400 (Wed, 18 Sep 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Lab05/sensors.py $
# $Revision: 59147 $

import sys
import math
values=[]
count=0
avg=0
low=1000
high=0
add=0

if len(sys.argv) != 2:
    print "Usage: sensors.py <sensor ID>"
    sys.exit(1)

row = sys.stdin.readline()


while row:
    row = row.strip()
    elements = row.split(':')
    if elements[0] == sys.argv[1]:
        values = elements[1]
        values = values.split(',')
        for i in values:
            i = float(i)
            if i > high:
                high = i
            if i < low:
                low = i
            count = count + 1
            add = add + i
   

    row = sys.stdin.readline()


if count == 0:
    print "No such sensor found."
    sys.exit(2)
else:
    avg=add/count
    print "min=%.3f, max=%.3f, sum=%.3f, avg=%.3f" % (low,high,add,avg)


sys.exit(0)
