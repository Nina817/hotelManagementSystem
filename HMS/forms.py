from django import forms
from .models import Room, Booking
from HMS.booking_functions.availability import is_room_available
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2'
        ]


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'number'
        ]

    def clean_number(self, *args, **kwargs):
        number = self.cleaned_data.get("number")
        if Room.objects.filter(number=number).exists():
            raise forms.ValidationError("This room already exists")
        else:
            return number


class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'room',
            'check_in',
            'check_out'
        ]

    check_in = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    check_out = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    # check_in = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget())
    # check_out = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget())


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)
        super(CreateBookingForm, self).__init__(*args, **kwargs)


    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")
        room = cleaned_data.get("room")


        if check_in and check_out:
            if is_room_available(room, check_in, check_out, self.object) == False:
                raise ValidationError("This room is not available for these dates")
            if check_out < check_in:
                raise ValidationError("Your check in time must be before your checkout time")

    def save(self, commit=True):
        booking = super(CreateBookingForm, self).save(commit=False)
        booking.user = self.request.user
        booking.save()
        return booking
