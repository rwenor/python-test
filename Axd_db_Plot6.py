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
    # print d_id
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
#fileName = "/Users/rolf/Dropbox/python/506_dato.axd"
fileName = "test.axd"

i = 0
sensor = 1
for arg in sys.argv:
    i = i + 1
    if i < 2:
        continue
    
    print i, " ", arg
    if i == 2:
        fileName = arg
    if i == 3:
        sensor = int(arg)


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
            #print line
            array.append(line.strip().split())



print len(array)

i = -1
j = -1
day = -1
datoStr = ""
ax_l = 2700 # akselavstand

data = []

for elem in array:
    i += 1
    j = -1
    de = []
    
    #print "Inn: ", i, elem
    
    for itm in elem:
        j += 1
        
        try:
              if j <> 4 and j <> 6 and j <> 7:
                   itm = float(itm)
                   de.append(itm)
              
              if j == 6:  # Dato: oker med 1 for hver NY dag
                   if datoStr <> itm:
                       day += 1
                       #print day, datoStr
                       datoStr = itm
              
              if j == 7: # Tid: Legger pa dag frakson
                   # itm = float(itm)
                   ts = 0.0
                   for et in itm.split(":"):
                       #print "*", et
                       ts = ts*60 + float(et)
                   
                   de.append(day + ts/3600.0/24)
              
              if j == 4:
                     #print itm
                     de.append(itm)
              
              if j == 8: # Akselavstand 1
                     #print itm
                     ax_l = int(itm)
                     de.append(ax_l)
        
        except:
            e = sys.exc_info()[0]
            print "Error: %s" % e
            print "Fail:", itm
            pass
    
    #print "de:", len(de), de
    if len(de) >= 7:
    #if len(de) > 7 and ax_l > 900 and ax_l < 1100 :  # sykler
        data.append(de)
        
        #print "add", len(data)

f, axarr = pl.subplots(2, 2)
tid = getCol(data, 6)

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
#    axarr[i, j].set_ylim([0 , 1000]) 

# xmin, xmax = pl.xlim()   # return the current xlim
# pl.xlim( (xmin - (xmax - xmin)/20.0 , xmax + (xmax - xmin)/20.0) )
# ymin, ymax = pl.ylim()   # return the current xlim
#pl.ylim( (0 , 200) )

pl.show()
