from django.urls import path

from watson_api.views import *

urlpatterns = [
  path('upload_handle/', upload_handle , name="upload_handle"),
]
