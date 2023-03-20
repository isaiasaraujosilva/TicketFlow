from django.shortcuts import render
from .models import People, User, Room, Seat, Session, Ticket
from .serializer import PeopleSerializador, UserSerializador, RoomSerializador, SeatSerializador, SessionSerializador, TicketSerializador
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication


@authentication_classes([JWTAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializador

    def delete(self, request, id=None):
        try:
        
            people = people.objects.get(id=id)
            people.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except people.DoesNotExist:

            return Response(status = status.HTTP_404_NOT_FOUND)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializador

    def delete(self, request, id=None):
        try:
        
            user = User.objects.get(id=id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except user.DoesNotExist:

            return Response(status = status.HTTP_404_NOT_FOUND)
        
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializador

    def delete(self, request, id=None):
        try:
        
            room = Room.objects.get(id=id)
            room.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except room.DoesNotExist:

            return Response(status = status.HTTP_404_NOT_FOUND)
    
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializador

    def delete(self, request, id=None):
        try:
        
            seat = Seat.objects.get(id=id)
            seat.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except seat.DoesNotExist:

            return Response(status = status.HTTP_404_NOT_FOUND)

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializador
    
    def delete(self, request, id=None):
        try:
        
            session = Session.objects.get(id=id)
            session.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except session.DoesNotExist:

            return Response(status = status.HTTP_404_NOT_FOUND)

class TickectViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializador

    def delete(self, request, id=None):
        try:
        
            ticket = Ticket.objects.get(id=id)
            ticket.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except ticket.DoesNotExist:

            return Response(status = status.HTTP_404_NOT_FOUND)