from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (HomeTemplateView, ContactTemplateView, ProductDetailView, ProductListView, ProductCreateView,
                           ProductUpdateView, ProductDeleteView)
from . import views


app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
]