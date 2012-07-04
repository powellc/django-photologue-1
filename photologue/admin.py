from django.contrib import admin
from django import forms
from django.core.urlresolvers import reverse

from models import *

from tinymce.widgets import TinyMCE

class GalleryAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GalleryAdminForm, self). __init__(*args, **kwargs)
        # Note: the reverse() cannot be run when the module is first loaded 
        # (need to wait for urlconf urls to be populated) so the description
        # field - with the reverse() - has to be loaded at this late stage.
        self.fields['description'] = forms.CharField(widget=\
            TinyMCE(attrs={'cols': 80, 'rows': 15},
                    mce_attrs={'external_image_list_url': \
                                               reverse('pl-photo-tinymce-list')}
            ))
        return

    class Meta:
        model = Gallery

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'photo_count', 'is_public')
    list_filter = ['date_added', 'is_public']
    date_hierarchy = 'date_added'
    prepopulated_fields = {'title_slug': ('title',)}
    filter_horizontal = ('photos',)
    form = GalleryAdminForm

class PhotoAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PhotoAdminForm, self). __init__(*args, **kwargs)
        self.fields['caption'] = forms.CharField(widget=\
            TinyMCE(attrs={'cols': 80, 'rows': 15},
                    mce_attrs={'external_image_list_url': \
                                               reverse('pl-photo-tinymce-list')}
            ))
        return

    class Meta:
        model = Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_taken', 'date_added', 'is_public', 'tags', 'view_count', 'admin_thumbnail')
    list_filter = ['date_added', 'is_public']
    search_fields = ['title', 'title_slug', 'caption']
    list_per_page = 10
    prepopulated_fields = {'title_slug': ('title',)}
    actions = None
    form = PhotoAdminForm

class PhotoEffectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'color', 'brightness', 'contrast', 'sharpness', 'filters', 'admin_sample')
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Adjustments', {
            'fields': ('color', 'brightness', 'contrast', 'sharpness')
        }),
        ('Filters', {
            'fields': ('filters',)
        }),
        ('Reflection', {
            'fields': ('reflection_size', 'reflection_strength', 'background_color')
        }),
        ('Transpose', {
            'fields': ('transpose_method',)
        }),
    )

class PhotoSizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'width', 'height', 'crop', 'pre_cache', 'effect', 'increment_count')
    fieldsets = (
        (None, {
            'fields': ('name', 'width', 'height', 'quality')
        }),
        ('Options', {
            'fields': ('upscale', 'crop', 'pre_cache', 'increment_count')
        }),
        ('Enhancements', {
            'fields': ('effect', 'watermark',)
        }),
    )


class WatermarkAdmin(admin.ModelAdmin):
    list_display = ('name', 'opacity', 'style')


class GalleryUploadAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False # To remove the 'Save and continue editing' button


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryUpload, GalleryUploadAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoEffect, PhotoEffectAdmin)
admin.site.register(PhotoSize, PhotoSizeAdmin)
admin.site.register(Watermark, WatermarkAdmin)
