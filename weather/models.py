# Create your models here.

from django.db import models

class WeatherSummary(models.Model):
    city = models.CharField(max_length=100)
    date = models.DateTimeField()
    main_condition = models.CharField(max_length=50)
    temp = models.FloatField()
    feels_like = models.FloatField()
    alert_triggered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.city} - {self.date}"


class DailyWeatherSummary(models.Model):
    city = models.CharField(max_length=100)
    date = models.DateField()  # Store date only (no time)
    avg_temp = models.FloatField()
    max_temp = models.FloatField()
    min_temp = models.FloatField()
    dominant_condition = models.CharField(max_length=50)  # The most frequent condition

    def __str__(self):
        return f"{self.city} - {self.date} Daily Summary"
