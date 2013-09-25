from datetime import datetime

from django.db import models

from autoslug import AutoSlugField
from easy_thumbnails.signal_handlers import generate_aliases_global
from easy_thumbnails.signals import saved_file


class PhotoSet(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    image = models.ImageField(upload_to="uploads")
    photo_set = models.ForeignKey(PhotoSet, blank=True, null=True)
    created = models.DateTimeField(default=datetime.now)

    def other_photos_in_set(self):
        return self.photo_set.photo_set.exclude(id__in=[self.id, ])

    def __unicode__(self):
        return self.title

saved_file.connect(generate_aliases_global)