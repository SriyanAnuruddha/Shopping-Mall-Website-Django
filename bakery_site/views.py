from django.shortcuts import get_object_or_404, redirect, render
from .models import BakeryItem,Cart,Order, OrderDetail

# Create your views here.
def bakery_home(request):
    context={
        'title':'bakery-home',
        'products':BakeryItem.objects.all()
    }
    return render(request,'bakery_site/home.html',context)

def add_to_cart(request, product_id):
    product = get_object_or_404(BakeryItem, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    return redirect('cart_bakery')

def cart(request):   
    try:
        cart = Cart.objects.get(user=request.user)
    except :
        cart=None

    context={
        'cart': cart    
    }
    return render(request, 'bakery_site/cart.html',context )


def delete_product_from_cart(request,product_id): 
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(BakeryItem, id=product_id)
    
    cart.products.remove(product)
    
    return redirect('cart_bakery')



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

        return redirect('cart_bakery')
    else:
        # Handle GET request
        return redirect('cart_bakery')
