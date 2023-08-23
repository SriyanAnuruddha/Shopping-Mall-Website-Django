from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BakeryItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image=models.ImageField(default='default.jpg',upload_to='bakery_images')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE,related_name="bakery_orders")
    order_date = models.DateTimeField(auto_now_add=True)
    total=models.DecimalField(max_digits=10, decimal_places=2)
    

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
    item = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Cart(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(BakeryItem, blank=True)