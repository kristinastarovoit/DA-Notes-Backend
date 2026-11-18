from rest_framework import serializers

class NoteSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=80)
    content = serializers.CharField(max_length=300)
    marked = serializers.BooleanField(default=False)
    trash = serializers.BooleanField(default=False)
