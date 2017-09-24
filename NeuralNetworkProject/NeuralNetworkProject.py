import numpy

x1 = numpy.array([1,2,4,5]) #Voltages
x2 = numpy.array([7,10,12,13]) #Currents
MAX_CURRENT = 16
MAX_VOLTAGE = 5
a = 1 #Learning Rate

result = numpy.array([1,0.7,0.4,0.2]) #Resistances

w = numpy.array([0.5,0.5]) # Weights

data = numpy.array([0,0])


def print_train_data():
    for i in range(len(x1)):
        data[0] = x1[i]
        data[1] = x2[i]
        print(data)

def run_network_once(y1, y2):
    y1=y1/MAX_VOLTAGE
    y2=y2/MAX_CURRENT
    output = numpy.array([0.0,0.0])
    output[0] =  (float)(y1*w[0])
    output[1] =  (float)(y2*w[1])
    return (float)(output[0]+output[1])

print(run_network_once(1,7))

def train_once(d1,d2, r1,w1):
    for i in range(len(result)):
        data[0] = d1[i]
        data[1] = d2[i]
        w2 = a*(r1[i]-run_network_once(d1[i],d2[i]))*data
        w1=w1+w2
    print(w1);
    return w1

w=train_once=(x1,x2,result,w)
print(run_network_once(1,7))