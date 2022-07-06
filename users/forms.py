from unittest.util import _MAX_LENGTH
from django import forms

from users.models import UserProfile

class UserChangePassword(forms.Form):
    old_password = forms.CharField(
                widget=forms.PasswordInput(
                attrs={
                'id': 'old_password',
                'type': 'password',
                'class': 'form-control'
            }
        ))
    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'new_password',
                'type': 'password',
                'class': 'form-control'
            }
        ))
    reenter_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'reenter_password',
                'type': 'password',
                'class': 'form-control'
            }
        ))

    def clean_reenter_password(self):
        cd = self.cleaned_data
        if cd['new_password'] != cd['reenter_password']:
            raise forms.ValidationError('Las Contraseñas no coinciden')
        return cd['reenter_password']


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': 'loginEmail',
                'type': 'email',
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'loginPassword',
            'type': 'password',
            'class': 'form-control',
        })
    )


class UserSignUpForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': 'signupEmail',
                'type': 'email',
                'class': 'form-control'
            }
        )
    )

    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control'
            }
        ))

    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control'
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'signupPassword',
                'type': 'password',
                'class': 'form-control'
            }
        ))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control'
            }
        ))

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las Contraseñas no coinciden')
        return cd['password2']



class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['password','last_login','email','slug','register_date','groups','user_permissions','followers']

    # first_name = forms.CharField(
    #     max_length=100,
    #     widget=forms.TextInput(
    #         attrs={
    #             'type': 'text',
    #             'class': 'form-control'
    #         }
    #     ))

#    last_name = forms.CharField(
#        max_length=100,
#        widget=forms.TextInput(
#            attrs={
#                'type': 'text',
#                'class': 'form-control'
#            }
#        ))

    # profile_pic=forms.ImageField(
    #     )

    # bio = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={
    #             'type': 'text',
    #             'class': 'form-control'
    #         }
    #     ))

    # is_superuser = forms.BooleanField(
    #     widget=forms.CheckboxInput())

    # is_staff = forms.BooleanField(
    #     widget=forms.CheckboxInput())

    # is_active = forms.BooleanField(
    #     widget=forms.CheckboxInput())