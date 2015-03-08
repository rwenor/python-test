import sys
import numpy as np
import pylab as pl

i = 0
for arg in sys.argv:
    i = i + 1

    if i < 2:
        continue
        
    print i, " ", arg
    
    # Use numpy to load the data contained in the file
    data = np.loadtxt(arg)
    # plot the first column as x, and second column as y
    pl.plot(data)
    
    
pl.xlabel('x')
pl.ylabel('y')
pl.xlim(0.0, 10.)
pl.show()
