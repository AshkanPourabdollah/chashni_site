from django.db import models

# Create your models here.
class Food(models.Model):
    foodName=models.CharField(max_length=30,default='')
    foodPrice=models.IntegerField(default=0)
    foodImage=models.CharField(max_length=30,default='')
    category=models.CharField(max_length=20,default='')
    likesCount=models.IntegerField(default=10)

    def __str__(self):
        return self.foodName
    
class Comments(models.Model):
    personName=models.CharField(max_length=100,default='')
    commentText=models.TextField(max_length=1000,default='')

    def __str__(self):
        return "کاربر : " + self.personName
    
class CommentAbout(models.Model):
    name=models.CharField(max_length=30,default='')
    phone=models.CharField(max_length=11,default='')
    subject=models.CharField(max_length=100,default='')
    text=models.CharField(max_length=1000,default='')

    def __str__(self) -> str:
        return self.name + " : " + self.subject