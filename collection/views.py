from django.shortcuts import render
from django.http import Http404

from .models import Album

# Create your views here.

def index(request):
    context = {}
    return render(request, 'collection/index.html', context)

def all(request):
    all_albums = Album.objects.order_by('artist_name')
    if not all_albums:
        raise Http404("There are no albums in the database!")
    else:
        context = { 'all_albums': all_albums}
        return render(request, 'collection/all.html', context)
