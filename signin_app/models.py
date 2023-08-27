from django.db import models

# Create your models here.
class Signin(models.Model):
    name=models.CharField(default='',max_length=50)
    phone=models.CharField(default='',max_length=11)
    password=models.CharField(default='',max_length=20)
    confirmPassword=models.CharField(default='',max_length=20)

    def __str__(self):
        return self.name
    
    