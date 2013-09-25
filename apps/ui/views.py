from django.shortcuts import render, get_object_or_404

from photos.models import Photo, PhotoSet

def home(request):

    photos = Photo.objects.all()

    return render(request, 'home.html', {
        'photo_list': photos
    })

def photo_set(request, photo_set_slug):

    photo_set = get_object_or_404(PhotoSet, slug=photo_set_slug)

    return render(request, 'photoset.html', {
        'photo_set': photo_set,
        'photo_list': photo_set.photo_set.all()
    })

def photo_detail(request, photo_set_slug, photo_slug):

    photo_set = get_object_or_404(PhotoSet, slug=photo_set_slug)
    photo = get_object_or_404(Photo, slug=photo_slug, photo_set=photo_set)

    return render(request, 'photo.html', {
        'photo_set': photo_set,
        'photo': photo,
    })