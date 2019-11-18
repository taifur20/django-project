from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.conf import settings

# from . import forms
from product import product_models
# from . import models

# import json
# import mailchimp

__author__ = 'Sathi'
__copyright__ = 'Copyright 2019'


# Views
def contact(request):
    product_list = product_models.Product.objects.all()
    # if request.method == 'POST':
    #     form = forms.ContactForm(request.POST or None)
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.save()
    #         ctx = {
    #             'instance': instance,
    #         }
    #         msg_plain = render_to_string('contact/mail_confirmation.txt', ctx)
    #         msg_html = render_to_string('contact/mail_confirmation.html', ctx)
    #         subject = 'Confirmation Mail'
    #         message = msg_plain
    #         from_email = settings.EMAIL_HOST_USER
    #         to_list = [instance.email, settings.ADMIN]
    #         send_mail(
    #             subject,
    #             message,
    #             from_email,
    #             to_list,
    #             html_message=msg_html,
    #             fail_silently=True
    #         )
    #         return HttpResponseRedirect(reverse('contact:school_trip_success'))
    # else:
    #     form = forms.ContactForm()
    context = {
        'product_list': product_list,
        'form': form,
    }
    return render(request, 'contacts/contact.html', context)
