
from django.contrib import admin
from . models import Order

# admin.site.register(Order) # normally we register  a model like this way...
class OrderAdmin(admin.ModelAdmin):
    # list_display = ("owner","order_status") # given fields are shown in the table while opening the order table through admin pannel
    list_filter = [
        "owner",
        "order_status",
            ] # given fields are used for filtering
    search_fields = (
        "owner",
        "id",
    )# using this fields we can search
admin.site.register(Order,OrderAdmin) # we can pass two arguments through register (model,admin class)
