#! /usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-11-06 15:24:53 -0500 (Wed, 06 Nov 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Lab12/scanner.py $
# $Revision: 62741 $


import re
import sys
import math
import os

if len(sys.argv) != 3:
    raise IOError("usage: scanner.py <input_file> <output_file>\n")
    sys.exit(1)
try:
    fp = open(sys.argv[1], "r")
except IOError as e:
    sys.stderr.write("IOError: <input file> is not a readable file\n")
    sys.exit(2)

regOp = "^(\+|-|\*|\/|=||\!\=|\<|\>|\)|\(|\:|\,|\<\=|\>\=|\:\=|\;)$"
regKeyword = "^(PROGRAM|BEGIN|END|FUNCTION|READ|WRITE|IF|ELSEIF|ENDIF|DO|WHILE|CONTINUE|BREAK|RETURN|INT|VOID|STRING|FLOAT|TRUE|FALSE)+$"
regInt = "^([0-9]+)$"
regFloat = "^([0-9]*\.[0-9]+)$"
regString = "(\".*\")"
regIden = "^()$"
regComm = "^(--)"

op = open(sys.argv[2], "w")

for line in fp:
        
    sline = line.split()
    tline = line.split("--")
    counter = 0
    for item in sline:
        counter = counter + 1
        if re.match(regComm, item):
            tokenType = "COMMENT"
            value = tline[1]
            op.write("Token Type:   %s\n" % (tokenType))
            op.write("Value:   %s" % (value))
            op.write("------------------------\n")
            break
        elif re.match(regOp, item):
            tokenType = "OPERATOR"
            value = item
        elif re.match(regKeyword, item):
            tokenType = "KEYWORD"
            value = item
        elif re.match(regInt, item):
            tokenType = "INT"
            value = item
        elif re.match(regFloat, item):
            tokenType = "FLOAT"
            value = item
        elif re.search(regString, line):
            tokenType = "STRINGLITERAL"
            value = re.findall(regString, line)
            value = value[0]
            op.write("Token Type:   %s\n" % (tokenType))
            op.write("Value:   %s\n" % (value))
            op.write("------------------------\n")
                
                
                
                
        else:
            tokenType = "IDENTIFIER"
            value = item
        
        op.write("Token Type:   %s\n" % (tokenType))
        op.write("Value:   %s\n" % (value))
        op.write("------------------------\n")

sys.exit(0)
