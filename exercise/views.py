from .models import Post, ExerciseGroup
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, MakeGroupForm, JoinGroupForm
from django.utils import timezone
from django.contrib.auth.models import User, Group
##
from django.http import HttpResponse
# Create your views here.
def home(request):
	grouplist = Group.objects.all()
	return render(request, 'home.html', {'grouplist': grouplist})

@login_required(login_url='login')
def new_post(request):
	
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('feed')
	else:
		form = PostForm()

	return render(request, 'new_post.html', {'form': form})

@login_required(login_url='login')
def feed(request):
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')[:50]
	return render(request, 'feed.html', {'posts': posts})

@login_required(login_url='login')
def create_group(request):
	if request.method == "POST":
		form = MakeGroupForm(request.POST)
		if form.is_valid():
			group = form.save(commit=False)
			group.save()
			request.user.groups.add(Group.objects.get(name=group.name))
			return redirect('feed')
	else:
		form = MakeGroupForm()

	return render(request, 'create_group.html', {'form': form})

@login_required(login_url='login')
def join_group(request):
	if request.method == "POST":
		form = JoinGroupForm(request.POST)

		if form.is_valid():
			add_groups = request.POST.getlist('form')
			for groupid in add_groups:
				request.user.groups.add(Group.objects.get(pk=groupid))
			#import pdb; pdb.set_trace()
			return redirect('home')
	else:
		form = JoinGroupForm()	

	return render(request, 'join_group.html', {'form': form})