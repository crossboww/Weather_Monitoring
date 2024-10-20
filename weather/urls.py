from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('fetch-weather/', views.fetch_weather_view, name='fetch_weather'),
    path('weather-summary/', views.weather_summary_view, name='weather_summary'),
    

]
