import matplotlib.pyplot as plot

def f(x):
    if x % 2 == 0:
        return -1
    else:
        return 1

xVal = range(-5,6)
yVal = []
for x in xVal:
    yVal.append(f(x))
plot.bar(xVal,yVal)
plot.show()
