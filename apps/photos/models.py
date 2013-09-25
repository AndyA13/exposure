from datetime import datetime

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver

from autoslug import AutoSlugField
from easy_thumbnails.signal_handlers import generate_aliases_global
from easy_thumbnails.signals import saved_file
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.fields import ThumbnailerImageField


class PhotoSet(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    image = ThumbnailerImageField(upload_to="photos")
    photo_set = models.ForeignKey(PhotoSet, blank=True, null=True)
    created = models.DateTimeField(default=datetime.utcnow)

    @property
    def size(self):
        return get_thumbnailer(self.image)

    def other_photos_in_set(self):
        return self.photo_set.photo_set.exclude(id__in=[self.id, ])

    def __unicode__(self):
        return self.title

saved_file.connect(generate_aliases_global)

@receiver(post_delete, sender=Photo)
def photo_delete(sender, instance, **kwargs):

    if instance.image:
        instance.image.delete(False)