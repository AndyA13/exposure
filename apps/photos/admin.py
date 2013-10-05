from django.contrib import admin

from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.exceptions import InvalidImageFormatError

from photos import models


class PhotoSetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image_tag', 'photo_set', 'created', 'image_exif')

    def image_tag(self, obj):
        thumbnailer = get_thumbnailer(obj.image)
        try:
            return u'<img src="%s" />' % (thumbnailer['admin'].url)
        except (InvalidImageFormatError, KeyError):
            return ''
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def image_exif(self, obj):
        html = ''
        for key, value in obj.exif.items():
            html += "%s -> %s<br/>" % (key, value)
        return html
    image_exif.short_description = 'Metadata'
    image_exif.allow_tags = True


admin.site.register(models.PhotoSet, PhotoSetAdmin)
admin.site.register(models.Photo, PhotoAdmin)
