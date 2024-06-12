from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api1.permissions import IsOwnerOrReadOnly
from .models import Artist
from .serializers import ArtistSerializer


class ArtistList(APIView):
    """
    List all artists.

    """
    def get (self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)
   