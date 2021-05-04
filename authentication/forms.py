from django.contrib.auth.forms import UserCreationForm
from django import forms

from authentication.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length=100, required=True)
    lastname = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ("firstname", "lastname", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
