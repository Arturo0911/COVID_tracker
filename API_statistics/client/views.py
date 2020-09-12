from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User_values
# Create your views here.




# Fetch all data; select * from table_name
def Users(request):
   

    values = User_values.objects.all()
    
    quantity = len(values)
    for x in range(0, quantity):
        print(values[x])

    #print(type(values))
    data = {
        'Nombre': values[0].fullname,
        'Email': values[0].email,
        'User': values[0].username
    }
    
    return JsonResponse(data)

def update(request):
    new_user = User_values.objects.get(id= 1)
    new_user.fullname= "Arturon Negreiros Samanez"
    new_user.save()
    return HttpResponse("updated")