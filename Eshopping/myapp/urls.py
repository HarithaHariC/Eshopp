from django.urls import path
from myapp.views import *
urlpatterns = [
    path('product/',Productlist.as_view()),
    path('product/<int:pk>',Productdetails.as_view()),
    path('custom/',custom_list.as_view()),
    path('custom_details/<int:pk>',custom_details.as_view()),
    path('customer_reg/',RegisterUserAPIView.as_view()),
]