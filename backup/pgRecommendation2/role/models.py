from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
# Create your models here.

class Admin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobileNumber=models.BigIntegerField()
    EC1=models.BigIntegerField(blank=True,null=True)
    EC2=models.BigIntegerField(blank=True,null=True)
    EC3=models.BigIntegerField(blank=True,null=True)
    image=models.ImageField(blank=True,null=True)
    gender=models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name}"

class Member(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobileNumber=models.BigIntegerField()
    workingAddress=models.CharField(max_length=200)
    fee=models.IntegerField(default=0)
    image=models.ImageField(blank=True,null=True,upload_to='upload/')
    specialization=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"
