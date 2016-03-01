#!/usr/bin/python

import sys
import numpy as np
import pylab as pl

for arg in sys.argv:
    print arg

# Use numpy to load the data contained in the file
data = np.loadtxt("/Users/rolf/Python/fakedata.txt")
# plot the first column as x, and second column as y
pl.plot(data)
pl.xlabel('x')
pl.ylabel('y')
pl.xlim(0.0, 10.)
pl.show()
