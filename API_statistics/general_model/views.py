from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index_general(request):
    return HttpResponse("Holis xD")