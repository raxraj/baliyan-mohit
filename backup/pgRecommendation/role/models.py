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
    address=models.CharField(max_length=200)
    otp=models.CharField(max_length=20)
    is_enabled=models.IntegerField()
    image=models.ImageField(blank=True,null=True,upload_to='upload/')
    

class Property(models.Model):
    user_name=models.CharField(max_length=100)
    house_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    rent=models.CharField(max_length=100)
    image=models.ImageField(blank=True,null=True,upload_to='upload/')
    facility=models.CharField(max_length=200)
    pg_type=models.CharField(max_length=100)
    no_of_rooms=models.CharField(max_length=100)
    near_by_facilities=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"
