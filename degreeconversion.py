import matplotlib.pyplot as plot

def degCon(temp):
    return float(temp)*1.8 + 32

cel = range(-30,31)
far = []
for c in cel:
    far.append(degCon(c))
plot.plot(cel,far)
plot.show()
