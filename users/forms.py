from django import forms

#class UserChangePassword(forms.Form):
#    old_password=forms.CharField()
#    new_password=forms.CharField()
#    reenter_password=forms.CharField()
#    def clean(self):
#        new_password=self.cleaned_data.get('new_password')
#        reenter_password=self.cleaned_data.get('reenter_password')
#        #similarly old_password
#        if new_password and new_password!=reenter_password or new_password==old_password:
#        #raise error
#        #get the user object and check from old_password list if any one matches with the new password raise error(read whole answer you would know) 
#            return self.cleaned_data #don't forget this.

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