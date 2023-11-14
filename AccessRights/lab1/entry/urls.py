from django.urls import re_path, path
from . import views

urlpatterns = [

	re_path(r'register/$', views.RegisterFormView.as_view()),
	re_path(r'^login/$', views.LoginFormView.as_view()),
	re_path(r'^logout/$', views.LogoutView.as_view()),
	re_path(r'^$', views.MainView.as_view()),
	path('update_user/<str:pk>/', views.updateUser, name="update_user"),
	path('delete_user/<str:pk>/', views.deleteUser, name="delete_user"),

]