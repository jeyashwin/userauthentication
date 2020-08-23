from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse 

class Post(models.Model):
	title = models.CharField(max_length=100)
	address = models.CharField(max_length=200, default= True)
	city = models.CharField(max_length=100, default= True)
	zipcode = models.CharField(max_length=20, default = True)
	bedrooms = models.IntegerField(default=True)
	bathrooms = models.IntegerField(default=True)
	garage = models.IntegerField(default=0)
	sqft = models.IntegerField(default=True)
	price = models.IntegerField(default= True)
	content = models.TextField()
	likes = models.ManyToManyField(User, related_name='likes', blank=True)
	dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	photo_main = models.ImageField(upload_to='media_cdn/%Y/%m/%d/',blank=True)
	videofile = models.FileField(upload_to='media_cdn/%Y/%m/%d/',blank=True)
	


	def __str__(self):
		return self.title


	def get_absolute_url(self): 
		return reverse('post-detail', kwargs={'pk': self.pk })




