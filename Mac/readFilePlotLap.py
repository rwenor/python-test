#!/usr/bin/python

import sys
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
    print d_id
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


fileName = "rwe2015-02-28.lap"

with open(fileName, "r") as ins:
    array = []
    
    i = 0
    for line in ins:
        i += 1
        if i % 2 <> 0:
            array.append(line.strip().split())
        else:
            #print i
            array[(i/2)-1].extend(line.strip().split())
            #print array[(i/2)-1]    
        
i = -1
j = -1

data = []

for elem in array:
    i += 1
    j = -1
    de = []
    
    print "Inn: ", i, elem
    
    for itm in elem:
        j += 1
        
        try:
              if j <> 1 and j <> 7:
                   itm = float(itm)
                   de.append(itm)
                   
              if j == 1:
                   # itm = float(itm)
                   ts = 0.0
                   for et in itm.split(":"):
                       # print "*", et
                       ts = ts*60 + float(et)
                       
                   de.append(ts)   
                   
              if j == 7:
                      print itm
                      de.append(itm)
              
              
        except:             
            pass
     
    print "de:", len(de), de 
    if len(de) == 7 and ts < 310 :          
        data.append(de)
            
#print array
print data

d_fg1 = getData(data, "fg1")
d_fs1 = getData(data, "fs1")


print "col 1 fg1: ", getCol(d_fg1, 1)

#m,b = pl.polyfit(getCol(d_fg1,1), getCol(d_fg1,3), 1) 
#pl.plot( getCol(d_fg1,1), getCol(d_fg1,3), m*getCol(d_fg1,1) + b, "yo")
pl.plot( getCol(d_fg1,1), getCol(d_fg1,3), "yo")

pl.plot( getCol(d_fs1,1), getCol(d_fs1,3), "ko")

pl.ylabel('Puls')
pl.xlabel('Tid (sec)')
# pl.xlim(0.0, 10.)
pl.show()

d_fg2 = getData(data, "fg2")
d_fs2 = getData(data, "fs2")

# print "col 1 fg1: ", getCol(d_fg1, 1)
#
# pl.plot( getCol(d_fg2,0), getCol(d_fg2,1), "yo")
# pl.plot( getCol(d_fs2,0), getCol(d_fs2,1), "ko")
#
# pl.ylabel('Tid')
# pl.xlabel('Runde')
# # pl.xlim(0.0, 10.)
# pl.show()
