import numpy as np
import pandas

#Punto 1
randomArray = np.random.randint(10000, size=100)
medianValue = np.median(randomArray)

#Punto 2
def factorial(n):
    return np.math.factorial(n)

def sumOfSeries(num1, num2):
    arr = np.arange(num1, num2+1)
    print(arr)
    if num1 >= num2:
        return "the first number must be bigger than the second"
    else:
        return np.sum(arr)

#Punto 3
def salariosNetos():
    salariosCSV = pandas.read_csv('./Salarios.csv')
    salariosNetos = salariosCSV.loc[:,'Salario mensual NETO (en tu moneda local)'].to_numpy()
    salariosNetos = salariosNetos.astype(int)
    return "Median: " + str(np.median(salariosNetos)) + " Mean: " + str(np.mean(salariosNetos))




