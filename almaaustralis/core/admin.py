from django.contrib import admin
from import_export import resources
from .models import *
from import_export.admin import ImportExportModelAdmin

class SocialNetworksResourse(resources.ModelResource):
    class Meta:
        model = SocialNetworks

class TextInfoResourse(resources.ModelResource):
    class Meta:
        model = TextInfo

class CarouselResourse(resources.ModelResource):
    class Meta:
        model = Carousel

class SocialNetworksAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("name", "link",  "active")
    resource_class = SocialNetworks

class TextInfoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("title", "url_image")
    resource_class = TextInfo

class CarouselAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("active", "info", "url_image")
    resource_class = Carousel

admin.site.register(SocialNetworks, SocialNetworksAdmin)
admin.site.register(TextInfo, TextInfoAdmin)
admin.site.register(Carousel, CarouselAdmin)
