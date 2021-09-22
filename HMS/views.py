from django.shortcuts import render, get_object_or_404
from .models import Room, Booking
from django.views import generic
from .forms import RoomForm, CreateBookingForm, NewUserForm
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.db.models import Q
from django.http import HttpResponseRedirect



class RegisterView(generic.CreateView):
    template_name = 'HMS/register.html'
    form_class = NewUserForm
    success_url = reverse_lazy('HMS:login')


class LoginView(auth_views.LoginView):
    template_name = 'HMS/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
     template_name = 'HMS/login.html'


class RoomListView(LoginRequiredMixin, generic.ListView):
    template_name = 'HMS/room_list.html'
    #model = Room
    queryset = Room.objects.all()
    context_object_name = 'room_list'

    #def get_queryset(self):
    #    return self.queryset


class BookingListView(LoginRequiredMixin, generic.ListView):
    template_name = 'HMS/booking_list.html'
    queryset = Booking.objects.all()
    context_object_name = 'booking_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_ = self.kwargs.get("pk")
        #room = Room.objects.get(number=id_)
        #context['room'] = Room.objects.get(number=id_)
        context['booking_list'] = Booking.objects.all()
        context['user'] = self.request.user
        return context

    def post(self, request):
        search_checkin = request.POST['search-checkin']
        search_checkout = request.POST['search-checkout']
        bookings_list = Booking.objects.filter((Q(check_in__gte=search_checkin) & Q(check_in__lte=search_checkout))
                                               | (Q(check_out__gte=search_checkin) & Q(check_out__lte=search_checkout)))
        user = self.request.user
        return render(request, 'HMS/booking_list.html', {
            'search_checkin': search_checkin,
            'search_checkout': search_checkout,
            'user': user,
            'booking_list': bookings_list,
        })


class RoomDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'HMS/room_detail.html'
    queryset = Room.objects.all()
    context_object_name = 'room'

    # def get_object(self):
    #     id = self.kwargs.get("id")
    #     return get_object_or_404(Room, id=id)


class BookingDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'HMS/booking_detail.html'
    queryset = Booking.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_ = self.kwargs.get("pk")
        #room = Room.objects.get(number=id_)
        context['booking'] = Booking.objects.get(id=id_)
        # context['bookings_list'] = room.booking_set.filter(user=self.request.user)
        context['user'] = self.request.user
        return context


class RoomCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'HMS/room_create.html'
    form_class = RoomForm
    queryset = Room.objects.all()


class BookingCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'HMS/booking_create.html'
    form_class = CreateBookingForm
    queryset = Booking.objects.all()
    #success_url = reverse_lazy('HMS:booking_list')

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid:
    #         obj = form.save(commit=False)
    #         obj.user = request.user
    #         obj.save()
    #         form = self.form_class()
    #     return render(request, 'HMS/booking_create.html', {'form': form})
    #     #return reverse("HMS:booking_detail", kwargs={"pk": obj.id})

    def get_form_kwargs(self):
        kwargs = super(BookingCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return reverse("HMS:booking_detail", kwargs={"pk": self.object.id})



class AllUserBookingsView(LoginRequiredMixin, generic.ListView):  # this view shows all the bookings by the current user
    template_name = 'HMS/all_user_bookings.html'
    context_object_name = 'user_bookings_list'
    # queryset = Booking.objects.filter(user=self.request.user)

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class RoomUserBookingsView(LoginRequiredMixin, generic.ListView):  # this view shows all the bookings by a current user for a specific room
    template_name = 'HMS/room_user_bookings.html'
    model = Room
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #user = self.request.user
        id_ = self.kwargs.get("pk")
        room = Room.objects.get(number=id_)
        context['room'] = Room.objects.get(number=id_)
        context['bookings_list'] = room.booking_set.filter(user=self.request.user)
        context['user'] = self.request.user
        return context

    # def get_queryset(self):
        #     id_ = self.kwargs.get("pk")
        #     room = Room.objects.get(number=id_)
        #     return room


class AllRoomBookingsView(LoginRequiredMixin, generic.ListView): # all bookings by all users for a specific room
    template_name = 'HMS/all_bookings_for_room.html'
    context_object_name = 'room'
    model = Room

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_ = self.kwargs.get("pk")
        room = Room.objects.get(number=id_)
        context['room'] = Room.objects.get(number=id_)
        context['bookings_list'] = room.booking_set.all()
        context['user'] = self.request.user
        return context


class BookingDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    template_name = 'HMS/booking_delete.html'
    #model = Booking
    context_object_name = 'booking'
    success_url = reverse_lazy('HMS:booking_list')

    def get_object(self):
        id_ = self.kwargs.get("pk")
        booking = Booking.objects.get(id=id_)
        if not booking.user == self.request.user:
            raise Http404
        return booking


class BookingUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    template_name = 'HMS/booking_update.html'
    context_object_name = 'booking'
    form_class = CreateBookingForm
    #success_url = reverse_lazy('HMS:booking_detail')

    def get_object(self):
        id_ = self.kwargs.get("pk")
        booking = Booking.objects.get(id=id_)
        if not booking.user == self.request.user:
            raise Http404
        return booking

    def get_form_kwargs(self):
        kwargs = super(BookingUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        kwargs['object'] = self.object
        return kwargs

    def get_success_url(self):
        return reverse("HMS:booking_detail", kwargs={"pk": self.object.id})
    # fields = [
    #     "room",
    #     "check_in",
    #     "check_out",
    # ]

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid:
    #         obj = form.save(commit=False)
    #         obj.user = request.user
    #         obj.save()
    #         form = self.form_class()
    #     return render(request, 'HMS/booking_update.html', {'form': form})
