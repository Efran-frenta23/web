from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from shoppinglist import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cart.urls')),
]