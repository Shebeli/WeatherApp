from django.db import models

class CityCord(models.Model): 
    name = models.CharField()
    country = models.CharField(max_length=2)
    lat = models.DecimalField("latitude")
    lon = models.DecimalField("longitude")


