from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=50)
    emails=models.CharField(max_length=40)
    msg=models.CharField(max_length=255)

