from django.db import models

class student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField()
    email = models.EmailField() 

class car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=80)
    
def __str__(self):
    return self.car_name
