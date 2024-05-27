from django.contrib import admin
from django.urls import path, include

from product.views.product_view import index_view

urlpatterns = [
    path('',include('home.urls')),
    path('admin/', admin.site.urls),
    path('products/', include("product.urls")),
]