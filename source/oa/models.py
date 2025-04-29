from django.db import models
from django.utils import timezone
# Create your models here.

class Sensors(models.Model):
    timestamp = models.DateTimeField()
    waterLevel = models.CharField(max_length=10)
    thermo = models.FloatField(default=0)
    tds = models.FloatField(default=0)
    pH = models.FloatField(default=0)
    def __str__(self):
        now = self.timestamp
        date_time = now.strftime("%Y-%m-%d %H:%M:%S") # Year-Month-Day Hours:Minutes:Seconds
        return date_time
