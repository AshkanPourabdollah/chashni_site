from django.db import models

# Create your models here.
class Orders(models.Model):
    nameOfFood=models.CharField(max_length=50,default='')
    countOfFood=models.IntegerField(default=0)
    priceOfFood=models.IntegerField(default=0)
    nameOfCostumer=models.CharField(max_length=50,default='')
    phoneOfCostumer=models.CharField(max_length=11,default='')
    dateOfReceive=models.CharField(max_length=14,default='')
    forDinnerOrLaunch=models.CharField(max_length=11,default='')

    def __str__(self) -> str:
        return self.nameOfFood+" برای "+self.dateOfReceive + " برای "+self.nameOfCostumer