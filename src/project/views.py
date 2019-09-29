""" Views for the project app """

from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext_lazy as _

from product import models as product_models

__author__ = 'Sathi'
__copyright__ = 'Copyright 2019'


# Views
def home(request):
    product_list = product_models.Product.objects.all()[:3]
    context = {
        'product_list': product_list,
        'navbar': 'home',

    }
    return render(request, 'home.html', context)
