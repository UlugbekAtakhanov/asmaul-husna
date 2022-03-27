from rest_framework import generics
from audios.models import Audios
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser


class GetAudiosList(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]
    queryset = Audios.objects.all()
    serializer_class = AudiosSerializer

class GetAudio(generics.RetrieveAPIView):
    serializer_class = AudioSerializer
    queryset = Audios.objects.all()