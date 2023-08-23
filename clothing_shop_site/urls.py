from django.urls import path
from . import views

urlpatterns = [
    path('',views.clothing_shop_home, name='clothing-shop-home'),
    path('cart/', views.cart, name='cart_clothShop'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart_clothShop'),
    path('delete-product-cart-clothShop/<int:product_id>',views.delete_product_from_cart,name='delete_product_cart_clothShop'),
    path('confirm-order-clothShop/', views.confirm_order, name='confirm_order_clothShop'),
    path('contact/', views.contact, name='clothShop_contact'),
    path('about/', views.about, name='clothShop_about'),
]
