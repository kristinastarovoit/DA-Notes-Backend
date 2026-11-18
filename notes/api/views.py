from django.shortcuts import render
from .serializers import NoteSerializer
from notes.models import Note
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view()
def notes_view(request):
    if request.method == "GET":
        markets = Note.objects.all()
        serializer = NoteSerializer(markets, many=True)
        return Response(serializer.data)