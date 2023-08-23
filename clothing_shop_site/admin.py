from django.contrib import admin
from .models import Cloth,Order,OrderDetail,Cart
# Register your models here.

admin.site.register(Cloth)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Cart)