#! /usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-08 23:56:18 -0400 (Tue, 08 Oct 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab08/lists.py $
# $Revision: 60851 $

import sys
import listmod

list1 = raw_input("Enter the first list of numbers: ")
list2 = raw_input("Enter the second list of numbers: ")

list1 = list1.split()
list2 = list2.split()

list1 = map(int,list1)
list2 = map(int,list2)

print ("First list: %s") % (list1)
print ("Second list: %s") % (list2)




(Median, Sorted_List) = listmod.find_median(list1,list2)

print ("Merged list: %s") % (Sorted_List)
print ("Median: %d") % (Median)

