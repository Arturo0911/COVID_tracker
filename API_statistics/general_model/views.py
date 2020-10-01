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

    #print(len(Universal_cases.objects.all()))


    countries_cases = Universal_cases.objects.all()
    database_length = len(countries_cases)
    for x in range(0, database_length):
        #print(x)
        #print(type(x))
        sample_country.append({'country':countries_cases[x].country, 'casos': countries_cases[x].cases})
    # print(len(countries_cases))
    #print(sample_country)
    return JsonResponse({'data': sample_country})




def general_page(request):
    # lista_data = []
    _lista_data_ = []
    #global_data = {[]}

    global_properties = Universal_cases.objects.all()
    quantity = len(global_properties)

    
    for x in range (0, quantity):
        

        lista_data = list([global_properties[x].country,global_properties[x].cases])
        _lista_data_.append(lista_data)

    #print(_lista_data_)
    #print(len(_lista_data_))




    return JsonResponse({'data': _lista_data_})
