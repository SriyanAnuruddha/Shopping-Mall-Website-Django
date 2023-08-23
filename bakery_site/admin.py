from django.contrib import admin
from .models import BakeryItem,Order,OrderDetail,Cart

# Register your models here.
admin.site.register(BakeryItem)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Cart)