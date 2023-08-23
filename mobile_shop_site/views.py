from django.shortcuts import get_object_or_404, redirect, render
from .models import Mobile,Other_parts,RepairCost,Order,OrderDetail,User,Cart

# Create your views here.
def mobile_shop_home(request):
    context={
        'title':'mobile-shop-home',
        'Replace_battery':RepairCost.objects.filter(repair_name="Replace battery").first().cost,
        'Screen_repair':RepairCost.objects.filter(repair_name="Screen repair").first().cost,
        'Water_damage_repair':RepairCost.objects.filter(repair_name="Water damage repair").first().cost,
        'Software_repair':RepairCost.objects.filter(repair_name="Software repair").first().cost,
        'Camera_repair':RepairCost.objects.filter(repair_name="Camera repair").first().cost,
        'Speaker_repair':RepairCost.objects.filter(repair_name="Speaker repair").first().cost,
        'Back_cover_replacement':RepairCost.objects.filter(repair_name="Back cover replacement").first().cost,
        'Screen_protector_replacement':RepairCost.objects.filter(repair_name="Screen protector replacement").first().cost
    }   
    return render(request,'mobile_shop_site/home.html',context)

def mobiles_page(request):
    context={
        'title':'mobiles',
        'mobiles':Mobile.objects.all()[:20]
    }
    return render(request,'mobile_shop_site/mobiles.html',context)

def search_product(request):
    productName=request.GET.get('productName')
    mobiles=Mobile.objects.filter(name__icontains=productName)
    context={
        'title':'pharmacy-home',
        'mobiles':mobiles
    }
    return render(request,'mobile_shop_site/mobiles.html',context)



def add_to_cart(request, product_id):
    product = get_object_or_404(Mobile, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    return redirect('cart_mobileShop')

def cart(request):   
    try:
        cart = Cart.objects.get(user=request.user)
    except :
        cart=None

    context={
        'cart': cart    
    }
    return render(request, 'mobile_shop_site/cart.html',context )


def delete_product_from_cart(request,product_id): 
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Mobile, id=product_id)
    
    cart.products.remove(product)
    
    return redirect('cart_mobileShop')



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

        return redirect('cart_mobileShop')
    else:
        # Handle GET request
        return redirect('cart_mobileShop')
