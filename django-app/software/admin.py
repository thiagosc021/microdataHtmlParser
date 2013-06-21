from django.contrib import admin
from software.models import Software
from software.models import Screenshot
from software.models import Link
from software.models import Image
from software.models import Review

class ScreenshotInline(admin.TabularInline):
  model = Screenshot
  extra = 1
  
class LinkInline(admin.TabularInline):
  model = Link
  extra = 1
  
class ImageInline(admin.TabularInline):
  model = Image
  extra = 1
  
class ReviewInline(admin.TabularInline):
  model = Review
  extra = 1

class SoftwareAdmin(admin.ModelAdmin):
  fields = ['name', 'text', 'downloadUrl', 'applicationSubCategory']
  inlines = [ScreenshotInline,LinkInline,ImageInline,ReviewInline]
   
admin.site.register(Software,SoftwareAdmin)