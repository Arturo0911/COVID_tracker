from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .api_functions import api
# Create your views here.

def index_general(request):
    # api.Generate()
    return HttpResponse("Holis xD")

def general_page(request):

    return HttpResponse("Another page")
