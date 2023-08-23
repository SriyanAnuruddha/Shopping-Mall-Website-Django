from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cloth(models.Model):
    name=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image=models.ImageField(default='default.jpg',upload_to='clothing_shop_images')

    def __str__(self) -> str: # when query this data using shell. the name of the med will show in the list insted of object id
        return self.name 
    

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE,related_name="clothShop_orders")
    order_date = models.DateTimeField(auto_now_add=True)
    total=models.DecimalField(max_digits=10, decimal_places=2)
    

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='clothShop_order_details')
    item = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Cart(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='clothShop_cart')
    products = models.ManyToManyField(Cloth, blank=True)