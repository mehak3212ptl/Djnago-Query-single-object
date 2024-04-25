from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=100)
    City= models.CharField(max_length=100)
    Email=models.EmailField()
    Contact= models.IntegerField()
    def __str__(self):
        return self.Name

