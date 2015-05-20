#! /usr/bin/env python2.7
# $Author: ee364d02 $
# $Date: 2013-09-18 14:14:19 -0400 (Wed, 18 Sep 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Lab05/email_list.py $
# $Revision: 59124 $

import sys

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print "email_list.py <type> [email host] < emails.in"
    sys.exit(1)

s = sys.stdin.readline()
emailList=[]
nameList=[]
while s:
    s=s.strip()
    items = s.split('|')
    
    
    if items[0].upper() == sys.argv[1].upper():
        nameList.append(items[2])
        emailList.append(items[3])
    
    if len(sys.argv) == 3:
        items = s.split('@')
        if items[1] == sys.argv[2]:
            items = s.split('|')
            nameList.append(items[2])
            emailList.append(items[3])
    s=sys.stdin.readline()


i=0
while i < len(emailList):
    sys.stdout.write("%s <%s>;" % (nameList[i], emailList[i]))
    i=i+1
print "\n"

sys.exit(0)
