from django.db import models

# Create your models here.
class ClarifaiPictureModel(models.Model):
    model_image = models.ImageField(upload_to = 'pic_folder/clarifai')
    uploaded_at = models.DateTimeField(auto_now_add=True)
