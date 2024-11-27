from django.db import models
from customers.models import Customer
from products.models import Product


class Order(models.Model): #
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED = 4
    STATUS_CHOICE=((ORDER_PROCESSED,"ORDER_PROCESSED"),
                   (ORDER_DELIVERED,"ORDER_DELIVERED"),
                   (ORDER_REJECTED,"ORDER_REJECTED")
                   )
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE) # order status first cartstage ayirikkum ie 0,
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders') #owner is the present customer --revrse relationship#An Order belongs to a Customer (via the owner field).
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OderedItem(models.Model):
    product=models.ForeignKey(Product,related_name='added_carts',on_delete=models.SET_NULL,null=True) #An OderedItem refers to a Product (via the product field).
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items') # here owner means cart of he customer #An OderedItem belongs to an Order (via the owner field).

    # size





# Create your models here.
