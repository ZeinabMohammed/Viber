from django.db import models
from django.urls import reverse

class Album(models.Model):
	artist		=	models.CharField(max_length=200)
	album_title	=	models.CharField(max_length=500)
	genere		= 	models.CharField(max_length=100)
	album_logo	= 	models.FileField(max_length=1000)
	link        = models.TextField(null=True)
	
	def __str__(self):
		return(self.album_title+"-" +self.artist)
		
	def get_absolute_url(self):
		return reverse ("music:detail", kwargs={'pk':self.pk})

class song(models.Model):
	album        = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type    = models.CharField(max_length=10)
	song_title   = models.CharField(max_length=200)
	is_favourite = models.BooleanField(default=False)
	def __str__(self):
		return(self.song_title)