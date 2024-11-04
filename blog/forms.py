from idlelib.autocomplete import ATTRS

from django import forms
from django.core.validators import ValidationError

from blog.models import Message, Article


class ContactUsForm(forms.Form):
    # text = forms.CharField(max_length=500, label='your message')
    # name = forms.CharField(max_length=10, label='your name', required=False)
    # name = forms.CharField(max_length=10, label='your name', widget=forms.)

    BIRTH_YEAR_CHOICES = ['1980','1981', '1982']
    FAVORITE_COLORS_CHOICES = {
        "blue": "Blue",
        "green": "Green",
        "black": "Black"
    }
    name = forms.CharField(max_length=10, label='your name')
    text = forms.CharField(max_length=10, label='your message')
    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, attrs={'class': 'form-control'}))
    birth_year = forms.DateField(widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    # colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=FAVORITE_COLORS_CHOICES)
    # colors = forms.ChoiceField(widget=forms.RadioSelect(), choices=FAVORITE_COLORS_CHOICES)
    colors = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    # numbers = forms.IntegerField(widget=forms.NumberInput())
    numbers = forms.IntegerField()

    def clean(self):
        name = self.cleaned_data.get('name')
        print(name)
        text = self.cleaned_data.get('text')
        # if 'a' in name:
        #     self.add_error('name', 'a can not be in name')
        if name == text:
            raise ValidationError("name and text are same", code='name_text_same')


    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if 'a' in name:
    #         raise ValidationError("a can not be in name", code='a_in_name')
    #     return name
    #     # return name + 'reza'


# class MessageForm(forms.Form):
    # title = forms.CharField(max_length=100)
    # text = forms.CharField(widget=forms.Textarea())
    # email = forms.EmailField()



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # model = Article
        # fields = '__all__'
        # fields = ('title', 'text', 'email')
        exclude = ('date',)
