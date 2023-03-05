from django.db import models
from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()   
    image_url = models.CharField(max_length=2083)
    price = models.DecimalField(max_digits=6, decimal_places=2)
   
    


class Offer(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

    def __str__(self):
        return self.title


    






