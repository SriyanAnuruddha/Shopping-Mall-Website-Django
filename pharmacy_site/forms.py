from django import forms

class ImageValidationForm(forms.Form): #this form will help to validate iamge
    prescriptionImage = forms.ImageField()
