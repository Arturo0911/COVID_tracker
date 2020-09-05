import csv
from datetime import datetime
list_results = [] # create_data()
list_country = [] # get_countries()
list_chart_regretion = [] #chart_cases()
list_chart_series = [] #time_series_chart()
list_get_by_month = [] # get_by_month()


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



def time_series_chart(): # this one is to get by day on month or global 
    with open('prediction_model/csv/WHO-COVID-19-global-data.csv',encoding='utf-8-sig') as CSVfile:
        reader = csv.DictReader(CSVfile)
        for x in reader:
            if(x['Country']== 'Ecuador'):
                list_chart_series.append({'Fecha':datetime.strftime(datetime.strptime(x['Date_reported'], '%Y-%m-%d'),'%b'), 'Nuevos_casos':x['New_cases']})

    return list_chart_series

def get_by_month(country): # here to filter using country but in chart time series using month to generate chart

    month_list = []
    total_list = []

    with open('prediction_model/csv/WHO-COVID-19-global-data.csv',encoding='utf-8-sig') as CSVfile:
        reader = csv.DictReader(CSVfile)
        for x in reader:
            if(x['Country'] == country):
                list_get_by_month.append({'Fecha':datetime.strftime(datetime.strptime(x['Date_reported'], '%Y-%m-%d'),'%b'), 'Nuevos_casos':x['New_cases']})
                fecha_append = datetime.strftime(datetime.strptime(x['Date_reported'], '%Y-%m-%d'),'%b')
                if (fecha_append not in month_list):
                    month_list.append(fecha_append)

    for z in month_list:
        suma = 0
        for a in list_get_by_month:
            #print(suma)
            if (a['Fecha']==z):
                
                suma = suma + int(a['Nuevos_casos'])
    
        total_list.append({'Mes':z, 'Casos_by_month':suma})

    return total_list


def get_by_day(country, month):
    day_list = []
    total_list = []
    object_days = {}
    with open('prediction_model/csv/WHO-COVID-19-global-data.csv',encoding='utf-8-sig') as CSVfile:
        reader = csv.DictReader(CSVfile)

        for x in reader:
            if (x['Country'] == country):
                day_list.append({'Fecha':datetime.strftime(datetime.strptime(x['Date_reported'], '%Y-%m-%d'),'%b'), 'Nuevos_casos':x['New_cases']})
        for y in day_list:
            if (y['Fecha']== month):
                total_list.append(y['Nuevos_casos'])
                #print(y['Nuevos_casos'])
    quantity_days = len(total_list)

    for i in range(1, quantity_days+1):
        object_days[i] = total_list[i-1]
    
    return object_days




