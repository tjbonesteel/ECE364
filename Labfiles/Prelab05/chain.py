#! /usr/bin/evn python2.6
# $Author: ee364d02 $
# $Date: 2013-09-18 13:21:08 -0400 (Wed, 18 Sep 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab05/chain.py $
# $Revision: 59109 $

import sys
i=2
s=sys.stdin.readline()
tupList=[]
regionList=[]
masterList=[]
predator="d"
validRegion = 0
validPrey = 0
while s:
    
    items = s.split()
    row = [items[0]]
    if items[0] == sys.argv[1]:
        validRegion = 1
    while i < len(items):
       temp=(items[i-1],items[i])
       if items[i-1] == sys.argv[2]:
           predator = items[i]
           validPrey = 1
       tupList.append(temp)
       i=i+1
    
    row.append(tupList)
    masterList.append(row)
    tupList=[]
    i=2
    s=sys.stdin.readline()
    
print masterList
if validRegion == 0:
    print "\nUnknow region: %s\n" % (sys.argv[1])
if validPrey == 0:
    print "\nNo chain entry for %s\n" % (sys.argv[2])
else:
    print "\nIn the %s the %s is eaten by the %s.\n" % (sys.argv[1],sys.argv[2],predator)
    
sys.exit(0)
