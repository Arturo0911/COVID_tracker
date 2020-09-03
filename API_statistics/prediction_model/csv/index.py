import csv

with open('WHO-COVID-19-global-data.csv') as CSVfile:
    reader = csv.DictReader(CSVfile)
    print(reader.fieldnames)
    #for x in reader:
        #print(x)

    #print("Country code     Nuevos casos        Casos acumulados        nuevas muertes      Muertes acumuladas")
    #for x in reader:
        #print("Country code     Nuevos casos        Casos acumulados        nuevas muertes      Muertes acumuladas")
        #if(x['Country'] == 'Ecuador'):
            
            
            #print(x['Date_reported'], x['Country_code'],"               ", x['New_cases'],"                 ",x['Cumulative_cases'],"                            ", x['New_deaths'],"                            ",x['Cumulative_deaths'])







