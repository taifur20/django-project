from django import forms
from django.utils.translation import ugettext_lazy as _

from . import models


# Forms
class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            'name',
            'subject',
            'description',
            'email',
            'phone',
        )


# class NewsletterForm(forms.Form):
#     email_address = forms.EmailField()
