from django.db import models

class productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField(default=0)
    categoria = models.CharField(max_length=30)