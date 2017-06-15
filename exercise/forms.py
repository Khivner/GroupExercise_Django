from django import forms
from .models import Post
from django.contrib.auth.models import Group, User
from django.forms import ModelChoiceField


class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('exercise', 'reps', 'weight',)

class MakeGroupForm(forms.ModelForm):

	class Meta:
		model = Group
		fields = ('name',)

class JoinGroupForm(forms.Form):
	form = forms.ModelMultipleChoiceField(queryset=Group.objects.all().order_by('name'), label='Group')