from django import forms

from .models import User


from django.contrib.auth.forms import UserCreationForm


#
# class UserCreationForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']


    # def clean_username(self, request, *args, **kwargs):
    #
    #     return None
