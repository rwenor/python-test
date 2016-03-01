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

# Use numpy to load the data contained in the file
# data = np.loadtxt("/Users/rolf/Python/fakedata.txt")
# # plot the first column as x, and second column as y
# pl.plot(data)
# pl.xlabel('x')
# pl.ylabel('y')
# pl.xlim(0.0, 10.)
# pl.show()


#fileName = "539_20150304-5d.axd"
fileName = "/Users/rolf/Dropbox/python/506_dato.axd"

i = 0
for arg in sys.argv:
    i = i + 1
    if i < 2:
        continue
        
    print i, " ", arg
    fileName = arg




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
            #print i
            array.append(line.strip().split())
            #print array[(i/2)-1]    
        
        
#print array

i = -1
j = -1
day = -1
datoStr = ""

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
                   
              if j == 6:
                   if datoStr <> itm:
                       day += 1
                       #print day, datoStr
                       datoStr = itm
                   #print "?", itm
                   # itm = float(itm)
                   #dt = datetime.strptime(itm, "%d.%m.%Y 00:00")
                   #print 1
                   #de.append(day)
                   #print "D", dt

              if j == 7:
                   # itm = float(itm)
                   ts = 0.0
                   for et in itm.split(":"):
                       #print "*", et
                       ts = ts*60 + float(et)
                       
                   de.append(day + ts/3600.0/24)
                   
                      
                   
              if j == 4:
                      #print itm
                      de.append(itm)
              
              
        except: 
            e = sys.exc_info()[0]
            print "Error: %s" % e 
            print "Fail:", itm           
            pass
     
    #print "de:", len(de), de 
    if len(de) == 7:          
        data.append(de)
        #print "add", len(data)
  
#print data  
sigD = getCol(data, 1) 
tid = getCol(data, 6)
#print "col 0:", sigD 
#print "col 6:", tid 
      
      
pl.hist2d(tid, sigD, bins=100)      
# H, xedges, yedges = np.histogram2d(sigD, tid) #, bins=(xedges, yedges))
# im = pl.imshow(H, interpolation='nearest', origin='low',
#                 extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
#pl.plot( sigD, "ko")
#pl.hist( sigD, bins = 100)

pl.ylabel('Sig')
pl.xlabel('Tid')

# xmin, xmax = pl.xlim()   # return the current xlim
# pl.xlim( (xmin - (xmax - xmin)/20.0 , xmax + (xmax - xmin)/20.0) )
#
# ymin, ymax = pl.ylim()   # return the current xlim
#pl.ylim( (0 , 200) )

pl.show()

# #print array
# print data
#
# d_fg1 = getData(data, "fg1")
# d_fs1 = getData(data, "fs1")
#
#
# print "col 1 fg1: ", getCol(d_fg1, 1)
#
# #m,b = pl.polyfit(getCol(d_fg1,1), getCol(d_fg1,3), 1)
# #pl.plot( getCol(d_fg1,1), getCol(d_fg1,3), m*getCol(d_fg1,1) + b, "yo")
# pl.plot( getCol(d_fg1,1), getCol(d_fg1,3), "yo")
#
# pl.plot( getCol(d_fs1,1), getCol(d_fs1,3), "ko")
#
# pl.ylabel('Puls')
# pl.xlabel('Tid (sec)')
#
# xmin, xmax = pl.xlim()   # return the current xlim
# pl.xlim( (xmin - (xmax - xmin)/20.0 , xmax + (xmax - xmin)/20.0) )
#
# ymin, ymax = pl.ylim()   # return the current xlim
# pl.ylim( (ymin - (ymax - ymin)/20.0 , ymax + (ymax - ymin)/20.0) )
#
# pl.show()
#
# # ***
#
# pl.plot( [ 3600/x for x in getCol(d_fg1,1) ], getCol(d_fg1,3), "yo")
# pl.plot( [ 3600/x for x in getCol(d_fs1,1) ], getCol(d_fs1,3), "ko")
#
# pl.ylabel('Puls')
# pl.xlabel('Km/t')
#
# xmin, xmax = pl.xlim()   # return the current xlim
# pl.xlim( (xmin - (xmax - xmin)/20.0 , xmax + (xmax - xmin)/20.0) )
#
# ymin, ymax = pl.ylim()   # return the current xlim
# pl.ylim( (ymin - (ymax - ymin)/20.0 , ymax + (ymax - ymin)/20.0) )
#
# pl.show()



#d_fg2 = getData(data, "fg2")
#d_fs2 = getData(data, "fs2")

# print "col 1 fg1: ", getCol(d_fg1, 1)
#
# pl.plot( getCol(d_fg2,0), getCol(d_fg2,1), "yo")
# pl.plot( getCol(d_fs2,0), getCol(d_fs2,1), "ko")
#
# pl.ylabel('Tid')
# pl.xlabel('Runde')
# # pl.xlim(0.0, 10.)
# pl.show()
