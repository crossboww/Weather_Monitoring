# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.utils import timezone
from datetime import datetime
from .models import WeatherSummary, DailyWeatherSummary
from django.db.models import Avg, Max, Min, Count
from collections import Counter
from .models import WeatherSummary


API_KEY = 'dfc6b42d7c02f145b26873765307b644'
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad","Navsari"]

# Threshold settings
THRESHOLDS = {
    'temp': 35,  # Trigger alert if temperature exceeds 35°C
    'main_condition': 'Rain'  # Trigger alert if main condition is 'Rain'
}

def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15

def kelvin_to_fahrenheit(temp_kelvin):
    return (temp_kelvin - 273.15) * 9/5 + 32

def fetch_weather_data(temp_unit='Celsius'):
    for city in CITIES:
        # Use 'units=metric' for Celsius or 'units=imperial' for Fahrenheit
        units = 'metric' if temp_unit == 'Celsius' else 'imperial'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"
        response = requests.get(url).json()

        if response.get("main"):
            # Temperatures are already in the correct unit based on the API request
            temp = response["main"]["temp"]
            feels_like = response["main"]["feels_like"]
            main_condition = response["weather"][0]["main"]
            timestamp = response["dt"]
            date = timezone.make_aware(datetime.utcfromtimestamp(timestamp))


            # Check for threshold breaches
            alert_triggered = False
            if temp > THRESHOLDS['temp']:
                alert_triggered = True
                print(f"Alert: {city} temperature {temp}°C exceeds {THRESHOLDS['temp']}°C!")

            if main_condition == THRESHOLDS['main_condition']:
                alert_triggered = True
                print(f"Alert: {city} has {main_condition} which matches alert condition!")


            # Save weather data
            WeatherSummary.objects.create(
                city=city,
                date=date,
                main_condition=main_condition,
                temp=temp,
                feels_like=feels_like
            )
            print(f"Weather data saved for {city}: {temp}° {temp_unit}")

def calculate_daily_summary():
    today = timezone.now().date()
    for city in CITIES:
        # Query all weather records for the current city and date
        weather_data = WeatherSummary.objects.filter(city=city, date__date=today)

        if weather_data.exists():
            avg_temp = weather_data.aggregate(Avg('temp'))['temp__avg']
            max_temp = weather_data.aggregate(Max('temp'))['temp__max']
            min_temp = weather_data.aggregate(Min('temp'))['temp__min']

            # Calculate dominant weather condition
            conditions = weather_data.values_list('main_condition', flat=True)
            condition_counts = Counter(conditions)
            dominant_condition = condition_counts.most_common(1)[0][0]

            # Store the daily summary in the database
            DailyWeatherSummary.objects.create(
                city=city,
                date=today,
                avg_temp=avg_temp,
                max_temp=max_temp,
                min_temp=min_temp,
                dominant_condition=dominant_condition
            )
            print(f"Daily summary saved for {city} on {today}: Avg Temp {avg_temp}°C")



def fetch_weather_view(request):
    fetch_weather_data()
    calculate_daily_summary()
    return HttpResponse("Weather data fetched successfully!")


def weather_summary_view(request):
    summaries = DailyWeatherSummary.objects.all()

    # Ensure these are lists of values
    dates = [summary.date.strftime("%Y-%m-%d") for summary in summaries]
    avg_temps = [summary.avg_temp for summary in summaries]

    context = {
        'dates': dates,
        'avg_temps': avg_temps,
        'summaries': summaries,
    }
    return render(request, 'weather/weather_summary.html', context)


