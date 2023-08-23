from django.contrib import admin
from .models import Medicine,Order,OrderDetail,Cart

admin.site.register(Medicine)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Cart)
