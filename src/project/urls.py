""" project URL Configuration """

# pylint: disable=E0401
from django.contrib import admin
from django.urls import include, path
# pylint: enable=E0401

from . import views

__author__ = 'Umme Nur Tubba'
__copyright__ = 'Copyright 2019'


# URLs
app_name = 'project'

urlpatterns = [

    # Admin
    path(
        'admin/',
        admin.site.urls
    ),

    # Home
    path(
        '',
        views.home,
        name='home'
    ),

    # Catalog API
    path(
        'product/',
        include('catalog.urls', namespace='catalog_api')
    ),
]
