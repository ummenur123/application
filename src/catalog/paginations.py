""" API pagination for the catalog app """

# pylint: disable=E0401
from rest_framework import pagination
# pylint: enable=E0401

__author__ = 'Umme Nur Tubba'
__copyright__ = 'Copyright 2019'


# Pagination
class ProductListResultsSetPagination(pagination.PageNumberPagination):
    """
    Product List Pagination
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 15
