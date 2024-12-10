from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
	STATUS_CHOICES = (


		('draft','draft'),
		('published','published'),


	)

	title = models.CharField(max_length=200,null=True,blank=True,)
	content = models.TextField(null=True,blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	slug = models.SlugField(unique=True,null=True,blank=True,allow_unicode=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft',null=True,blank=True)

	def __str__(self):
		return self.title

