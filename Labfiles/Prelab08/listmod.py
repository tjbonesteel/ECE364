# $Author: ee364d02 $
# $Date: 2013-10-08 23:56:18 -0400 (Tue, 08 Oct 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab08/listmod.py $
# $Revision: 60851 $
import sys
import os

def find_median(l1,l2):

    mergedList = l1
    mergedList.extend(l2)
    mergedList.sort()
    median = mergedList[(len(mergedList)-1)/2]
    tuple1 = (median,mergedList)
    return tuple1
        
