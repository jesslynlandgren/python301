import matplotlib.pyplot as plot

def f(x):
    return x+1

xVal = range(-3,4)
yVal = []
for x in xVal:
    yVal.append(f(x))
plot.plot(xVal,yVal)
plot.show()
