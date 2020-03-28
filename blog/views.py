from django.shortcuts import render,redirect
# Create your views here.
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from .models import Post
from .forms import RegForm,LoginForm,CreationForm
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import views as a_views


def home(request):
	return HttpResponse(render(request,"blog/home.html",{"post_list":Post.objects.order_by("-pub_date")}))

def register(request):
	if(request.method=="POST"):
		form=RegForm(request.POST)
		print(form.is_valid())
		if form.is_valid():
			form.save()
			messages.success(request,f'New user-{username} created succesfully')
			return redirect('blog-home')
		else:
			messages.warning(request,f'Details entered are invalid.Please enter valid details.')
			return redirect('register')

	else:
		form=RegForm()
		return render(request,'blog/register.html',{"form":form})

def login_generic(request):
	if request.user.is_authenticated:
		return a_views.LoginView.as_view(template_name="blog/login.html")
	else:
		messages.info(request,f'You are already logged in.Please logout to login fron another account')
		return redirect('dashboard')


def login1(request):
	if not request.user.is_authenticated:
		if(request.method=="POST"):
			password=request.POST['password']
			username=request.POST['username']

			user=authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('dashboard')
			else:
				messages.warning(request,f'Please enter valid username and password')
				return redirect('login2')
			
		return render(request,'blog/login2.html')
	messages.info(request,f'You are already logged in.Please logout to login fron another account')
	return redirect('dashboard')

@login_required
def logout1(request):
	logout(request)
	return render(request,'blog/logout.html')


class PostDetail(DetailView):
	model=Post
	context_object_name='post'


def CreatePost(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			form=CreationForm(request.POST)
			if form.is_valid():
				post=form.save(commit=False)
				post.user=request.user
				post.save()
				return redirect('dashboard')
			messages.warning(request,f'Please enter valid fields')
			return redirect('create2')

		else:
			form=CreationForm()
			return render(request,"blog/post_create_2.html",{'form':form})
	else:
		messages.warning(request,f'You have to login before creating a post')
		return redirect('login')



class PostCreate(LoginRequiredMixin,CreateView):
	model=Post
	fields=['title','content']

	def form_valid(self,form):
		form.instance.user=self.request.user
		return super().form_valid(form)


class PostUpdate(LoginRequiredMixin,UpdateView, UserPassesTestMixin):
	model=Post
	fields=['title','content']
	template_name_suffix="_edit"

	def form_valid(self,form):
		form.instance.user=self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user==post.user:
			return True
		return False

class PostDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model=Post
	success_url=reverse_lazy('dashboard')

	def test_func(self):
		post=self.get_object()
		if self.request.user==post.user:
			return True
		return False


@login_required
def dashboard(request):
	cuser=request.user
	post_list=Post.objects.all().filter(user=cuser)
	return render(request,'blog/dashboard.html',{"post_list":post_list})










