from django import template


register= template.Library()

@register.simple_tag(name='multiply_tag')
# // name given to the custom tag is multiply_tag
def multiply_tag(a,b):

    return a*b


# multiply_tag--a custom tag created