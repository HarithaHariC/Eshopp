from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from myapp.models import *
from myapp.serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication

class Productlist(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductSerializer

class Productdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product
    serializer_class = ProductSerializer

class custom_list(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class= UserSerializer

class custom_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = User
    serializer_class = UserSerializer

# class UserDetailAPI(APIView):
#   authentication_classes = (TokenAuthentication,)
#   permission_classes = (AllowAny,)
#   def get(self,request,*args,**kwargs):
#     user = User.objects.get(id=request.user.id)
#     serializer = UserSerializer(user)
#     return Response(serializer.data)
  


class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer




