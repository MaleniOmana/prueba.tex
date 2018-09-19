y=[4,15,24,56]
print "El primer es", y[0], "ultimo", y[3]

print range(7)

for i in range(3):
    print "Hola"
    print "Maleni"
print "Hasta luego"

y.append("Bye")
print y


x=[100]
for i in range(100):
    x.append(1.01*x[i])
print x

def iteracion(100,50,lafuncion):

#serie de fibonacci
# x=[1,1]
# for i in range(10):
#     x.append(x[i]+x[i+1])
# print x

import matplotlib.pyplot as plt
plt.plot(x)
plt.show(x)





def suma (x,y):
    return x+y

suma (2,3)

def producto(x,y):
    return x*y

producto(2,3)

def funcion(x,y,f):
    return f(x,y)

funcion(2,3,producto)

x=[100]
for i in range(50):
    x.append(1.01*x[i])
print x

def lafuncion(x):
    return 1.01*x


def iteracion(inicial,iteraciones,lafuncion):
    x=[inicial]
    for i in range(iteraciones):
        x.append(lafuncion(x[i]))
    return x
import math
valores=iteracion(5,40,math.cos)
print valores

import matplotlib.pyplot as plt
plt.plot(valores)
plt.show(valores)


import numpy as np
def diagrama(f,x0,it):
    x=[x0]
    y=[x0]
    s=np.arange(0, 1, 0.01)
    for i in range(it):
        x.append(x[2*i])
        x.append(f(x[2*i]))
        y.append(f(y[2*i]))
        y.append(f(y[2*i]))
    plt.plot(x, y, color= 'red')
    plt.plot(s, f(s))
    plt.plot(s, s, color='black')
    plt.show()

def logistica(x):
    return 4*x*(1-x)

diagrama(logistica, 0.01, 10000)


                 
    
