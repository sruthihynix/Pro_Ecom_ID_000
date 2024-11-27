from django.shortcuts import render,redirect

from django.shortcuts import render
from .models import Order,OderedItem
from products.models import Product
# Create your views here.
def show_cart(request):
    user = request.user
    if user.is_authenticated:
        customer = user.customer_profile
        # Get the user's active cart
        cart = Order.objects.filter(owner=customer, order_status=Order.CART_STAGE).first()

        return render(request, 'cart.html', {'cart': cart})
        # print(cart)


    # else:
    return render(request, 'cart.html', {'cart': None})
    # return render(request,'cart.html')

def add_to_cart(request):

    if request.POST:
        user = request.user

        customer = user.customer_profile # customer object conected
        # Get product and quantity from posted data
        quantity = int(request.POST.get('quantity',1))
        product_id = request.POST.get('product_id')

        # Get the product and create the OrderedItem
        product=Product.objects.get(pk=product_id) # product obj
        # print(product,user,customer,quantity,product_id)

# to add data to item-> get cart_obj
# get_or_create() if no order is there then create an order
# tuple is returned,two values 1.object 2.create/not
# use coma to unbock tuple

        # Get or create the cart for the user
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE,
        )
        # get or create object for ordered item
        ordered_item,created = OderedItem.objects.get_or_create(
            product = product,# product obj
            owner = cart_obj,
        )
        if created:
            ordered_item.quantity=quantity
            ordered_item.save()
        else:
            ordered_item.quantity=ordered_item.quantity+quantity
            ordered_item.save()
        # print(ordered_item)
        # print(product,quantity)
        return redirect('cart')
