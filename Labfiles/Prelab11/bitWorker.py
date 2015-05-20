#! /usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-30 13:18:33 -0400 (Wed, 30 Oct 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab11/bitWorker.py $
# $Revision: 62157 $

import os
import sys
import math
import re


def displayBinary( num ):
    binary = bin(num)
    binary = binary[2:]
    return binary.zfill(16)

def getBit(index, num):
    if index > 31 or index < 0:
        raise ValueError(index)
    binary = displayBinary(num)
    binary = str(binary)
    index = 15-index
    return binary[index:index+1]

def getPartialValue(index1, index2, num):
    if index1 > 31 or index1 < 0:
        raise ValueError(index)
    if index2 > 31 or index2 < 0:
        raise ValueError(index)
    binary = displayBinary(num)
    binary = str(binary)
    index1 = 15 - index1 + 1
    index2 = 15 - index2
    bin2 = binary[index2:index1]
    return int(str(bin2),2)


print displayBinary(10)
print getBit(0, 99)
print getPartialValue(1, 3, 22)



exit(0)
