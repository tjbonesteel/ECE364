#! /usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-10-09 00:57:32 -0400 (Wed, 09 Oct 2013) $
# $HeadURL: svn+ssh://ece
# $Revision: 60856 $

import string
import re

def is_valid_name(identifier):
    identifier = identifier.strip()
    matching = re.match('[A-Za-z0-9-_]', identifier)
    if matching:
        return True
    else:
        return False

    
def parse_pin_assignment(assignment):
    assign = assignment.strip()
    assign = assign.split()
    tups = ()

    matches = re.match('.[A-Za-z0-9_]([0-90-9])')
    if matches:
        assign = assign.replace(".","")
        assign = assign.replace("(","")
        assign = assign.replace(")","")
        tups = (assign[0],assign[1:])
        print tups
        return tups
    else:
        raise ValueError(assign)
    


