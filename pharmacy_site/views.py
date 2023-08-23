from django.shortcuts import get_object_or_404, render,redirect,reverse
from .models import Medicine,Prescription,OrderDetail,Order,Cart,User
from .forms import ImageValidationForm

# imports for OCR 
import pytesseract
from PIL import Image
import os

#imports string matching
from fuzzywuzzy import fuzz

def pharmacy_home(request):
    context={
        'title':'pharmacy-home',
        'meds':Medicine.objects.all()[:10]
    }
    return render(request,'pharmacy_site/home.html',context)


def search_product(request):
    productName=request.GET.get('productName')
    meds=Medicine.objects.filter(name__icontains=productName)
    context={
        'title':'pharmacy-home',
        'meds':meds
    }
    return render(request,'pharmacy_site/home.html',context)

def upload_prescription(request):
    if request.method == 'POST':
        form = ImageValidationForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded image file
            image_file = request.FILES['prescriptionImage']
            # Create an instance of the Prescription model and set the image field
            prescription = Prescription()
            prescription.image = image_file
            prescription.save()
            #redirect to the page
            redirect_url = reverse('prescription-calculate') + f'?id={prescription.id}'
            return redirect(redirect_url)
    else:
        form = ImageValidationForm()

    return render(request, 'pharmacy_site/prescription.html', {'form': form})

def prescription_calc(request):
    id = request.GET.get('id')
    prescription = get_object_or_404(Prescription, id=id)
    image_url = prescription.image.url

    #ocr code
    def ocr_core(filename):
        text = pytesseract.image_to_string(Image.open(filename), lang='eng', config='--psm 6')
        text.strip()
        return text.strip()

    #change 'replace()' if ur using linux or mac
    filename=os.path.abspath(os.path.join(os.getcwd(),'.')+image_url.replace('/','\\'))
    medNames = ocr_core(filename)

    
    #check those objects exist in the database
    names_in_database = list(Medicine.objects.values_list('name', flat=True))

    #compare database names with prescription names
    def find_matching_names(string, name_list, threshold=70):
        matching_names = []
        sorted_tokens = sorted(string.lower().split())
        for name in name_list:
            processed_name = ''.join(e for e in name.lower() if e.isalnum())
            if fuzz.partial_ratio(''.join(sorted_tokens), processed_name) >= threshold:
                matching_names.append(name)
        return matching_names

    matching_names = find_matching_names(medNames, names_in_database)

    context = {
        'image_url': image_url,
        'medNames':matching_names
    }


    return render(request, 'pharmacy_site/prescription.html', context)


def presc_to_cart(request):
    if request.method == 'POST':
            # Access the POST data
            for key, value in request.POST.items():
                if(key!='csrfmiddlewaretoken'):
                    product = get_object_or_404(Medicine, name=value)
                    cart, created = Cart.objects.get_or_create(user=request.user)
                    cart.products.add(product)
                    
            return redirect('cart_pharmacy')
    
        # Render the template with the provided context
    return render(request, 'pharmacy_site/cart.html')




def cart(request):   
    try:
        cart = Cart.objects.get(user=request.user)
    except :
        cart=None

    context={
        'cart': cart    
    }
    return render(request, 'pharmacy_site/cart.html',context )


def add_to_cart(request, product_id):
    product = get_object_or_404(Medicine, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    return redirect('cart_pharmacy')


def delete_product_from_cart(request,product_id): 
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Medicine, id=product_id)
    cart.products.remove(product)
    return redirect('cart_pharmacy')


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

            OrderDetail.objects.create(order=order, medicine=product, quantity=quantity, price=price)

        # Clear the cart after successful order placement
        cart.products.clear()

        return redirect('cart_pharmacy')
    else:
        # Handle GET request
        return redirect('cart_pharmacy')

