from dataclasses import fields
from rest_framework import serializers
from core.models import User, People, Ticket, InTheaters, Session, Seat, Room

class PeopleSerializador(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['cpf','fires_name','last_name','sex','birth_date','phone_number','email']

class UserSerializador(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user','password']

class RoomSerializador(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['identifier','avaliable']

class SeatSerializador(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['row','number','available','room_id']


class SessionSerializador(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['imdb_id','start_time','end_time','day','room_id'] 

class TicketSerializador(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id','session_id','people_id','seat_id'] 


