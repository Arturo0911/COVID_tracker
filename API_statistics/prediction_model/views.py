from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .csv import index
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# Modules
import json
from .parser import json_parser



def Index(request): # url index

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
    


def get_values_to_country(request, country,filter): # get country_response
    #print(filter)
    
    

    #print(index.get_by_month('Peru'))
    index.get_by_day(country, 'Aug')
    cases_ = {'cases':index.get_by_day(country, 'Aug')}
    # cases_ = {'cases':index.chart_cases(country)}



    #print(cases_)
    return JsonResponse(cases_)


    


