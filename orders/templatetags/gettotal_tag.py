from django import template


register= template.Library()

@register.simple_tag(name='gettotal_tag')
# // name given to the custom tag is gettotal_tag
# code writing intemplate tag is samelike in python
def gettotal_tag(cart):
    total=0
    for item in cart.added_items.all():
        total+= item.quantity * item.product.price
    return total


# gettotal_tag--a custom tag created