from django.db import models

class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=32)
    esal = models.FloatField()
    eexp = models.FloatField()
