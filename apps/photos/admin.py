from django.contrib import admin

from photos import models


class PhotoSetAdmin(admin.ModelAdmin):
    list_display = ('name', )

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'photo_set', 'created', )

admin.site.register(models.PhotoSet, PhotoSetAdmin)
admin.site.register(models.Photo, PhotoAdmin)
