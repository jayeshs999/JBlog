from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse




class Post(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	content=models.TextField(max_length=1000)
	likes=models.IntegerField(default=0)
	pub_date=models.DateTimeField(default=timezone.now)

	def get_absolute_url(self):
		return reverse('dashboard')




