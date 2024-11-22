from django.urls import path

from django.conf import settings  # +
from django.conf.urls.static import static  # +
from . import views

urlpatterns = [

                  path('', views.index, name='home'),
                  path('product_list/', views.list_products, name='product_list'),
                  path('product_detail/<pk>', views.detail_product, name='product_detail'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
