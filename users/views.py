from django.shortcuts import render,redirect
from .forms import UserRegisterForm #import my custom form
from django.contrib import messages


def register(request):
    #now we need way to handle data that come with the form
    #if we get post request which means that post request contains that data
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():# check submitted data is valid
            form.save() #this will save the submitted data to database
            username=form.cleaned_data.get('username')
            messages.success(request,f"Your account has been created! you are now able to login") #inform user that account is succesfully created
            return redirect('user-login')
    else: #if we dont get valid data or not data at all we create new form
        form=UserRegisterForm() # this will create empty form

    context={
                'title':'user registration', # we can access this form within the template by passing it as context
                'form':form
            }
    return render(request,'users/register.html',context)