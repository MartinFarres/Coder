import pandas as pd

#Punto 1
summerOlympicCSV = pd.read_csv("./Summer-Olympic-medals-1976-to-2008.csv")
summerOlympicYears = pd.DatetimeIndex(summerOlympicCSV['Year'])
seriesSummerOlympic = pd.Series(summerOlympicYears.values, index=summerOlympicYears)


#Punto 2
olympicAthlete = pd.DataFrame({'Name': summerOlympicCSV['Athlete']})
olympicAthlete[['Name', 'Surname']] = olympicAthlete['Name'].str.split(',',1,expand=True)

#Punto 3
def dataSummary(keyValue):
    columnNames = summerOlympicCSV.columns.values
    for col in columnNames:
        if col == keyValue:
            return summerOlympicCSV[keyValue].describe()
            break
    return keyValue + ' is not a column name value. Try: ' + ', '.join(columnNames)

#Punto 4
def menByYear():
    df = summerOlympicCSV[['Year', 'Event_gender']]
    return df[df['Event_gender'] == 'M'].groupby('Year').count()
