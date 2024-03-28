from django.db import models
class products(models.Model):
    name=models.CharField(max_length=50, default="null")
    price=models.IntegerField(default="null")
    category=models.CharField(max_length=50, default="null")
    types=models.CharField(max_length=50, default="null")
    brand=models.CharField(max_length=50,default="null")
    image=models.ImageField(max_length=50, default="null",upload_to="media/")

class user(models.Model):
    firstname=models.CharField(max_length=50,default="")
    lastname=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    password=models.CharField(max_length=50,default="")
class order(models.Model):
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    password=models.CharField(max_length=50,default="")
    color=models.CharField(max_length=50,default="")
    products=models.CharField(max_length=5000,default="")
    size=models.IntegerField(default=0)
    pin=models.IntegerField(default=0)
    phone_no=models.IntegerField(default=0)
    address=models.CharField(max_length=50,default="")
    pay_mode=models.CharField(max_length=50,default="")
    products=models.CharField(max_length=5000,default="")
    city=models.CharField(max_length=50,default="")
    

    


    


# Create your models here.
