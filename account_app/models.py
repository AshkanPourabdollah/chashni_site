from django.db import models

# Create your models here.
class Account(models.Model):
    name=models.CharField(max_length=50,default='')
    phone=models.CharField(max_length=11,default='')
    password=models.CharField(max_length=20,default='')

    def __str__(self):
        return self.name