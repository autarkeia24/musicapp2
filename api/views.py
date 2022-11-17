from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArtisteSerializer, SongSerializer
from musicapp.models import Artiste, Song
from rest_framework import status


@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': '/api/songs'},
        {'GET': '/api/artistes'},
        {'GET': '/api/songs/id'},
        {'PUT': '/api/songs/id'},
        {'DELETE': '/api/songs/id'},
    ]
    return Response(routes)


@api_view(['GET'])
def get_artistes(request):
    artistes = Artiste.objects.all()
    artiste_serializer = ArtisteSerializer(artistes, many=True)
    return Response(artiste_serializer.data)


@api_view(['GET'])
def get_songs(request):
    songs = Song.objects.all()
    song_serializer = SongSerializer(songs, many=True)
    return Response(song_serializer.data)


@api_view(['GET'])
def get_single_song(request, pk):
    single_song = Song.objects.get(id=pk)
    single_song_serializer = SongSerializer(single_song, many=False)
    return Response(single_song_serializer.data)


@api_view(['DELETE'])
def delete_song(request, pk):
    single_song = Song.objects.get(id=pk)
    single_song.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_song(request, pk):
    single_song = Song.objects.get(id=pk)
    return Response(status=status.HTTP_204_NO_CONTENT)
