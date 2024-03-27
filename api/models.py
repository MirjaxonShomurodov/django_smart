from django.db import models

from django.db import models
from django.http import HttpRequest


class Mobile(models.Model):
    price = models.FloatField(max_length=255)
    img_url = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    ram = models.IntegerField()
    memory = models.IntegerField()
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    # release_data = models.DateField()


    def __str__(self):
        return self.name 
    
    def to_dict(self):
        """
        Convert model to dictionary
        """
        return {
            'id': self.id,
            'price': self.price,
            'url': self.img_url,
            'color': self.color,
            'ram': self.ram,
            'memory': self.memory,
            'name': self.name,
            'model': self.model
        }
     
