from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    mrp = models.IntegerField()
    color = models.CharField(max_length=50)
    varients = models.CharField(max_length=100)
    image1 = models.TextField()
    image2 = models.TextField()
    image3 = models.TextField()
    image4 = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.user)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self) -> str:
        return self.user.username
    
class Offers(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    percent = models.IntegerField()
    title = models.CharField(max_length=100)
    png = models.TextField()
    
    def __str__(self) -> str:
        return str(self.category)

statuses = (
    ('Placed','Placed'),
    ('Shipped','Shipped'),
    ('Out For Delivery', 'Out For Delivery'),
    ('Delivered','Delivered'),
    ('Cancelled','Cancelled')
)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=30,choices=statuses,default="Placed")
    
gender = (
    ('Male','Male'),
    ('Female','Female'),
)
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50,choices=gender)
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.city+'--'+self.pincode