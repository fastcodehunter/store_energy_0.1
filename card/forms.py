from django import forms
from card.models import Order

class FormMakingAnOrder(forms.ModelForm):
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_'}),
        error_messages={
            'required': 'Please enter your city.',
            'invalid': 'Invalid city name.',
            'max_length': 'City name is too long.'
        }
    )
    street = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_'}),
        error_messages={
            'required': 'Please enter your street.',
            'invalid': 'Invalid street name.',
            'max_length': 'Street name is too long.'
        }
    )
    home = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'castom_input'}),
        error_messages={
            'required': 'Please enter your home number.',
            'invalid': 'Invalid home number.',
            'max_length': 'Home number is too long.'
        }
    )
    flot = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'castom_input'}),
        error_messages={
            'required': 'Please enter your flot number.',
            'invalid': 'Invalid flot number.',
            'max_length': 'Flot number is too long.'
        }
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_'}),
        error_messages={
            'required': 'Please enter your name.',
            'invalid': 'Invalid name.',
            'max_length': 'Name is too long.'
        }
    )
    surname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_'}),
        error_messages={
            'required': 'Please enter your surname.',
            'invalid': 'Invalid surname.',
            'max_length': 'Surname is too long.'
        }
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'input_'}),
        error_messages={
            'required': 'Please enter your email.',
            'invalid': 'Invalid email address.',
            'max_length': 'Email address is too long.'
        }
    )

    class Meta:
        model = Order
        fields = ['city', 'street', 'home', 'flot', 'name', 'surname', 'email']