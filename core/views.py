from django.shortcuts import render
from .models import People
from .serializer import PeopleSerializador
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.
class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializador