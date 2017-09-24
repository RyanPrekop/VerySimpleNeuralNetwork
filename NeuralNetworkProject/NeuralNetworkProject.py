import numpy

a = 0.01 #Learning Rate

x1 = numpy.array(    [  1,    3, 6,  10, 15, 18, 20,    3,  4,   5,    7]) #Voltages
x2 = numpy.array(    [0.5,  1.5, 2, 2.5,  3,  2,  2,  0.1,  1,   2,    4]) #Currents
result = numpy.array([  2,    2, 3,   4,  5,  9, 10,   30,  4, 2.5, 1.75]) #Resistances

MAX_VOLTAGE = max(x1)   #Find maximum Voltage
MAX_CURRENT = max(x2)   #Find maximum Current
MAX_RESISTANCE = max(result)    #Find maximum Resistance

absolute_max = max([MAX_VOLTAGE, MAX_CURRENT, MAX_RESISTANCE])  #Find overall maximum
print('Absolute Maximum:')
print(absolute_max);
print('-----------Start of Program-------------')

xs1 = x1/absolute_max   #Scale Voltages by absolute maximum
xs2 = x1/absolute_max   #Scale Currents by absolute maximum
results = result/absolute_max   #Scale Resistance by absolute maximum

w = numpy.array([0.5,0.5]) # Weights

data = numpy.array([0.0,0.0]) #Temporary Storage Location


def print_train_data():
    for i in range(len(x1)):
        data[0] = xs1[i]
        data[1] = xs2[i]
        print(data)

def run_network_once(y1, y2):
    output = numpy.array([0.0,0.0])
    output[0] =  (float)(y1*w[0])
    output[1] =  (float)(y2*w[1])
    return (float)(output[0]+output[1])

def train_once(d1,d2, r1,w1):
    for i in range(len(result)):
        data[0] = (float)(d1[i])
        data[1] = (float)(d2[i])
        print('-----------------Begin------------------')
        print(data)
        predict = run_network_once(d1[i],d2[i])
        print(predict)
        w2 = a*(predict-r1[i])*data
        print(w2)
        w1 = numpy.add(w1,w2)
        print(w1)
        print('------------------End-------------------')
    return w1

print(run_network_once(3/absolute_max,1.5/absolute_max))
w=train_once(xs1,xs2,results,w)
print(run_network_once(3/absolute_max,1.5/absolute_max))