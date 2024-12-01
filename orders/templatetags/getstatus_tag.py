from django import template


register= template.Library()

@register.simple_tag(name='getstatus_tag')
# // name given to the custom tag is getstatus_tag
# code writing in template tag is same like in python
def getstatus_tag(status):
    status=status-1 # because cart stage status is 0 so to avoid that error

    status_array=['confirmed','processed','delivered','rejected']

    return status_array[status]


# getstatus--a custom tag created

 # # Constants for order status
 #    CART_STAGE=0
 #    ORDER_CONFIRMED=1
 #    ORDER_PROCESSED=2
 #    ORDER_DELIVERED=3
 #    ORDER_REJECTED = 4