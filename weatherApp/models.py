from django.contrib.auth.models import User
from django.db import models

class CardCityWeather(models.Model):
    city_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = 'WeatherCard'
        verbose_name_plural = 'WeatherCards'
