from django.urls import path

from django.conf import settings  # +
from django.conf.urls.static import static  # +
from . import views

urlpatterns = [
    # path('', views.index, name='home'),
    path('account/', views.show_account, name='account'),
    path('logout/', views.signout, name='logout'),



  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
