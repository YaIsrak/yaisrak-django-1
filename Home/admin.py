from django.contrib import admin
from .models import Pic
# Register your models here.

class PicAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Pic, PicAdmin)