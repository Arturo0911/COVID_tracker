from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .api_functions import api
from django.core.serializers import serialize
# Create your views here.
import json

# Import models
from .models import Universal_cases



def index_general(request):
    sample_country = []
    
    # print(api._create_object())
    # return JsonResponse({'data': values})
    # values = [{'value': 'Reactjs'}]
    # api._create_object()

    print(len(Universal_cases.objects.all()))


    countries_cases = Universal_cases.objects.all()
    database_length = len(countries_cases)
    for x in range(0, database_length):
        #print(x)
        #print(type(x))
        sample_country.append({'country':countries_cases[x].country, 'casos': countries_cases[x].cases})
    # print(len(countries_cases))
    


    
    """sample_data = [{'Userid':1 ,'id':1, 'title':'Hola ¿Cómo vas?'},
    {'Userid':2 ,'id':2,'title':'Hola ¿Cómo vas?'}]
    # json_serialize = serialize('json',sample_data)
    """


    return JsonResponse({'data': sample_country})

def general_page(request):

    return HttpResponse("Another page")
