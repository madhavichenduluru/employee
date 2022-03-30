from django import forms
from django.contrib.auth.models import User
from app_users.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

        labels = {
        'password1':'Password',
        'password2':'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    user1 = 'user1'
    user2 = 'user2'

    user_types = [
        (user1, 'user1'),
        (user2, 'user2'),
    ]
    user_type = forms.ChoiceField(required=True, choices=user_types)

    class Meta():
        model = UserProfileInfo
        fields = ('profile_Pic','user_type')
