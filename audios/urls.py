from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path    
from .views import *


urlpatterns = [
    path("", GetAudiosList.as_view(), name = "audios"),
    path("<int:pk>", GetAudio.as_view(), name = "audio")
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # this is for uploading images



