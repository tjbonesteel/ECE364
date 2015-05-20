#! /usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-09 00:29:09 -0400 (Wed, 09 Oct 2013) $
# $HeadURL: svn+ssh://ece
# $Revision: 60853 $

masterList  = raw_input("Please enter some values: ")
masterList = masterList.split()
total = 0

for x in masterList:
    try:
        x = float(x)
        total = total + x
    except ValueError:
        x = x


print ("The sum is: %.1f") % (total)
