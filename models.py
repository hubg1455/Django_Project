from django.db import models

# Create your models here.

class Position(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class employee(models.Model):
    fullname=models.CharField(max_length=20)
    emp_code = models.CharField(max_length=40)
    mobile_no = models.CharField(max_length=20)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
