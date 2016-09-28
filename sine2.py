from numpy import arange
import math
import matplotlib.pyplot as plot

def f(x):
    return math.sin(x)

xVal = arange(-5,6,0.1)
yVal = []
for x in xVal:
    yVal.append(f(x))
plot.plot(xVal,yVal)
plot.show()
