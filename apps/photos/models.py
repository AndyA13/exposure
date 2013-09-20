from django.db import models
from django.dispatch import receiver

from easy_thumbnails.signals import saved_file
from easy_thumbnails.files import generate_all_aliases


class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="uploads")


@receiver(saved_file)
def generate_thumbnails_async(sender, fieldfile, **kwargs):
    print "Generating thumbnail."
    instance = sender._default_manager.get(pk=fieldfile.instance.pk)
    fieldfile = getattr(instance, fieldfile.field.name)
    generate_all_aliases(fieldfile, include_global=True)