from django.db import models

class Order(models.Model):
    academic_level = models.CharField(max_length=200)
    service_type = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    powerpoint_slides = models.IntegerField() 
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

