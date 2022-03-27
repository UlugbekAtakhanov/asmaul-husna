from django.db import models
from django.utils.translation import gettext_lazy

# Create your models here.

def upload_to(instance, filename):
    return 'posts/images/{filename}'.format(filename=filename)



class Audios(models.Model):
    audio_id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=250, default="asmaul-husna")
    image = models.ImageField(gettext_lazy("Image"), upload_to=upload_to, default=None)
    audio = models.FileField(upload_to=upload_to, default=None)
