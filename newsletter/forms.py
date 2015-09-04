from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ["full_name","email"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if extension != 'edu':
            raise forms.ValidationError("Please provide edu email")
        return email


class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if extension != 'edu':
            raise forms.ValidationError("Please provide edu email")
        return email
