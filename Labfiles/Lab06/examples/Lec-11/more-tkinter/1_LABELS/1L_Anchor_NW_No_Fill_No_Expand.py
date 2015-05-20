#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:30:05 $
#   $Revision: 1.1 $

# The script keeps the button in the TOP LEFT of
# the window when expanded 
# The button is anchored to the NW (North West) corner
# No Fill or expand options

from Tkinter import *
import sys

Root = Tk()
Root.title(sys.argv[0])

My_Label = Label(Root, text = '1L: Hello EE 364 Students',
                       fg="White", # foreground color
                       bg="Green", # background color
                       font=("Helvetica", 24, "normal"))
My_Label.pack(anchor=NW) 
Root.mainloop()

