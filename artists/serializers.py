from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Artist
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name', 
            'content', 'image'
        ]