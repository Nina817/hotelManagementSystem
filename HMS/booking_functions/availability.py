from HMS.models import Room, Booking
import datetime

# get data to input into function from booking form?? Can create a booking form where you'll input room number, and checkin/out dates
#or maybe will already know room because you will access booking form from that room's page??


def is_room_available(room, new_check_in, new_check_out, object):
    current_bookings = Booking.objects.filter(room=room)
    for booking in current_bookings:
        if object != booking:
            if (new_check_in > booking.check_out) or (new_check_out < booking.check_in): # if the new check in time is after
                continue  # booking doesn't clash with older bookings
            else:
                return False
    return True


        # if (new_check_in > booking.check_in) and (new_check_in< booking.check_out):
        #     return False # room is not available
        # elif (new_check_in < booking.check_in) and (new_check_out > booking.check_in):
        #     return False # room is not availble
        # else:
        #     return True

# def check_availability(room, check_in, check_out):
#     avail_list =  []
#     booking_list = Booking.objects.filter(room=room)
#     for booking in booking_list:
#         if booking.check_in > check_out or booking.check_out < check_in:
#             avail_list.append(True)
#         else:
#             avail_list.append(False)
#     return all(avail_list) #all function - returns true if all items in list are true