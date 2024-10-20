from django.core.management.base import BaseCommand
from weather.views import fetch_weather_data

class Command(BaseCommand):
    help = 'Fetches weather data from OpenWeatherMap'

    def add_arguments(self, parser):
        parser.add_argument('--unit', type=str, help="Choose Celsius or Fahrenheit", default='Celsius')

    def handle(self, *args, **kwargs):
        unit = kwargs['unit']
        fetch_weather_data(temp_unit=unit)
        self.stdout.write(self.style.SUCCESS(f'Successfully fetched weather data in {unit}'))
