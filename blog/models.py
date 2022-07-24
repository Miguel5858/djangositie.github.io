from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100)
    vendedor = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(datetime.date.today)
