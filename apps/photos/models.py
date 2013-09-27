from datetime import datetime

from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch.dispatcher import receiver

from autoslug import AutoSlugField
from djorm_hstore.fields import DictionaryField
from djorm_hstore.models import HStoreManager
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.signal_handlers import generate_aliases_global
from easy_thumbnails.signals import saved_file

from .exif import file_exif


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
    exif = DictionaryField(db_index=True, editable=False)

    objects = HStoreManager()

    @property
    def size(self):
        return get_thumbnailer(self.image)

    def other_photos_in_set(self):
        return self.photo_set.photo_set.exclude(id__in=[self.id, ])

    def update_exif(self):
        self.exif = file_exif(open(self.image.path))

    def __unicode__(self):
        self.update_exif()

        return self.title


saved_file.connect(generate_aliases_global)


@receiver(post_delete, sender=Photo)
def photo_delete(sender, instance, **kwargs):

    if instance.image:
        instance.image.delete(False)

@receiver(post_save, sender=Photo)
def photo_save(sender, instance, **kwargs):

    if not instance.exif:
        instance.update_exif()
        instance.save()