import csv



def _create_country_list():
    list_country = list() # define a list with countrie's names
    with open('prediction_model/csv/WHO-COVID-19-global-data.csv', encoding='utf-8-sig') as Csvfile:
        reader = csv.DictReader(Csvfile)

        for x in reader:
            if (x[' Country'] not in list_country):
                list_country.append(x[' Country'])
    
    return list_country





def Generate():
    
    cases_list = list()
    
    list_general = {}
    countries = _create_country_list()
    #print(countries)
    with open('prediction_model/csv/WHO-COVID-19-global-data.csv', encoding='utf-8-sig') as Csvfile:
        new_reader = csv.DictReader(Csvfile)

        for x in countries:
            #print(x)
            for y in new_reader:
                #print(y)
                if (x == y[' Country']):
                    print(x)
                    cases_list.append(int(y[' New_cases']))
                    #break
                    #print(x, y[' New_cases'])
                    #cases_list.append(int(y[' New_cases']))
                #print(x, cases_list)
                #list_general[x] = sum(cases_list)
                #cases_list.clear()

            #print(cases_list)    
    #print(list_general)
    
                    
