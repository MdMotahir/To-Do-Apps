from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    email=forms.EmailField()
    confirm_email=forms.EmailField()
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','username','email','confirm_email','password1','password2')
        
    def clean(self):
        cleaned_data=super().clean()
        if cleaned_data.get('email') != cleaned_data.get('confirm_email'):
            raise forms.ValidationError('Your Email and Confirm Email is not match',code='Invalid')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','username','email')
    