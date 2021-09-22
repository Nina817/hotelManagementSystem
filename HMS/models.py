from django.db import models
from django.urls import reverse
from django.conf import settings
from datetime import datetime
from datetime import timedelta
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    # ROOM_CATEGORIES = (
    #     ('YAC', 'AC'),
    #     ('NAC', 'NON-AC'),   # whether room has air con?? won't need for room scheduler
    #     ('DEL', 'DELUXE'),
    #     ('KIN', 'KING'),
    #     ('QUE', 'QUEEN'),
    # )  # in this tuple, the left one is gonna be stored in the database, right one will be what's displayed
    number = models.IntegerField()
    # category = models.CharField(max_length=3, choices=ROOM_CATEGORIES, default='YAC')  # this is for selecting from room categories options above, that's why max 3 char
    # beds = models.IntegerField(default=1)
    # capacity = models.IntegerField(default=1)

    def __str__(self):
        return f'Room No. {self.number}.'  # - {self.category} with {self.beds} beds for {self.capacity} people'

    def get_absolute_url(self):
        #return f"/HMS/{self.id}/"
        return reverse("HMS:room_detail", kwargs={"pk": self.id})


DEFAULT_ROOM_ID =1

class Booking(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=DEFAULT_ROOM_ID)
    check_in = models.DateTimeField(default=datetime.now())
    check_out = models.DateTimeField(default=datetime.now()+timedelta(hours=1))

    def __str__(self):
        return f'Booking {self.id} - {self.user} has booked {self.room} from {self.check_in} to {self.check_out}'

    # def get_absolute_url(self):
    #     return reverse("HMS:booking_detail", kwargs={"pk": self.id})