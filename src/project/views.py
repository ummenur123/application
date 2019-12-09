""" Views for the project app """

from django.shortcuts import render  # pylint: disable=E0401

__author__ = 'Umme Nur Tubba'
__copyright__ = 'Copyright 2019'


# Views
def home(request):
    """
    Home view for Application
    """
    return render(request, 'home.html', {})
