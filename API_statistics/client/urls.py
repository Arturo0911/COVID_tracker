from django.urls import path
from . import views


urlpatterns = [
    path('', views.Users, name = "users_page"),
    path('update/', views.update, name = "update_users_"),
]