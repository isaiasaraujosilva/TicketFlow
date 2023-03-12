from dataclasses import fields
from rest_framework import serializers
from core.models import User, People, Ticket, InTheaters, Session, Seat

class PeopleSerializador(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['cpf','fires_name','last_name','sex','birth_date','phone_number','email']
