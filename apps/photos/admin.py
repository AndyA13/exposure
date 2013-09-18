from django.contrib import admin

from photos import models


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)

admin.site.register(models.Photo, PhotoAdmin)
