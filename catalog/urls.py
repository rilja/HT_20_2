from django.urls import path

from catalog.views import ProductListView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog_home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_details')
]