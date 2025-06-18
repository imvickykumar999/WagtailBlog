from django_recaptcha.widgets import ReCaptchaV2Checkbox 
from django_recaptcha.fields import ReCaptchaField
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20, required=False)
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    