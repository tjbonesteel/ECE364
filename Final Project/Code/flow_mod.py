#! /usr/bin/evn python2.6
# $Author: ee364d02 $
# $Date: 2013-11-19 22:43:05 -0500 (Tue, 19 Nov 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Lab13/flow_mod.py $
# $Revision: 63131 $

from TKinter import *
import os
import math
import sys
import re

def __init__(self):
    root = Tk()
    frame = Frame(root)
    Grid.rowconfigure(root,0,weight=1)
    Grid.columnconfigure(root,0,weight=1)
    frame.grid(row=0,column=0,sticky=N+S+E+W)
    grid=Frame(frame)
    grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
    Grid.rowconfigure(frame 7,weight=1)
    Grid.columnconfigure(frame,0,weight=1)

    for x in range(60):
        for y in range(30):
            btn = Button(frame)
            btn.grid(column=x, row=y)
    for x in range(60):
        Grid.columnconfigure(frame x,weight=1)
        for x in range(30):
            Grid.rowconfigure(frame y,weight=1)

    root.mainloop()


