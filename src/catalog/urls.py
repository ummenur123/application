""" API URLs for the catalog app """

from django.urls import path  # pylint: disable=E0401

from . import views

__author__ = 'Umme Nur Tubba'
__copyright__ = 'Copyright 2019'


# App
app_name = 'catalog'


# URLs
urlpatterns = [

    # Product API URLs
    path(
        '',
        views.ProductListAPIView.as_view(),
        name='product_list',
    ),
    path(
        '<int:pk>/',
        views.ProductDetailAPIView.as_view(),
        name='product_detail',
    ),

    # Product Attribute API URLs
    path(
        'attribute/',
        views.ProductAttributeCreateAPIView.as_view(),
        name='product_attribute_create',
    ),
    path(
        'attribute-list/',
        views.ProductAttributeListAPIView.as_view(),
        name='product_attribute_list',
    ),

    # Product Price API URLs
    path(
        'price/',
        views.ProductPriceCreateAPIView.as_view(),
        name='product_price_create',
    ),
    path(
        'price-list/',
        views.ProductPriceListAPIView.as_view(),
        name='product_price_list',
    ),

]
