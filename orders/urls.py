from django.urls import path

from django.conf import settings  # +
from django.conf.urls.static import static  # +
from . import views

urlpatterns = [
path('cart/', views.show_cart, name='cart'),

  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
