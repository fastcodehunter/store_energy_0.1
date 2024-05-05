from django import forms
from .models import Order

class FormMakingAnOrder(forms.ModelForm):
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'input_'}))
    street = forms.CharField(widget=forms.TextInput(attrs={'class':'input_'}))
    home = forms.CharField(widget=forms.TextInput(attrs={'class':'castom_input'}))
    flot = forms.CharField(widget=forms.TextInput(attrs={'class':'castom_input'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'input_'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class':'input_'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'input_'}))

    class Meta:
        model = Order
        fields = ['city', 'street', 'home', 'flot', 'name', 'surname', 'email']