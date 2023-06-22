from django.db import models

class UserRegistration(models.Model):
    Name = models.CharField(max_length=50)
    UserName = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Phone = models.BigIntegerField()
    Address = models.CharField(max_length=50)
    Password = models.CharField(max_length=20)
    TermAndConditions = models.BooleanField(default=True)