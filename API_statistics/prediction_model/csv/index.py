import csv
from datetime import datetime
list_results = []
def create_data(filter):


    with open('prediction_model/csv/WHO-COVID-19-global-data.csv',encoding='utf-8-sig') as CSVfile:
        reader = csv.DictReader(CSVfile)
        
        for x in reader:
            if(x['Country']== filter):
                list_results.append({'Pais':x['Country'],'Fecha':datetime.strftime(datetime.strptime(x['Date_reported'], '%Y-%m-%d'),'%b %d, %Y'), 'Nuevos_casos':x['New_cases']})

        #print(reader.fieldnames)

    return list_results
    

    
    







