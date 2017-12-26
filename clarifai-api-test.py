from clarifai import rest
from clarifai.rest import ClarifaiApp
import json

CLARIFAI_API_KEY = "e52b9ec7a4aa43869d653557cd05abf5"

app = ClarifaiApp(api_key=CLARIFAI_API_KEY)

# get the general model
model = app.models.get("general-v1.3")

# predict with the model
res = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
output = res['outputs'][0]
model = output['model']['name']
image = output['input']['data']['image']
data = output['data']['concepts']

print(f'Model: {model}')
print(f'Image: {image}')
for i in range(0, len(data)):
    print(i,data[i]['name'], data[i]['value'])
