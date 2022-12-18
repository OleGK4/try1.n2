from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts', ContactsView.as_view(), name='contacts'),
    path('about', AboutView.as_view(), name='about'),
    path('login', LoginingView.as_view(), name='login'),
    path('add_product', AddProductView.as_view(), name='add-product'),
    path('product', ProductView.as_view(), name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
