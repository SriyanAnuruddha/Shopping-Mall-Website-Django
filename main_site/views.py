from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Review

def main_home(request):
    reviews = Review.objects.all()
    return render(request,'main_site/home.html',{'title':'home','reviews': reviews})


def postReview(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        rating = request.POST.get('rating')
        
        if content and rating:
            review = Review.objects.create(content=content, rating=rating, user=request.user)
            messages.success(request, "Review stored successfully")
        else:
            messages.error(request, "Invalid data")
    
    return redirect('main-home')

def getReview(request):
    reviews = Review.objects.all()
    return render(request, 'main_site/home.html', {'reviews': reviews})