from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User, Group

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	exercise = models.CharField(max_length=100)
	reps = models.IntegerField(default=None, blank=True, null=True)
	weight = models.DecimalField(max_digits=7,decimal_places=2, default=None, blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)

	def publish(self):
		self.save()		

class ExerciseGroup(models.Model):
	groupname = models.CharField(max_length=100)

	@classmethod
	def create(exercisegroup, groupname):
		newgroup = Group.objects.create(name=self.groupname)
