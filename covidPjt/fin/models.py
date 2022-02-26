from django.db import models
from django.forms import CharField


# Create your models here.

class Covid(models.Model):
    date= models.CharField(max_length=100, primary_key=True)
    deathCnt = models.CharField(max_length=100, default=0)
    decideCnt= models.CharField(max_length=100, default=0)

    def __str__(self):
        return self.date
