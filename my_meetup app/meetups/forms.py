from django import forms


class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Enter your email to join')