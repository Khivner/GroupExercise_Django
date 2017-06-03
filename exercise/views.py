from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.
def home(request):
	return render(request, 'home.html')

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
