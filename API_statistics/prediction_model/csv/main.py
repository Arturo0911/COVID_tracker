from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt


# Using scraping to fetch data from covid page official
def Fetch_csv():
    with urlopen("https://covid19.who.int/WHO-COVID-19-global-data.csv") as f:
        html = f.read().decode('utf-8')
        outdir = open("prediction_model/csv/WHO-COVID-19-global-data.csv", "w")
        outdir.write(html)
        outdir.close()
    return True
        
