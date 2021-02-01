from django.db import models
from django.forms import ModelForm

class User(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(default=0)
    email = models.EmailField()
    gender = models.CharField(max_length=5)
    password = models.CharField(max_length=20)
    dob = models.DateField()
    profilefor = models.CharField(max_length=50, default="Self")
    height = models.FloatField(default=0.0, max_length=5)
    weight = models.FloatField(default=0.0, max_length=5)
    color = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    caste = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    disability = models.CharField(max_length=50)
    familystatus = models.CharField(max_length=50)
    familytype = models.CharField(max_length=50)
    familyvalue = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    diet = models.CharField(max_length=50)
    work = models.CharField(max_length=100, default="None")
    income = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='profilepic')
    def __str__(self):
        return self.name





