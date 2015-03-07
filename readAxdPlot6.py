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
  
#pl.Figure()
#thismanager = get_current_fig_manager()
#thismanager.window.wm_geometry("500x500+890+300") #sets original size and position

f, axarr = pl.subplots(2, 2)
tid = getCol(data, 6)

sensor = -1
for i in range(0, 2):
	for j in range(0, 2):
		sensor += 1
		sigD = getCol(data, sensor) 
		
		print i, j
		axarr[i, j].hist2d(tid, sigD, bins=100)      
		axarr[i, j].grid(color='y')
        #axarr[i, j].ylim( (0 , 200) )

# xmin, xmax = pl.xlim()   # return the current xlim
# pl.xlim( (xmin - (xmax - xmin)/20.0 , xmax + (xmax - xmin)/20.0) )
#
# ymin, ymax = pl.ylim()   # return the current xlim
#pl.ylim( (0 , 200) )


pl.show()

