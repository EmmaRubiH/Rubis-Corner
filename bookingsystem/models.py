from django.db import models
from django.contrib.auth.models import User


# The choice which are presented to people making bookings
TIME_CHOICE = (
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
)

OCCASION_CHOICE = (
    ('Birthday', 'BIRTHDAY'),
    ('Anniversary', 'ANNIVERSARY'),
    ('Graduation', 'GRADUATION'),
    ('Confirmation', 'CONFIRMATION'),
    ('None', 'None'),
)


TABLE_CHOICE = (
    ('Window', 'WINDOW'),
    ('Outside', 'OUTSIDE'),
    ('Inside', 'INSIDE'),
)

NUMBER_OF_PEOPLE_CHOICE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),

)


class Booking(models.Model):
    """
    Model to be used in the forms.py and views.py for the booking form.
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_bookings"
        )
    name = models.CharField(max_length=60, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    number_of_people = models.CharField(max_length=2,
                                        choices=NUMBER_OF_PEOPLE_CHOICE,
                                        blank=False)
    date = models.DateField()
    time = models.CharField(
        max_length=50, choices=TIME_CHOICE, blank=False
        )
    table = models.CharField(
        max_length=50, choices=TABLE_CHOICE, blank=False
        )
    occasion = models.CharField(
        max_length=100, choices=OCCASION_CHOICE, blank=False
        )

    def __str__(self):
        return str(self.name)


class SignUp(models.Model):
    """
    Model to be used in the forms.py for the sign up to newsletter.
    """

    first_name = models.CharField(max_length=60, null=True, blank=True)
    last_name = models.CharField(max_length=60, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)

    def __str__(self):
        return str(self.first_name)
