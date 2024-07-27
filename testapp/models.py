from django.db import models

# Create your models here.
#model class defiend
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=50)
    esal=models.FloatField()
    def __str__(self):
        return self.ename
    
