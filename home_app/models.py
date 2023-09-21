from django.db import models

# Create your models here.
class Food(models.Model):
    foodName=models.CharField(max_length=30,default='')
    foodPrice=models.IntegerField(default=0)
    foodImage=models.ImageField(upload_to="foodImages")
    category=models.CharField(max_length=20,default='')
    likesCount=models.IntegerField(default=10)
    isExist=models.BooleanField(default=True)

    def __str__(self):
        if self.isExist:
            return self.foodName
        else:
            return self.foodName+" موجود نیست "
    



class Comments(models.Model):
    personName=models.CharField(max_length=100,default='')
    commentText=models.TextField(max_length=1000,default='')
    showing=models.BooleanField(default=False)
    category=models.ForeignKey(Food,on_delete=models.CASCADE,default='')

    def __str__(self):
        if(self.showing == False):
            return "نظر تایید نشده دارید"
        return "کاربر : " + self.personName + " / غذا : "+str(self.category)
    




class CommentAbout(models.Model):
    name=models.CharField(max_length=30,default='')
    phone=models.CharField(max_length=11,default='')
    subject=models.CharField(max_length=100,default='')
    text=models.TextField(max_length=1000,default='')

    def __str__(self) -> str:
        return self.name + " : " + self.subject