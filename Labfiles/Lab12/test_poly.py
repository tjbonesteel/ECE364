#!/usr/bin/env python2.6
# encoding: utf-8

import poly

print "Step 1: Creating Polynomials"
try:
    A = poly.Polynomial([1, -2, 3, 3], [2, 3, -4, 0])
    print A
except:
    print "Unexpected exception!"

try:
    B = poly.Polynomial([1, -1, 1, 4], [0, 1, 2, 3])
    print B
except:
   print "Unexpected exception!"

try:
    C = poly.Polynomial([1, 2, 2, 2], [1, 2, 3])
    print C
except ValueError as e:
    print "ValueError: %s" %e

print "Step 2: Evaluating Polynomials"
try:
    print "A.evaluateAt(2) = %f" % (A.evaluate(2))
    print "B.evaluateAt(7) = %f" % (B.evaluate(7))
except:
    print "Unexpected exception!"

print "Step 3: Differentiation"
try:
    dA = A.differentiate()
    print dA
except:
    print "Unexpected exception!"

try:
    dB = B.differentiate()
    print dB
except:
    print "Unexpected exception!"

print "Step 4: Evaluating the derivative"
try:
    print "dA.evaluateAt(2) = %f" % (dA.evaluate(2))
    print "dB.evaluateAt(7) = %f" % (dB.evaluate(7))
except:
    print "Unexpected exception!"

print "Step 5: Checking validity of Polynomials"

if not poly.isValidPolynomialString("-3x^2+4x^3+10"):
    raise Exception("Check your regular expression!")
	
if poly.isValidPolynomialString("x^4.2 + 99"):
    raise Exception("Check your regular expression!")
	
if not poly.isValidPolynomialString("1-2+4"):
    raise Exception("Check your regular expression!")
else:
    print "Your regular expression looks good!"
