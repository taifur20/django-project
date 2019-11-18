from django.urls import path

from . import views

__author__ = 'Sathi'
__copyright__ = 'Copyright 2019'

app_name = 'product'

urlpatterns = [
    path(
        '',
        views.contact,
        name='contacts'
    ),
]
