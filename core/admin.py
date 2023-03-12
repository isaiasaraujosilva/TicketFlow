from django.contrib import admin
from core.models import People, User,Room, Seat, Ticket, InTheaters, Session

# Register your models here.


# admin.site.register(People)
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Seat)
admin.site.register(Ticket)
admin.site.register(Session)


@admin.register(People)
class PeopleAdmin (admin.ModelAdmin):
    list_display = ('cpf','fires_name','last_name','sex','birth_date','phone_number','email')
    

# class UserAdmin(admin.ModelAdmin):
#     admin.site.register(User)

# class RoomAdmin(admin.ModelAdmin):
#     

# class SeatAdmin(admin.ModelAdmin):
#     

# class TicketAdmin(admin.ModelAdmin):
#     

# class SessionAdmin(admin.ModelAdmin):
#     
