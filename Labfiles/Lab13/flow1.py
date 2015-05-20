#! /usr/bin/env python2.6
# $Author: ee364d02 $
# $Date: 2013-11-18 19:03:54 -0500 (Mon, 18 Nov 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/F13/students/ee364d02/Lab13/flow.py $
# $Revision: 63002 $

from Tkinter import *
import os
import sys
import math
import re
import tkMessageBox
curLevel = 0





class Board(Frame):

    def __init__(self, nodes, terminals, master=None):
        Frame.__init__(self, master,background="gray")
        global curLevel
        self.grid()
        self.nodes = nodes
        self.match=[]
        self.terminals = terminals
        self.master.title("Flow")
        self.master = master
        self.startx = 0
        self.starty = 0
        self.gcol = 0
        self.grow = 0
        self.color = 0
        
        self.goalNum = len(self.terminals)/2
        self.score = goalNum*20
        for i in range(self.goalNum):
            self.match.append(0)
        
    

    def refresh(self):
        self.color = 0
        self.grow = 0
        self.gcol = 0
        self.startx = 0
        self.starty = 0
        for key, value in self.nodes.items():
            btn = Board.Node(self, value, key[0], key[1])
            btn.grid(column=key[1],row=key[0])
            Board.Node.btColor(btn, value)
            
        for key, value in self.terminals.items():
            btn = Board.Terminal(self, value, key[0], key[1])
            btn.grid(column=key[1],row=key[0])
            Board.Node.btColor(btn, value)
            
    def clearBoard(self):
        for key, value in self.nodes.items():
            self.nodes[key] = "0"
        for value in range(len(self.match)):
            self.match[value]=0
        self.score = self.goalNum*20
        self.refresh()
    

    class Node(Button):
        def __init__(self,master, num, row, col, **configs):
            Button.__init__(self, master, **configs)
            self.config(width=10,height=5, font=('Arial', 12), command=self.Callback)
            self.num = num
            self.row = row
            self.col = col
            self.master = master

        def btColor(self, num):
            if num == "0":
                self.config(bg="gray")
            elif num == "1":
                self.config(bg="red", highlightcolor="red4")
            elif num == "2":
                self.config(bg="Yellow")
            elif num == "3":
                self.config(bg="Green")
            elif num == "4":
                self.config(bg="Blue")
            elif num == "5":
                self.config(bg="Orange")
            self.master.nodes[self.row,self.col]=num 
            
                
        def Callback(self):
            self.master.score -= 2
            if self.row == self.master.grow:
                if self.col == self.master.gcol+1 or self.col == self.master.gcol-1:
                    if self.master.color != 0 and self.num == "0":
                        self.btColor(self.master.color)
                        self.master.gcol = self.col
                        self.master.grow = self.row
                        self.num = self.master.color
                        self.checkComplete()
                        
            elif self.col == self.master.gcol:
                if self.row == self.master.grow+1 or self.row == self.master.grow-1:
                    if self.master.color != 0 and self.num == "0":
                        self.btColor(self.master.color)
                        self.num = self.master.color
                        self.master.gcol = self.col
                        self.master.grow = self.row
                        self.checkComplete()
            
       
        def checkComplete(self):
            global curLevel
            
            done = 0
            ind = int(self.num)-1
            
            try:
                if self.master.terminals[self.row+1,self.col] == self.num:
                    if self.row+1 != self.master.startx:
                        self.master.match[ind] = 1
                    elif self.col != self.master.col:
                        self.master.match[ind] = 1
            except Exception, e:
                pass
            try:
                if self.master.terminals[self.row,self.col+1] == self.num:
                    if self.master.starty != self.col+1:
                        self.master.match[ind] = 1
                    elif self.master.startx != self.row:
                        self.master.match[ind] = 1
            except Exception, e:
                pass

            try:
                if self.master.terminals[self.row-1,self.col] == self.num:
                    if self.row-1 != self.master.startx:
                        self.master.match[ind] = 1
                    elif self.col != self.master.starty:
                        self.master.match[ind] = 1
            except Exception, e:
                pass
            try:
                if self.master.terminals[self.row,self.col-1] == self.num:
                    if self.master.starty != self.col-1:
                        self.master.match[ind] = 1
                    elif self.master.startx != self.row:
                        self.master.match[ind] = 1
            except Exception, e:
                pass
            if sum(self.master.match) == self.master.goalNum:
                
                for value in self.master.nodes.values():
                    
                    if value == "0":
                        done = 0
                        break
                    else:
                        done = 1
            if done == 1:
                
                playAgain = tkMessageBox.askquestion("Congratulations!","You have completed the board with %d points!\n Would you like to continue?"%(self.master.score))
                if playAgain == 'yes':
                    self.master.clearBoard()
                    self.master.grid_forget()
                    curLevel = 0
                    tkMessageBox.showinfo("Awesome!","Please select a level from the menu!")
                else:
                    self.master.master.quit
                    
            
            

    class Terminal(Node):
        def __init__(self,master,num, row, col,**configs):
            Board.Node.__init__(self, master,num, row, col, **configs)
            self.num = num
            self.row = row
            self.col = col
            self.master = master

        def Callback(self):
            
            if self.master.color == self.num:
                for key, value in self.master.nodes.items():
                    if value == self.master.color:
                        self.master.nodes[key] = "0"
                
                Board.refresh(self.master)
                        
            else:
                self.master.color = self.num
                self.master.startx = self.row
                self.master.starty = self.col
            self.master.gcol = self.col
            self.master.grow = self.row

def readFile(fileIN):
    
    nodes={}
    terminals={}
    fileOBJ = open(fileIN)
    global goalNum
    row=0
    for line in fileOBJ:
        line = line.strip()
        sLine = line.split(",")
        width = len(sLine)
        for column in range(width):
            if sLine[column] == "0":
                nodes[row,column]=sLine[column]
            else:
                terminals[row,column]=sLine[column]
        row += 1
        goalNum =  len(terminals)/2
    
    level = Board(nodes, terminals)
    Board.refresh(level)
    fileOBJ.close()
    return level

def showBoard(level):
    global curLevel
    if curLevel != 0:
        save = tkMessageBox.askquestion("Save?","Would you like to save your progress?")
        if save == 'no':
            Board.clearBoard(curLevel)
        curLevel.grid_forget()
    
    curLevel = level
    curLevel.grid()
    curLevel.focus_set()

def restart():
    global curLevel
    if curLevel != 0:
        Board.clearBoard(curLevel)

        
            

### Check num args & if can read file
if len(sys.argv) < 2:
    print "Usage: ./flow.py <Input File>"
    exit(1)

fileIN1 = sys.argv[1]
fileIN2 = sys.argv[2]
fileIN3 = sys.argv[3]
fileIN4 = sys.argv[4]
fileIN5 = sys.argv[5]
if not os.access(fileIN1,os.R_OK):
    print "%s is not a readable file" % (fileIN1)
    exit(1)
if not os.access(fileIN2,os.R_OK):
    print "%s is not a readable file" % (fileIN1)
    exit(1)
if not os.access(fileIN3,os.R_OK):
    print "%s is not a readable file" % (fileIN1)
    exit(1)
if not os.access(fileIN4,os.R_OK):
    print "%s is not a readable file" % (fileIN1)
    exit(1)
if not os.access(fileIN5,os.R_OK):
    print "%s is not a readable file" % (fileIN1)
    exit(1)


### Open input file and create main board

root=Tk()
root.geometry("700x700+300+300")

### Load input file and create buttons



level1 = readFile(fileIN1)
level1.grid_forget()
level2 = readFile(fileIN2)
level2.grid_forget()
level3 = readFile(fileIN3)
level3.grid_forget()
level4 = readFile(fileIN4)
level4.grid_forget()
level5 = readFile(fileIN5)
level5.grid_forget()
levels = [level1, level2, level3, level4, level5]


menubar = Menu(root)
optionMenu = Menu(menubar)
levelMenu = Menu(optionMenu)
menubar.add_cascade(label="Start", menu=optionMenu)
optionMenu.add_command(label="Restart", command=restart)
optionMenu.add_cascade(label="Level Select", menu=levelMenu)
levelMenu.add_command(label="Level 1", command=lambda level=level1: showBoard(level))
levelMenu.add_command(label="Level 2", command=lambda level=level2: showBoard(level))
levelMenu.add_command(label="Level 3", command=lambda level=level3: showBoard(level))
levelMenu.add_command(label="Level 4", command=lambda level=level4: showBoard(level))
levelMenu.add_command(label="Level 5", command=lambda level=level5: showBoard(level))

menubar.add_command(label="Exit", command=root.quit, background="red")
root.config(menu=menubar)







root.mainloop()
