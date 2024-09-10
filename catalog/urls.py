from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductDeleteView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog_home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]