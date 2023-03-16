from django.shortcuts import render
from .models import People, User, Room, Seat, Session, Ticket
from .serializer import PeopleSerializador, UserSerializador, RoomSerializador, SeatSerializador, SessionSerializador, TicketSerializador
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView


# Create your views here.
class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializador

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializador

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializador

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializador

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializador


class TickectViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializador

    def delete(self, request, id=None):
        ticket = Ticket.objects.get(id=id)
        ticket.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
# # class MyView(APIView):
# #     def delete(self, request, pk):
# #         # logic for deleting the resource identified by pk
# #         try:
# #             obj = MyModel.objects.get(pk=pk)
# #             obj.delete()
# #             return Response(status=status.HTTP_204_NO_CONTENT)
# #         except MyModel.DoesNotExist:
# #             return Response(status=status.HTTP_404_NOT_FOUND)
