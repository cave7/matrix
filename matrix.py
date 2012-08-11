#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import time
import random
import string
#import traceback
import curses
class View:
    def __init__(self):
        self.screen = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1,curses.COLOR_GREEN,-1)
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.screen.keypad(1)
    def __del__(self):
        curses.nocbreak()
        self.screen.keypad(0)
        curses.echo()
        curses.curs_set(1)
        curses.endwin()
    def displayMatrix(self,matrix):
        self.screen.erase()
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                #try:
                self.screen.addstr(y,x,matrix[y][x],curses.color_pair(1)|curses.A_BOLD)
                        #except:
                        #    f=open('log.txt','a')
                        #    f.write(str(x)+'\t'+str(y)+'\n')
                        #    f.close()
        self.screen.refresh()
        return
    def getScreenYX(self):
        return self.screen.getmaxyx()
    def displayText(self,y,x,text):
        #self.screen.erase()
        self.screen.addstr(y,x,text,curses.color_pair(1)|curses.A_BOLD)
        self.screen.refresh()
        return

class Matrix:
    def __init__(self,y,x):
        self.y=y
        self.x=x
        self.promoteChance=0.001
        self.matrix=[[' ' for i in range(x)] for j in range(y)]
        self.position=[-1 for i in range(x)]
        
        self.text='''If there exists on any subject a philosophy (that is, a system of
            rational knowledge based on concepts), then there must also be for
            this philosophy a system of pure rational concepts, independent of any
            condition of intuition, in other words, a metaphysic.'''
        random.seed()
    def promote(self):
        for i in range(len(self.position)):
            if self.position[i]==-1:
                if random.random()<self.promoteChance:
                    self.position[i]=0
            else:
                self.position[i]+=1
                if self.position[i]==len(self.text):
                    self.position[i]=-1
    
    def fill(self):
        line=[]
        for i in self.position:
            if i==-1:
                line.append(' ')
            else:
                line.append(self.text[i])
        self.matrix.pop(-1)
        self.matrix.insert(0,line)
    def mutate(self):
        quantity=random.randint(0, 50)
        for i in range(quantity):
            rx=random.randint(0,self.x-1)
            ry=random.randint(0,self.y-1)
            if self.matrix[ry][rx]!=' ':
                replacement=random.choice(string.octdigits)
                self.matrix[ry][rx]=replacement
    def refresh(self):
        self.promote()
        self.fill()
        self.mutate()
        return self.matrix
    def genText(self):
        pass

#print "ddd"
v=View()
#v.displayText(0,0,'kkkkkkkk')
#time.sleep(2)
(y,x)=v.getScreenYX()
#v.displayText(0,0,str(y))
#v.displayText(1,0,str(x))
#v.displayMatrix([['s','w'],['o','e']])
#time.sleep(2)
#m=Matrix(20,40)
m=Matrix(y-1,x-1)
#v.displayText(2,0,str(len(m.matrix)))
#v.displayText(3,0,str(len(m.matrix[0])))
#print m.refresh()
#print m.refresh()
#print m.refresh()


while(1):
    v.displayMatrix(m.refresh())
#v.displayMatrix([['s','d','w'],['o','f','e']])
    time.sleep(0.1)


