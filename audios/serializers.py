from rest_framework import serializers
from .models import *

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audios
        fields = "__all__"

        
class AudiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audios
        fields = "__all__"
        