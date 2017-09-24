import numpy

x1 = numpy.array([1,2,4,5]) #Voltages
x2 = numpy.array([7,10,12,13]) #Currents

result = numpy.array([1,0.7,0.4,0.2]) #Resistances

w = numpy.array([0.5,0.5]) # Weights

data = numpy.array([0,0])

for i in range(len(x1)):
    data[0] = x1[i]
    data[1] = x2[i]
    print(data)