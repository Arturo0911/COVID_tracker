import csv
from datetime import datetime
list_results = []
list_country = []
list_chart_regretion = []


def create_data(filter): # Only test filter to parser datetime

    with open('prediction_model/csv/WHO-COVID-19-global-data.csv',encoding='utf-8-sig') as CSVfile:
        reader = csv.DictReader(CSVfile)
        
        for x in reader:
            if(x['Country']== filter):
                list_results.append({'Pais':x['Country'],'Fecha':datetime.strftime(datetime.strptime(x['Date_reported'], '%Y-%m-%d'),'%b %d, %Y'), 'Nuevos_casos':x['New_cases']})

        #print(reader.fieldnames)

    return list_results
    
def get_countries(): # Get Countries from csv file, to send to make select and option tag =>  HTML 

    with open('prediction_model/csv/WHO-COVID-19-global-data.csv',encoding='utf-8-sig') as Country_file:
        country = csv.DictReader(Country_file)

        for x in country:
            if (x['Country'] not in list_country):
                list_country.append(x['Country'])

    return list_country
    
    

def chart_cases(country):
    with open('prediction_model/csv/WHO-COVID-19-global-data.csv',encoding='utf-8-sig') as Cases_file:
        cases_reader = csv.DictReader(Cases_file)

        for i in cases_reader:
            if (i['Country'] == country):
                list_chart_regretion.append({'x': i['Cumulative_cases'], 'y':i['Cumulative_deaths']})
    
    return list_chart_regretion





