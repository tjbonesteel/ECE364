#! /usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-30 13:18:33 -0400 (Wed, 30 Oct 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Prelab11/bitWorker.py $
# $Revision: 62157 $

import os
import sys
import math
import re


class Account:
	def __init__(self, owner, amount):
		self.owner = owner
                self.amount = float(amount)
		
	def deposit(self, amount):
                self.amount = self.amount + amount

	def withdraw(self, amount):
                self.amount = self.amount - amount
                                
	def endMonth(self):
		
		
	def __str__(self):
		# Converts this object to a string representation
		# Called when you convert this object to a string with str()
		return ("%s's account has a balance of %.2f") % (self.owner, self.amount)
				
class CheckingAccount(Account):
	def __init__(self, owner, value, fee):
		self.owner = owner
		self.value = value
		self.fee = fee
		
	def deposit(self, amount):
		self.amount = self.amount + amount
		
	def withdraw(self, amount):
		self.amount = self.amount - amount
		
	def endMonth(self):
		float balance = self.amount - self.fee
		if balance < 0:
			printf("%s's checking accont is overdrawn") % (self.owner)

		
	def __str__(self):
		return ("%s's account has a balance of $%.2f\nThe monthly fee is $%.2f ") % (self.owner, self.amount, self.fee)

class SavingsAccount:
	def __init__(self, str owner, float amount, float rate):
		self.owner = owner
		self.amount = amount
		self.rate = rate

	def withdraw(self, amount):
		self.amount = self.amount - amount
	def deposit(self, amount):
		self.amount = self.amount + amount
	def endMonth(self):
		float interest = self.amount * self.rate
		self.amount = self.amount + interest
	def __str__(self:
		return ("%s's account has a balance of $%.2f\nThe interest rate is %.4f\%") % ( self.owner, self.balance, self.rate)
	




