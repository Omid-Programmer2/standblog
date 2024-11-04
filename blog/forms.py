from django import forms
from django.core.validators import ValidationError

class ContactUsForm(forms.Form):
    # text = forms.CharField(max_length=500, label='your message')
    name = forms.CharField(max_length=10, label='your name')
    text = forms.CharField(max_length=10, label='your message')

    def clean(self):
        name = self.cleaned_data.get('name')
        print(name)
        text = self.cleaned_data.get('text')
        # if 'a' in name:
        #     self.add_error('name', 'a can not be in name')
        if name != text:
            raise ValidationError("name and text are same", code='name_text_same')


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if 'a' in name:
            raise ValidationError("a can not be in name", code='a_in_name')
        return name
        # return name + 'reza'