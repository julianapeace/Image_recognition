import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect
from urllib.parse import urlparse

# Clarifai Set Up
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai_api.forms import *

CLARIFAI_API_KEY = os.environ.get('CLARIFAI_API_KEY', None)

def upload(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            # classify_url(url)
    else:
        form = URLForm()
    return render(request, 'u_form.html', {'form':form})

def upload_handler(request):
    return render(request, 'u_form.html', context={'api_key': CLARIFAI_API_KEY})

def classify_url(url):
    app = ClarifaiApp(api_key=CLARIFAI_API_KEY)
    model = app.models.get("general-v1.3")
    res = model.predict_by_url(url=url)
    output = res['outputs'][0]
    model = output['model']['name']
    image = output['input']['data']['image']
    data = output['data']['concepts']
    print(f'Model: {model}')
    print(f'Image: {image}')
    for i in range(0, len(data)):
        print(i,data[i]['name'], data[i]['value'])
