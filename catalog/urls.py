from django.urls import path

from catalog.views import home, product_details

app_name = 'catalog'

urlpatterns = [
    path('', home, name='catalog_home'),
    path('product/<int:pk>/', product_details, name='product_details')
]