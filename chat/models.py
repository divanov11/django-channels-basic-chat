from unicodedata import name
from django.db import models

# Create your models here.

class Details(models.Model):
    name = models.CharField(max_length=255, default=None)
    userid = models.CharField(max_length=255, blank=True)
    
    clientWebsocketKey = models.CharField(max_length=255, blank=True)

    windowServiceKey = models.CharField(max_length=255, blank=True)
    
    def __str__(self) -> str:
        return self.userid