from django.urls import path
from . import views
from django.contrib.auth import views as a_views

urlpatterns=[
path("home/",views.home,name='blog-home'),
path("register/",views.register,name='register'),
path("login/",a_views.LoginView.as_view(redirect_authenticated_user=True,template_name="blog/login.html"),name='login'),
path("login2/",views.login1,name='login2'),
path("logout2/",views.logout1,name='logout2'),
path("logout/",a_views.LogoutView.as_view(template_name='blog/logout.html'),name='logout'),
path("dashboard/",views.dashboard,name='dashboard'),
path("post/<int:pk>",views.PostDetail.as_view(),name='detail'),
path("post/create",views.PostCreate.as_view(),name='create'),
path("post/<int:pk>/edit",views.PostUpdate.as_view(),name='update'),
path("post/<int:pk>/delete",views.PostDelete.as_view(),name='delete'),
path("post/create2",views.CreatePost,name='create2')

]