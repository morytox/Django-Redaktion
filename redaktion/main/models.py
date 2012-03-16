from django.db import models

# Create your models here.

class redakteur(models.Model):
    name=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name

class journalist(models.Model):
    name=models.CharField(max_length=50)
    redakteur=models.ForeignKey(redakteur)
    
    def __unicode__(self):
        return self.name
    
class thema(models.Model):
    t_name=models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.titel
    
class story(models.Model):
    STATUS_CHOICES=(("P","published"),("A","archived"),("D","draft"))
    titel=models.CharField(max_length=50)
    inhalt=models.TextField()
    journalist=models.ForeignKey(journalist)
    status=models.CharField(max_length=1,choices=STATUS_CHOICES)
    thema=models.ManyToManyField(thema)
    
    def __unicode__(self):
        return self.titel

