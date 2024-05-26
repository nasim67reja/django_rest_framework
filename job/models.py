from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    experience = models.IntegerField()
    skills = models.CharField(max_length=200)
    ending_date = models.DateField()