from django.db import models

class login(models.Model):
    email_id= models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)