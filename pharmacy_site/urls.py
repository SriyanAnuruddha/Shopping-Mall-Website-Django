from django.urls import path
from . import views

urlpatterns = [
    path('',views.pharmacy_home, name='pharmacy-home'),
    path('search/',views.search_product, name='pharmacy-search-product'),
    path('prescriptionUpload/',views.upload_prescription, name='prescription-upload'),
    path('prescriptionCalculate/',views.prescription_calc, name='prescription-calculate'),
    path('presecriptionToCart/',views.presc_to_cart, name='prescription-to-cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart_pharmacy'),
    path('cart/', views.cart, name='cart_pharmacy'),
    path('delete-product-cart-pharmacy/<int:product_id>',views.delete_product_from_cart,name='delete_product_cart_pharmacy'),
    path('confirm-order-pharmacy/', views.confirm_order, name='confirm_order_pharmacy'),
    
]

