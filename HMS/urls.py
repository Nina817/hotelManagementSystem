from django.urls import path
from .views import(
    RoomListView,
    RoomDetailView,
    RoomCreateView,
    BookingListView,
    BookingDetailView,
    BookingCreateView,
    RegisterView,
    LoginView,
    LogoutView,
    AllUserBookingsView,
    RoomUserBookingsView,
    AllRoomBookingsView,
    BookingDeleteView,
    BookingUpdateView,
)
app_name = 'HMS'

urlpatterns = [
    path('login', LoginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name="register"),
    path('room_list', RoomListView.as_view(), name="room_list"),
    path('room_detail/<int:pk>/', RoomDetailView.as_view(), name="room_detail"),
    path('create/', RoomCreateView.as_view(), name='room_create'),
    path('booking_detail/<int:pk>/', BookingDetailView.as_view(), name="booking_detail"),
    path('booking_list', BookingListView.as_view(), name="booking_list"),
    path('booking_create', BookingCreateView.as_view(), name="booking_create"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('all_user_bookings', AllUserBookingsView.as_view(), name="all_user_bookings"),
    path('room_user_bookings/<int:pk>/', RoomUserBookingsView.as_view(), name="room_user_bookings"),
    path('all_bookings_for_room/<int:pk>/', AllRoomBookingsView.as_view(), name="all_room_bookings"),
    path('booking_delete/<int:pk>/', BookingDeleteView.as_view(), name="booking_delete"),
    path('booking_update/<int:pk>/', BookingUpdateView.as_view(), name='booking_update'),
]
