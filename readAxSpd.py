#!/usr/bin/python

import sys
from datetime import datetime

import numpy as np
import pylab as pl


def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def getData(d, id):
    d_id = []
    for row in d:
        if row[7-1] == id:
            d_id.append(row)
    print d_id
    return d_id

def getCol(d, col):
    d_id = []
    for row in d:
        d_id.append(row[col])
    #print d_id
    return d_id

# for arg in sys.argv:
#     print arg

#fileName = "539_20150304-5d.axd"
fileName = "./506_dato.axd"

i = 0
sensor = 1
for arg in sys.argv:
    i = i + 1
    if i < 2:
        continue
    
    print i, " ", arg
    if i == 2:
        fileName = arg
    #if i == 3:
    #?    sensor = int(arg)


with open(fileName, "r") as ins:
    array = []
    
    i = 0
    for line in ins:
        i += 1
        if i == 1:
            print "Head: ", line.strip().split()
        elif i == 2:
            print "Skip: ", line.strip().split()
        
        else:
            array.append(line.strip().split())

print len(array)

i = -1
j = -1
day = -1
datoStr = ""
ax_l = 2700 # akselavstand

data = []

# Lag data
for elem in array:
    i += 1
    j = -1
    
    h = float(elem[6])/100
    
    de = [int(elem[0]), # vnr
          float(elem[6])/100, # h_a1
          float(elem[7])/100 - h, # diff ha2
          float(elem[1])/100 - h, # diff h_lf
          float(elem[2])/100 - h # diff h_lt    
         ]
    
    #print "Inn: ", i, elem
    
    print "de:", len(de), de
    if len(de) == 5:
        data.append(de)
        
        #print "add", len(data)

f, axarr = pl.subplots(2, 2)
tid = getCol(data, 0)

#print tid

sensor = -1
for i in range(0, 2):
  for j in range(0, 2):
    sensor += 1
    sigD = getCol(data, sensor)
		
    print i, j
    axarr[i, j].set_title('Sens: %d:%d (%d)' % (j+1, i+1, sensor+1))
    axarr[i, j].grid(color='y')
    axarr[i, j].hist2d(tid, sigD, bins=100)
    #axarr[i, j].set_ylim([0 , 15000]) 

# xmin, xmax = pl.xlim()   # return the current xlim
# pl.xlim( (xmin - (xmax - xmin)/20.0 , xmax + (xmax - xmin)/20.0) )
# ymin, ymax = pl.ylim()   # return the current xlim
#pl.ylim( (0 , 200) )

pl.show()
