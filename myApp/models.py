from django.db import models

# Create your models here.
class blogModel(models.Model):
    titre = models.CharField(max_length=50)
    image = models.URLField(max_length=200)
    description = models.CharField(max_length=300)

class portfolioModel(models.Model):
    titre = models.CharField(max_length=50)
    description = models.CharField(max_length=300)