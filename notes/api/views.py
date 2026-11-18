from django.shortcuts import render
from .serializers import NoteSerializer
from notes.models import Note
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

# Create your views here.

class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer