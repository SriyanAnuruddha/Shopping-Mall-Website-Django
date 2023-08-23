from django.urls import path
from . import views
from  pharmacy_site.views import pharmacy_home

urlpatterns = [
    path('',views.main_home, name='main-home'),
    path('postReview/',views.postReview, name='postReview'),
    path('getReview/',views.getReview, name='getReview'),
]
