from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('', views.Index, name = "index"),
    path('country/', views.Country_selector, name ="country"),
    path('api/', views.Country_get_data, name = "api"),
    path('country_reponse/<str:country>/', views.get_values_to_country, name = "country_response"),
]
#urlpatterns += static(settings)