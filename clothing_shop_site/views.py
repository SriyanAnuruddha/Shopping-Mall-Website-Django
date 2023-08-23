from django.shortcuts import get_object_or_404, redirect, render
from .models import *
# Create your views here.
def clothing_shop_home(request):
    context={
        'title':'clothing-shop-home',
        'cloths':Cloth.objects.all()[:10],
        'recents':Cloth.objects.order_by('-id')[:10]
    }
    return render(request,'clothing_shop_site/home.html',context)


def cart(request):   
    try:
        cart = Cart.objects.get(user=request.user)
    except :
        cart=None

    context={
        'cart': cart    
    }
    return render(request, 'clothing_shop_site/cart.html',context )


def add_to_cart(request, product_id):
    product = get_object_or_404(Cloth, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    return redirect('cart_clothShop')

def delete_product_from_cart(request,product_id): 
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Cloth, id=product_id)
    
    cart.products.remove(product)
    
    return redirect('cart_clothShop')



def confirm_order(request):
    if request.method == 'POST':
        # Retrieve form data and create an order
        customer = request.user
        total_price = request.POST.get('total_price')

        order = Order.objects.create(customer=customer, total=total_price)

        # Retrieve cart items and create order details
        cart = get_object_or_404(Cart, user=customer)
        products = cart.products.all()

        for product in products:
            quantity = request.POST.get('quantity[]')
            price = product.price

            OrderDetail.objects.create(order=order, item=product, quantity=quantity, price=price)

        # Clear the cart after successful order placement
        cart.products.clear()

        return redirect('cart_clothShop')
    else:
        # Handle GET request
        return redirect('cart_clothShop')


def contact(request):
    return render(request, 'clothing_shop_site/contact.html' )

def about(request):
    return render(request, 'clothing_shop_site/about.html' )