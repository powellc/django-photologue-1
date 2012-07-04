#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.views.generic.dates import ArchiveIndexView, DateDetailView, DayArchiveView, MonthArchiveView, YearArchiveView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from photologue.models import Photo, Gallery
from tinymce.views import render_to_image_list

class PhotoView(object):
    queryset = Photo.objects.filter(is_public=True)

class PhotoListView(PhotoView, ListView):
    paginate_by = 20

class PhotoDetailView(PhotoView, DetailView):
    slug_field = 'title_slug'

class PhotoDateView(PhotoView):
    date_field = 'date_added'

class PhotoDateDetailView(PhotoDateView, DateDetailView):
    slug_field = 'title_slug'

class PhotoArchiveIndexView(PhotoDateView, ArchiveIndexView):
    pass

class PhotoDayArchiveView(PhotoDateView, DayArchiveView):
    pass

class PhotoMonthArchiveView(PhotoDateView, MonthArchiveView):
    pass

class PhotoYearArchiveView(PhotoDateView, YearArchiveView):
    pass

def photo_tiny_mce_list(request):
    """Return list of all photos for consumption by tinyMCE widget.
    
    TODO: convert this to class view.
    """
    photos = Photo.objects.filter(is_public=True)
    link_list = [(p.title, p.get_notices_url()) for p in photos]
    return render_to_image_list(link_list)

#gallery Views
class GalleryView(object):
    queryset = Gallery.objects.filter(is_public=True)

class GalleryListView(GalleryView, ListView):
    paginate_by = 20

class GalleryDetailView(GalleryView, DetailView):
    slug_field = 'title_slug'

class GalleryDateView(GalleryView):
    date_field = 'date_added'

class GalleryDateDetailView(GalleryDateView, DateDetailView):
    slug_field = 'title_slug'

class GalleryArchiveIndexView(GalleryDateView, ArchiveIndexView):
    pass

class GalleryDayArchiveView(GalleryDateView, DayArchiveView):
    pass

class GalleryMonthArchiveView(GalleryDateView, MonthArchiveView):
    pass

class GalleryYearArchiveView(GalleryDateView, YearArchiveView):
    pass
