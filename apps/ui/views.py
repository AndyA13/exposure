from django.shortcuts import render

def home(request):

    return render(request, 'home.html')

def photoset(request):

	return render(request, 'photoset.html')

def photo(request):

	return render(request, 'photo.html')