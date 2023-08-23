from django.urls import path
from . import views

urlpatterns = [
    path('',views.mobile_shop_home, name='mobile-shop-home'),
    path('mobiles-page/',views.mobiles_page, name='mobiles-page'),
    path('search/',views.search_product, name='mobiles-search-product'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart_mobileShop'),
    path('cart/', views.cart, name='cart_mobileShop'),
    path('delete-product-cart-mobileShop/<int:product_id>',views.delete_product_from_cart,name='delete_product_mobileShop'),
    path('confirm-order-mobileShop/', views.confirm_order, name='confirm_order_mobileShop'),
]
