from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .api_functions import api
# Create your views here.
import json



def index_general(request):
    return JsonResponse(api._create_object())

def general_page(request):

    return HttpResponse("Another page")
