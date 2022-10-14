from django.db import models

# Create your models here.
'''
uid creates a random id for the model everytime.
UUID, Universal Unique Identifier, is a python library that helps in generating random objects of 128 bits as ids. 
It provides the uniqueness as it generates ids on the basis of time, Computer hardware (MAC etc.). 
Universally unique identifiers are a good alternative to AutoField for primary_key. 
'''



class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

