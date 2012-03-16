from django.db import models

# Create your models here.
class werbung(models.Model):
    name=models.CharField(max_length=50)
    picture=models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name