from django.db import models

# Create your models here.

class Notas(models.Model):
    Notas = models.CharField(max_length= 250)    
    
    def __str__(self):
        return self.Notas