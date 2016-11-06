from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _


phone_number = RegexValidator(regex=r'^\d{10}$',
                              message=_('Phone number must be entered in the format: 1234567890. Without +7 or 8'))


class SignUpForm(forms.Form):
    phone = forms.CharField(validators=[phone_number])
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if User.objects.filter(username=phone).exists():
            raise forms.ValidationError(_('Phone number already exists'))
        return phone


class MessageForm(forms.Form):
    receiver = forms.CharField(validators=[phone_number])
    text = forms.CharField(widget=forms.Textarea)

    def clean_receiver(self):
        receiver = self.cleaned_data['receiver']
        if not User.objects.filter(username=receiver).exists():
            raise forms.ValidationError(_('The person with this number is not in service'))
        return receiver
