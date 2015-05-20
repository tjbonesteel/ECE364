#! /usr/bin/env python2.6


import sys




if len(sys.argv) != 1:
    print "Usage: ./hist.py"
    sys.ext(1)


IFS=" "
for line in sys.stdin:
    zone = [0,0,0,0,0,0,0,0,0,0]
    i=0
    line=line.strip()
    line = line.split(" ")
    number=int(line[1])
    number = number / 5
    number = number / 2 + number % 2
    
    while i < number:
        zone[i]=1
        
        
        i=i+1
        
    zone=str(zone)
    print line[0] + zone
    


sys.exit(0)
