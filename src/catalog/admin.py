""" Admin for the catalog app """

# pylint: disable=E0401
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
# pylint: enable=E0401

from . import models

__author__ = 'Umme Nur Tubba'
__copyright__ = 'Copyright 2019'


# Inlines
class ProductAttributeInline(admin.TabularInline):
    """
    Product Attribute Inline
    """
    model = models.ProductAttribute
    extra = 0
    fields = (
        'id',
        'color',
        'size',
    )


class ProductPriceInline(admin.StackedInline):
    """
    Product Price Inline
    """
    model = models.ProductPrice
    extra = 0
    fields = (
        'id',
        'price',
        'start_date',
        'end_date',
    )


# Admin
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Product Admin
    """
    fieldsets = (
        (_('Product Info'), {
            'fields': (
                'name',
                'code',
            )
        }),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'id',
                'created_by',
                'created_on',
                'slug',
                'updated_by',
                'updated_on',
            ),
        }),
    )
    inlines = [
        ProductAttributeInline,
        ProductPriceInline,
    ]
    list_display = (
        'name',
        'code',
        'updated_on',
        'updated_by',
    )
    list_display_links = (
        'name',
    )
    readonly_fields = (
        'id',
        'created_by',
        'created_on',
        'slug',
        'updated_by',
        'updated_on',
    )

    def save_model(self, request, obj, form, change):
        if change:
            if request.user:
                obj.updated_by = request.user
        else:
            if request.user:
                obj.created_by = request.user
                obj.updated_by = request.user
        obj.save()
