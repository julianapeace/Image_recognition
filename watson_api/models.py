from django.db import models

# Create your models here.
class PictureModel(models.Model):
    model_image = models.ImageField(upload_to = 'pic_folder/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
