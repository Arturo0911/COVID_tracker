import csv


def Generate():

    with open('prediction_model/csv/WHO-COVID-19-global-data.csv', encoding='utf-8-sig') as Csvfile:
        reader = csv.DictReader(Csvfile)
        