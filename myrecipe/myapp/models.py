from django.db import models

# Create your models here.
class recipe(models.Model):
    recipename=models.CharField(max_length=100)
    recipedescription=models.CharField(max_length=100)
    recipeimg=models.ImageField(upload_to='recipeimg')