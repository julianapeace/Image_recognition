from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from string import Template #gives u ability to create variables in a string
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from watson_api.models import *
from watson_api.forms import *
import requests

def upload_handle(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = PictureModel.objects.get(pk=course_id)
            m.image = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    else:
        return HttpResponseForbidden('allowed only via POST')

    # return HttpResponse('image upload success')
def index(request):
    all_images = PictureModel.objects.all().values_list('id', 'model_image')
    return render(request, 'index.html', context={'all_images': all_images})














GH_ENDPOINT = 'https://api.github.com/graphql'

def get_all_repos(token, repos=None, after=None):
  if repos is None:
    repos = []

  a = ''
  if after:
    a = 'after: "{}"'.format(after)
  q = """
  query {
    viewer {
      repositories(first: 100 $after orderBy: {field: PUSHED_AT, direction: DESC}) {
        edges{
          node{
            id
            name
            url
            isPrivate
            pushedAt
          }
        }
        pageInfo{
          startCursor
          hasNextPage
          endCursor
        }
      }
    }
  }
  """

  q = Template(q)
  q = q.substitute(after=a)

  headers = {'Authorization': 'bearer ' + token}
  response = requests.post(GH_ENDPOINT, json={'query': q}, headers=headers)
  data = response.json()['data']['viewer']['repositories']

  for edge in data['edges']:
    repos.append(edge['node'])

  if data['pageInfo']['hasNextPage']:
    get_all_repos(token, repos, data['pageInfo']['endCursor'])

  return repos

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_repos (request):
  auth = request.user.social_auth.get()
  return Response(get_all_repos(auth.access_token))
