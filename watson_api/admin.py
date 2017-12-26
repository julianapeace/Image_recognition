from django.contrib import admin

# Register your models here.
from watson_api.models import *
# Register your models here.

@admin.register(PictureModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('model_image', 'uploaded_at',)
    list_filter = ('model_image', 'uploaded_at',)
    search_fields = ['model_image', 'uploaded_at',]
