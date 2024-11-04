from django import forms

class ContactUsForm(forms.Form):
    # text = forms.CharField(max_length=500, label='your message')
    text = forms.CharField(max_length=10, label='your message')