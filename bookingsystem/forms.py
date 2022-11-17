from django.forms import ModelForm
from django import forms
from .models import Booking, SignUp


class DateInput(forms.DateInput):
    """
    This class provides a widget for use in the
    booking form. It provides a calendar for users
    to pick the booking date from
    """
    input_type = 'date'


class OnlineForm(ModelForm):
    """
    This form is connected with the view
    in order to provide users with the neccessary
    fields for making a booking
    It also provides the labels and placeholder
    text for each field, as wells as the widgets
    and handles validation where required.
    """
    name = forms.CharField(
        label='Booking Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Booking Name'}),
    )

    email_address = forms.EmailField(
        label='Email Address',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email Address'}),
    )

    phone = forms.IntegerField(
        label='Contact Number',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Contact number'}),
    )

    class Meta:
        """Defines which model to pull the
        fields from"""
        model = Booking
        # Tell the form to use all the fields provided
        fields = '__all__'
        # Except fot the user field
        exclude = ('user', )
        widgets = {
            'date': DateInput()
        }


class SignUpForm(ModelForm):
    """
    This form is connected with the Signup view
    so that visiters to the site can sign up
    for the restaurants newsletter.
    It also provides the labels and placeholder
    text for each field, as wells as the widgets
    and handles validation where required.
    """

    first_name = forms.CharField(
        label='First Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
    )

    last_name = forms.CharField(
        label='Last Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
    )

    email_address = forms.EmailField(
        label='Email Adress',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email Adress'}),
    )

    class Meta:
        """Defines which model to pull the
        fields from"""
        model = SignUp
        # Tell the form to use all the fields provided
        fields = ('first_name', 'last_name', 'email_address')
