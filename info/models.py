from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class  UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adress = models.ForeignKey('Adress',on_delete = models.CASCADE,
                               null=True, blank=True)
    company = models.ForeignKey('Company',on_delete = models.CASCADE,
                                null=True, blank=True)
    date = models.DateField(auto_now=True,null=True, blank=True)
    email = models.EmailField(max_length=50)
    def __str__(self):
        return self.user.get_username()

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)
    
class Adress(models.Model):
    oras = models.CharField(max_length= 20)
    tara = models.CharField(max_length= 20)
    strada = models.CharField(max_length= 40)
    zip_code = models.IntegerField()

    def __str__(self):
        return self.oras + " " +self.strada

class Company(models.Model):
    name = models.CharField(max_length = 20)
    adress = models.ForeignKey('Adress',on_delete = models.CASCADE)
    def __str__(self):
        return self.name
    
class  Account(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE,
                               null=True, blank=True)
    name = models.CharField(max_length = 20)
    balance = models.IntegerField()
    income = models.IntegerField()
    expenses = models.IntegerField()
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

    
