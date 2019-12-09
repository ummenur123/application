""" API serializers for the catalog app """

from rest_framework import serializers  # pylint: disable=E0401

from . import models

__author__ = 'Umme Nur Tubba'
__copyright__ = 'Copyright 2019'


# Product API Serializer
class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product
    """
    class Meta:
        model = models.Product
        fields = [
            'id',
            'name',
            'code',
            'slug',
        ]


# Product Attribute API Serializer
class ProductAttributeCRUDSerializer(serializers.ModelSerializer):
    """
    Serializer for Product Attribute Create
    """
    class Meta:
        model = models.ProductAttribute
        fields = [
            'id',
            'product',
            'color',
            'size',
        ]


class ProductAttributeSerializer(serializers.ModelSerializer):
    """
    Serializer for Product Attribute List
    """
    class Meta:
        model = models.ProductAttribute
        fields = [
            'id',
            'product',
            'color',
            'size',
        ]


# Product Price API Serializer
class ProductPriceCRUDSerializer(serializers.ModelSerializer):
    """
    Serializer for Product Price Create
    """
    class Meta:
        model = models.ProductPrice
        fields = [
            'id',
            'product',
            'price',
            'start_date',
            'end_date',
        ]


class ProductPriceSerializer(serializers.ModelSerializer):
    """
    Serializer for Product Price List
    """
    class Meta:
        model = models.ProductPrice
        fields = [
            'id',
            'product',
            'price',
            'start_date',
            'end_date',
        ]
