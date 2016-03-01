#!/usr/bin/python

import sys
import numpy as np
import pylab as pl


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
    if len(de) == 7:          
        data.append(de)
            
#print array
print data

pl.plot(data)
pl.xlabel('x')
pl.ylabel('y')
pl.xlim(0.0, 10.)
pl.show()
