x1 = [1,2,4,5] #Voltages
x2 = [7,10,12,13] #Currents

result = [1,0.7,0.4,0.2] #Resistances

w = [0.5,0.5] # Weights

data = [0,0]

for i in range(2):
    data[0] = x1[i]
    data[1] = x2[i]
    print(data)