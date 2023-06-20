from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    name = models.CharField(max_length=50,blank=True)
    description = models.CharField(max_length=200,blank=True)
    price = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
    
class Customer_order(models.Model):
    cust_id=models.ForeignKey(User,on_delete=models.CASCADE)
    prod_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    


