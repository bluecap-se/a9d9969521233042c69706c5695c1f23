from django import forms


class CreatePollForm(forms.Form):
    name = forms.CharField(
        required=True,
        label='Name',
        widget=forms.TextInput(attrs={
            'placeholder': 'Poll name',
            'autofocus': True,
            'class': 'form-control',
        })
    )

    username = forms.CharField(
        required=True,
        label='Username',
        widget=forms.TextInput(attrs={
            'placeholder': 'Your name',
            'class': 'form-control',
        })
    )
