import math
import matplotlib.pyplot as plot

def f(x):
    return math.sin(x)

xVal = range(-5,6)
yVal = []
for x in xVal:
    yVal.append(f(x))
plot.plot(xVal,yVal)
plot.show()
