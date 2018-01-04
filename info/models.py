from django.db import models

class  User(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 15)
    email = models.CharField(max_length = 30)
    adress = models.ForeignKey('Adress',on_delete = models.CASCADE)

    def __str__(self):
        return self.first_name + "  "+self.last_name
    

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
    
class user_at_company(models.Model):
    user = models.ForeignKey('User',on_delete = models.CASCADE)
    company = models.ForeignKey('Company',on_delete = models.CASCADE)
    
class  Account(models.Model):
    name = models.CharField(max_length = 20)
    balance = models.IntegerField()
    income = models.IntegerField()
    expenses = models.IntegerField()

    def __str__(self):
        return self.name

class user_account(models.Model):
    user = models.ForeignKey('User',on_delete = models.CASCADE)
    acont = models.ForeignKey('Account',on_delete = models.CASCADE)
    
