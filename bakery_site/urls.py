from django.urls import path
from . import views

urlpatterns = [
    path('',views.bakery_home, name='bakery-home'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart_bakery'),
    path('cart/', views.cart, name='cart_bakery'),
    path('delete-product-cart-bakery/<int:product_id>',views.delete_product_from_cart,name='delete_product_cart_bakery'),
    path('confirm-order-bakery/', views.confirm_order, name='confirm_order_bakery'),
]
