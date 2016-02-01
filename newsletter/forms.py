from django import forms

from .models import SignUp


class SignUpForm (forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email']

    def clean_email(self):
        email = self.cleaned_data.get ('email')
        email_base, provider = email.split ('@')
        domain, extension = provider.split ('.')
        #if not domain.lower() == 'usc':
            #raise forms.ValidationError ('Please make sure u use *@USC.* email')
        if not extension.lower() == 'edu':
            raise forms.ValidationError ('Please make sure u use *@*.edu')
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        #write ur walidation code
        return full_name