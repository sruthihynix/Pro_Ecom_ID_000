from django.contrib import admin
from django.urls import path
from django.urls import include #+
from django.conf import settings #+
from django.conf.urls.static import static #+

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('customers/', include('customers.urls')),
    #               path('', include('customers.urls')), # this also  correct

    path('orders/', include('orders.urls')),
    # path('themes/',include('themes.urls')),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
