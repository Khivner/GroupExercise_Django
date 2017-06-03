from django.db import models
from django.utils import timezone
from datetime import datetime

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	exercise = models.TextField()
	reps = models.IntegerField(default=None, blank=True, null=True)
	weight = models.DecimalField(max_digits=7,decimal_places=2, default=None, blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)

	def publish(self):
		self.save()		
