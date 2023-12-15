from main.models import Login
from django import forms
class LoginForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone number, username, or email'}))
    passwordd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Phone number, username, or email'}))
    class Meta:
        model = Login
        fields = ['name','passwordd']
