from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    profile_pic = models.ImageField(default='computer-icons-user-profile-male-avatar-avatar-png-clip-art.png',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name





class Product(models.Model):
    CATEGORI = (
        ('indor','Indor'),
        ('outdor','Outdor')
    )

    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,choices=CATEGORI,null=True)
    description = models.CharField(max_length=200,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name





class Order(models.Model):
    STATUS  = (
        ('delivered','Delivered'),
        ('pending','Pending'),
        ('out of delivered','Out Of Delivered')


    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=200,choices=STATUS,null=True)
    date = models.DateTimeField(auto_now_add=True)
