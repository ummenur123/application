""" Models for the catalog app """

from __future__ import unicode_literals

# pylint: disable=E0401
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
# pylint: enable=E0401

__author__ = 'Umme Nur Tubba'
__copyright__ = 'Copyright 2019'


# Models
class Product(models.Model):
    """
    Main Model, Product
    """

    # Attributes
    code = models.CharField(
        _('code'),
        blank=False,
        max_length=191,
    )
    name = models.CharField(
        _('name'),
        blank=False,
        max_length=191,
    )
    slug = models.SlugField(
        _('slug'),
        editable=False,
        unique=True,
    )

    # Meta Data
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        verbose_name=_('created by'),
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )
    updated_by = models.ForeignKey(
        User,
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        verbose_name=_('updated by'),
    )

    # Meta
    class Meta:
        ordering = ['name']
        verbose_name = _('product')
        verbose_name_plural = _('products')

    # Method
    def __str__(self):
        return "%s - %s" % (self.name, self.code)

    # Save function
    def save(self, *args, **kwargs):
        """
        Save slug
        """
        self.slug = slugify("%s - %s" % (self.name, self.id))
        return super(Product, self).save(*args, **kwargs)


class ProductAttribute(models.Model):
    """
    Attribute Model for Product App
    """

    # Relations
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        verbose_name=_('product'),
    )

    # Attributes
    color = models.CharField(
        _('product color'),
        max_length=191,
    )
    size = models.CharField(
        _('size'),
        max_length=191,
    )

    # Meta Data
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Meta
    class Meta:
        verbose_name = _('product attribute')
        verbose_name_plural = _('products attributes')

    # Method
    def __str__(self):
        return "%s - [%s - %s]" % (self.product.name, self.color, self.size)


class ProductPrice(models.Model):
    """
    Price Model for Product App
    """

    # Relations
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        verbose_name=_('product'),
    )

    # Attributes
    price = models.DecimalField(
        _('price'),
        decimal_places=2,
        max_digits=8,
        default=0,
    )
    start_date = models.DateField(
        _('start date')
    )
    end_date = models.DateField(
        _('end date')
    )

    # Meta Data
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Meta
    class Meta:
        verbose_name = _('product price')
        verbose_name_plural = _('products prices')

    # Method
    def __str__(self):
        return "%s - [%s - %s]" % (
            self.product.name,
            self.start_date,
            self.end_date
        )
