from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .csv import index, main
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# Modules
import json
from .parser import json_parser
from datetime import datetime as dt


# Modules externals
from general_model.api_functions import api


"""
    # url index
"""

def Index(request): 
    api._create_object()
    while True:
        now_time = dt.now()
        current = now_time.strftime("%H:%M")
        # print(current > "02:50")
        if (current > "02:50"):
            main.Fetch_csv()
            break
        else:
            break
    #print(index.create_data())
    #for x in index.create_data('Ecuador'):
    #    print(x)

    # {'covid':index.create_data('Ecuador')}
    return render(request, 'prediction_model/index.html')

def Link(request):

    return render(request, 'prediction_model/content.html')


def Country_selector(request):  # url country
    country_values = index.get_countries()
   
    return  render(request, 'prediction_model/country.html', {'countries':country_values})

@csrf_exempt
def Country_get_data(request): # url api
    if request.method == 'POST':

        body  = json_parser.json_decoder(request.body)
        #json_decoder = request.body.decode('utf-8')
        #body = json.loads(json_decoder)
        #print(body)
        
        return JsonResponse({'data':'ok'})
    else:
        return JsonResponse({'data':'No hay datos'})
    


def get_values_to_country(request, country): # get country_response
    
    

    return JsonResponse({'cases':index.get_by_month(country)})

def get_values_to_death_by_country(request, country):
    print(index.fetch_deaths_acumulative(country))
    return JsonResponse({'deaths':index.fetch_deaths_acumulative(country)})


def leslie (request):

    return HttpResponse("Te quero mi vida uwuwuuwuwuwuwuwu <3 ")

