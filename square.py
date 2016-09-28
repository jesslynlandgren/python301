import matplotlib.pyplot as plot

def f(x):
    return x**2

xVal = range(-100,101)
yVal = []
for x in xVal:
    yVal.append(f(x))
plot.plot(xVal,yVal)
plot.show()
