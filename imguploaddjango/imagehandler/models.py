from django.db import models

# Create your models here.
class Image(models.Model):
	image = models.ImageField(
		blank = True,
		null = True,
		upload_to = 'images/')