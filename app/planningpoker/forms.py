from django import forms


class CreatePollForm(forms.Form):
    name = forms.CharField(
        required=True,
        label='Name',
        widget=forms.URLInput(attrs={
            'placeholder': 'Poll name',
            'autofocus': True,
            'class': 'form-control',
        })
    )

    username = forms.CharField(
        required=True,
        label='Username',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your name',
            'class': 'form-control',
        })
    )
