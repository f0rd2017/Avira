from .models import Wallet, History, Users
from django.forms import ModelForm, TextInput, Select, CharField, ChoiceField

class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ['email','name','password']

        widgets = {
            "email": TextInput(attrs={
                'placeholder': 'Email'
            }),
            "name": TextInput(attrs={
                'placeholder': 'Ім\'я'
            }),
            "password": TextInput(attrs={
                'placeholder': 'password',
                'type': 'password'
            })
        }

class UserLoginForm(ModelForm):
    class Meta:
        model = Users
        fields = ['email','password']

        widgets = {
            "email": TextInput(attrs={
                'placeholder': 'Email'
            }),
            "password": TextInput(attrs={
                'placeholder': 'password',
                'type': 'password'
            })
        }

class WalletForm(ModelForm):
    class Meta:
        model = Wallet
        fields = ['user','wallet','Tron','Avira','USDT']

class HistoryForm(ModelForm):
    class Meta:
        model = History
        fields = ['wallet','DateTime','user','count']



