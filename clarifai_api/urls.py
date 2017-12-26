from django.urls import path
from clarifai_api.views import *

urlpatterns = [
  path('upload/', upload , name="upload"), #this is the url form. takes in input url.
  path('upload_handle', upload_handler, name='upload_handler'), #this handles the url and returns repsonse
]
