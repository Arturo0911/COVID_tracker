import csv
from datetime import datetime

# In each list we put function that already involves


list_results = [] # create_data()
list_country = [] # get_countries()
list_chart_regretion = [] #chart_cases()
list_chart_series = [] #time_series_chart()
list_get_by_month = [] # get_by_month()


month_list = [] # get_by_month()
total_list = [] # get_by_month()
country_filter = {} # get_by_month() => this is a object to render in chart js


day_list = [] # get_by_day()
total_list = [] # get_by_day()
object_days = {} # get_by_day()

death_list = [] # fetch_deaths_acumulative()
get_list_by_death = [] # fetch_deaths_acumulative()
total_death_list = [] # fetch_deaths_acumulative()
object_deaths = {} # fetch_deaths_acumulative()


#def main():


"""
    # Only test filter to parser datetime
"""
def create_data(filter):

    with open('prediction_model/csv/WHO-COVID-19-global-data.csv',encoding='utf-8-sig') as CSVfile:
        reader = csv.DictReader(CSVfile)
        
        for x in reader:
            if(x['Country']== filter):
                list_results.append({'Pais':x[' Country'],'Fecha':datetime.strftime(datetime.strptime(x['Date_reported'], '%Y-%m-%d'),'%b %d, %Y'), 'Nuevos_casos':x[' New_cases']})

        #print(reader.fieldnames)

    return list_results


"""
    # Get Countries from csv file, to send to make select and option tag =>  HTML 
"""
def get_countries(): 

    with open('prediction_model/csv/WHO-COVID-19-global-data.csv',encoding='utf-8-sig') as Country_file:
        country = csv.DictReader(Country_file)

        for x in country:
            if (x[' Country'] not in list_country):
                list_country.append(x[' Country'])

    return list_country
    
    
"""
    # This one was to get from csv file data about acumulative cases by all 8 months over 
    # cumulatives deaths.
"""
def chart_cases(country):
    with open('prediction_model/csv/WHO-COVID-19-global-data.csv',encoding='utf-8-sig') as Cases_file:
        cases_reader = csv.DictReader(Cases_file)

        for i in cases_reader:
            if (i[' Country'] == country):
                list_chart_regretion.append({'x': i[' Cumulative_cases'], 'y':i[' Cumulative_deaths']})
    
    return list_chart_regretion



"""
    # this one is to get by day on month or global 
"""
def time_series_chart(): 
    with open('prediction_model/csv/WHO-COVID-19-global-data.csv',encoding='utf-8-sig') as CSVfile:
        reader = csv.DictReader(CSVfile)
        for x in reader:
            if(x[' Country']== 'Ecuador'):
                list_chart_series.append({'Fecha':datetime.strftime(datetime.strptime(x['Date_reported'], '%Y-%m-%d'),'%b'), 'Nuevos_casos':x[' New_cases']})

    return list_chart_series






"""
    # here to filter using country but in chart time series using month to generate chart
    # this one is to fetch cases infected
"""
def get_by_month(country): 
    if(country not in country_filter):
        country_filter.clear()
        total_list.clear()
        month_list.clear()
        list_get_by_month.clear()

        with open('prediction_model/csv/WHO-COVID-19-global-data.csv',encoding='utf-8-sig') as CSVfile:
            reader = csv.DictReader(CSVfile)
            
            for x in reader:
                if(x[' Country'] == country):
                    list_get_by_month.append({'Fecha':datetime.strftime(datetime.strptime(x['Date_reported'], '%Y-%m-%d'),'%b'), 'Nuevos_casos':x[' New_cases']})
                    fecha_append = datetime.strftime(datetime.strptime(x['Date_reported'], '%Y-%m-%d'),'%b')
                    if (fecha_append not in month_list):
                        month_list.append(fecha_append)

        for z in month_list:
            suma = 0
            for a in list_get_by_month:
                
                if (a['Fecha']==z):
                    
                    suma = suma + int(a['Nuevos_casos'])
        
            total_list.append({'Mes':z, 'casos':suma})
        country_filter[country] = total_list
        return country_filter[country]
    else:
        return country_filter[country]






def fetch_deaths_acumulative(country):
    if(country not in object_deaths):
        object_deaths.clear()
        total_death_list.clear() # sumatory about cases
        death_list.clear() # this is to fetch months per cases
        get_list_by_death.clear() # to fetch all data

        with open('prediction_model/csv/WHO-COVID-19-global-data.csv',encoding='utf-8-sig') as CSVfile:
            reader = csv.DictReader(CSVfile)
            
            for x in reader:
                if(x[' Country'] == country):
                    get_list_by_death.append({'Fecha':datetime.strftime(datetime.strptime(x['Date_reported'], '%Y-%m-%d'),'%b'), 'Muertes':x[' New_deaths']})
                    fecha_append = datetime.strftime(datetime.strptime(x['Date_reported'], '%Y-%m-%d'),'%b')
                    if (fecha_append not in death_list):
                        death_list.append(fecha_append)

        for z in death_list:
            suma = 0
            for a in get_list_by_death:
                
                if (a['Fecha']==z):
                    
                    suma = suma + int(a['Muertes'])
        
            total_death_list.append({'Mes':z, 'muertes':suma})
        object_deaths[country] = total_death_list
        return object_deaths[country]
    else:
        return object_deaths[country]