#! /usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-30 13:18:33 -0400 (Wed, 30 Oct 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab11/bitWorker.py $
# $Revision: 62157 $

import os
import sys
import math
import re
import Accounts_Gold

def readAccountFile(infile):
	infileOBJ = open(infile, "r")
	accounts = {}
	curAccount = {}
	regSec1 = "^[A-Z]{2}([0-9]|[1-2][0-9]|3[0-1])[a-z]?$"
	regSec2 = "^([A-Za-z0-9]{7})(AX|BY)[0-9]{3}$"
	regSec3 = "^sec-[1-9][0-9][0-9]$"	
	
	for line in infileOBJ:
		
		line = line.strip()
		line = line.split(",")
		ID = line[1]
		security1 = line[0]
		security2 = line[3]
		security3 = line[6]
		name = line[2]
		balance = line[4]
		balance = float(balance[1:])
		modifier = float(line[5])
		if accounts.has_key(ID):	
			print("Error! ID %s is already in use!") % (ID)
		if re.match(regSec1, security1):
			if re.match(regSec2, security2):
				iRate = modifier/100
                                acc = Accounts_Gold.SavingsAccount(name,balance,iRate)
				account = {ID:acc}
				accounts.update(account)			
			if re.match(regSec3, security3):
                                acc = Accounts_Gold.CheckingAccount(name,balance,modifier)
				account = {ID:acc}
				accounts.update(account)
	

#if __name__ == main:
# The standard argument checks
if len(sys.argv) != 3:
	sys.stderr.write("usgae: parseTransactions.py <accounts filename> <transactions filename>\n")
	sys.exit(1)

if not os.path.isfile(sys.argv[1]) or not os.access(sys.argv[1], os.R_OK):
	sys.stderr.write("error: %s is not a readable file.\n" % (sys.argv[1],))
	sys.exit(2)

if not os.path.isfile(sys.argv[2]) or not os.access(sys.argv[2], os.R_OK):
	sys.stderr.write("error: %s is not a readable file.\n" % (sys.argv[2],))
	sys.exit(3)

infile = sys.argv[1]
transfile = sys.argv[2]

trans = open(transfile, "r")
for line in trans:
	line = line.strip()
	sline = line.split(",")
        ID = sline[0]
        date = sline[1]
        month = date.split("/")[0]
        tType = line[2]
        ammount = line[3][1:]
        acc = accounts[ID]
        if tType == "WITHDRAWAL":
                acc = Accounts_Gold.SavingsAccount.withdraw(acc, ammount)

	













