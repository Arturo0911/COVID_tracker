import csv


def _initialize_csv_file():
    with open('prediction_model/csv/WHO-COVID-19-global-data.csv', encoding='utf-8-sig') as CsvFile:
        Reader = csv.DictReader(CsvFile)

    return Reader




def _create_country_list():
    list_country = list() # define a list with countrie's names
    with open('prediction_model/csv/WHO-COVID-19-global-data.csv', encoding='utf-8-sig') as Csvfile:
        reader = csv.DictReader(Csvfile)

        for x in reader:
            if (x[' Country'] not in list_country):
                list_country.append(x[' Country'])
    
    return list_country





def Generate(country):
    
    cases_list = list()
    
    
    with open('prediction_model/csv/WHO-COVID-19-global-data.csv', encoding='utf-8-sig') as Csvfile:
        new_reader = csv.DictReader(Csvfile)

        for x in new_reader:

            if (x[' Country'] == country):
                cases_list.append(int(x[' New_cases']))
                

    return sum(cases_list)



def _create_object():

    list_general = {}

    countries = _create_country_list()

    for x in countries:

        list_general[x] = Generate(x) 

    return list_general
                    
