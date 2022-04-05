import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

mpl.style.use("bmh")

#Punto 1
data = pd.read_csv("visualizaciones-data.csv")
def dataSummary(keyValue = 'blank'):
    columnNames = data.columns.values
    for col in columnNames:
        if col == keyValue:
            return data[keyValue].describe()
            break
    return keyValue + ' is not a column name value. Try: ' + ', '.join(columnNames)

#Punto 2
def histogram():
    salaryHist = data["Salary"].values.flatten()
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(salaryHist, bins=20, label='Frecuencia de salarios')
    ax.set_title('Histograma - Salarios')
    ax.set_xlabel('Rangos de Salarios')
    ax.set_ylabel('Frecuencia Absoluta')
    ax.legend()
    plt.show()

#Punto 3
def graphViolin():
    ax = sns.catplot(data=data, kind='violin', y='Salary', x='Department', hue='Sex', split=True, height=5, aspect=2)
    ax.set(xlabel='Departamento', ylabel='Salario')
    ax.fig.subplots_adjust(top=.9)
    ax.fig.suptitle('Distribucion salarial')
    plt.show()

#Punto 4
def contratacionesAnuales():
    data['Year'] = pd.to_datetime(data['DateofHire']).dt.year
    group = data[['Year', 'EmpID']].groupby('Year').count()
    x = group.index
    y = group['EmpID']
    fig, ax = plt.subplots(figsize=(12,4))
    ax.plot(x, y, label='Contratacion anuales')
    ax.set_xlabel('Año')
    ax.set_ylabel('Contrataciones')
    ax.set_title('Serie de tiempo - Contratacion')
    ax.legend()
    plt.show()