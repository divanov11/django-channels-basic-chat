from pyexpat import model
from statistics import mode
from django.db import models
# Create your models here.

class userDetail(models.Model):
    name=models.CharField(default='',max_length=150)
    userid=models.CharField(blank=True,max_length=150)
    key1=models.CharField(blank=True,max_length=150)
    key2=models.CharField(blank=True,max_length=150)
    
class pdf_details(models.Model):
    name=models.ForeignKey(userDetail,on_delete=models.CASCADE)
    hsncode=models.CharField(default='',max_length=150)
    gstno=models.CharField(default='',max_length=150)
    buyername=models.CharField(default='',max_length=150)