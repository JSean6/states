from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse

# Create your models here.

class State(models.Model):
    state_name = models.CharField(max_length=255)
    state_abbrev = models.CharField(max_length=255)
    state_region = models.CharField(max_length=255)
    state_division = models.CharField(max_length=255)    

    def __str__(self):
        return self.state_name
    

class People(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.first_name