from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class SignUpForm(forms.Form):
    phone_number = RegexValidator(regex=r'^\d{10}$',
                                  message='Phone number must be entered in the format: 1234567890. Without +7 or 8')
    phone = forms.CharField(validators=[phone_number])
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if User.objects.filter(username=phone).exists():
            raise forms.ValidationError('Phone number already exists')
        return phone
