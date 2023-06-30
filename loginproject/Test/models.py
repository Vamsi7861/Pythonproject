from django.db import models

# Create your models here.
class User(models.Model):
     name=models.CharField(max_length=50)
     email=models.EmailField()
     username=models.TextField()
     phone=models.IntegerField(30)
     password=models.CharField(max_length=50)
     img=models.ImageField()
    
     def __str__(self):
        return self.name