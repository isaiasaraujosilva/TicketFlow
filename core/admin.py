from django.contrib import admin
from core.models import People, User,Room, Seat, Ticket, InTheaters, Session

# Register your models here.

class PeopleAdmin (admin.ModelAdmin):
    admin.site.register(People)

class UserAdmin(admin.ModelAdmin):
    admin.site.register(User)

class RoomAdmin(admin.ModelAdmin):
    admin.site.register(Room)

class SeatAdmin(admin.ModelAdmin):
    admin.site.register(Seat)

class TicketAdmin(admin.ModelAdmin):
    admin.site.register(Ticket)

class SessionAdmin(admin.ModelAdmin):
    admin.site.register(Session)
