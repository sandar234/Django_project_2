from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, \
    PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User



class AuthenticationNewForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your password'})


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'form-control',
                                                       'placeholder': 'Please enter your first name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder': 'Please enter your last name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder': 'Please enter your email'})

        self.fields['password1'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder': 'Please enter your password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder': 'Please enter your password confirmation'})



class NewPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your old password'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your new password'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter once more your new password'})



class NewPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your email'})



class NewSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["new_password1"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your new password1'})
        self.fields["new_password2"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your new password2'})
