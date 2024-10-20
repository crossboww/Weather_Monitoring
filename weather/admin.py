# Register your models here.

from django.contrib import admin
from .models import WeatherSummary  # Import your model
from .models import DailyWeatherSummary

# Register the model with the admin site
admin.site.register(WeatherSummary)
admin.site.register(DailyWeatherSummary)
