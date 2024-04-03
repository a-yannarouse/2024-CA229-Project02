from django.db import models
from django.urls import reverse

class Area(models.Model):
    area_name = models.CharField(max_length=200)
    area_type = models.CharField(max_length=200)
 
    def __str__(self):
        return self.area_name
        
    def get_absolute_url(self):
        return reverse('areadetail', kwargs={'pk':self.pk})
    
class Attraction(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    attraction_name = models.CharField(max_length=200)
 
    def __str__(self):
        return self.attraction_name