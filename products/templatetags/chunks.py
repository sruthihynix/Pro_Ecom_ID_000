from django import template


register= template.Library()

@register.filter(name='chunks_tag')
# // name given to the custom tag is chunks
def chunks_tag(list_data,chunk_size):
    chunk_array=[]
    i=0
    for data in list_data:
        chunk_array.append(data)
        i=i+1
        if  i==chunk_size:
            i=0
            yield chunk_array
            chunk_array=[]# empty chunk_array
    yield chunk_array #Add remaining data if list length is not a perfect multiple of chunk_size


# chunks--a custom tag created