from django.db import models

# Create your models here.

class Signupdetails(models.Model):
    admin_name = models.CharField(max_length=100)
    admin_email = models.CharField(max_length=100)
    admin_username = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=400)