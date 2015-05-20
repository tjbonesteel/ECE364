#! /usr/bin/evn python2.6
# $Author: ee364d02 $
# $Date: 2013-09-18 01:48:48 -0400 (Wed, 18 Sep 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab05/test_rwhile.py $
# $Revision: 58992 $

import sys
sum = 0
number = sys.argv[1]
num = int(number)
num = num + 1
run = range(num)
i = 0
while i < num:

    sum = sum + run[i]
    i=i+1
print sum

