from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class userRegisterForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Retype Password'})
        
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
    def save(self, commit=True):
        user = super(userRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            
        return user