from django import forms

class ContactUsForm(forms.Form):
    # text = forms.CharField(max_length=500, label='your message')
    name = forms.CharField(max_length=10, label='your name')
    text = forms.CharField(max_length=10, label='your message')