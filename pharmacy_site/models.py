from django.db import models
from django.contrib.auth.models import User

class Medicine(models.Model):
    name=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.IntegerField()
    dosage=models.CharField(max_length=100)
    description = models.TextField()
    image=models.ImageField(default='default.jpg',upload_to='pharmacy_images')

    def __str__(self) -> str: # when query this data using shell. the name of the med will show in the list insted of object id
        return self.name 

class Order(models.Model):
    date_ordered=models.DateTimeField(auto_now_add=True) #add time that ordered is created
    total=models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Prescription(models.Model):
    image=models.ImageField(default='default.jpg',upload_to='pharmacy_images/')

class Cart(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='pharmacy_cart')
    products = models.ManyToManyField(Medicine, blank=True)