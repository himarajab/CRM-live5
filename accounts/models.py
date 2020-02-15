from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=200 , null= True )
    phone = models.CharField(max_length=200, null= True )
    email = models.CharField(max_length=200, null= True )
    profile_pic = models.ImageField(default='12.png',null=True , blank=True)
    date_created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200 , null= True )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200 , null= True )
    price = models.FloatField(null = True)
    CATEGORY = (
        ('Indoor' , 'Indoor',),
        ('Out of door' , 'Out of door'),
    )
    category = models.CharField(max_length=200 , null= True , choices=CATEGORY )
    description = models.CharField(max_length=200 , null= True , blank=True )
    date_created = models.DateTimeField(auto_now_add= True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer , null = True , on_delete= models.SET_NULL)
    product =  models.ForeignKey(Product , null = True , on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add= True)
    STATUS = (
        ('pending' ,'pending' ),
        ('out for delivery' , 'out for delivery'),
        ('delivered' , 'delivered'),
    )
    status = models.CharField(max_length = 200 , null = True ,choices = STATUS)
    note = models.CharField(max_length=200, null= True )


    def __str__(self):
        return self.product.name

