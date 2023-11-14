from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import User
from .forms import UserCreateForm, UserUpdateForm
from django.shortcuts import get_object_or_404
# Create your views here.

class List(TemplateView):
    template_name = "users.html"

    def get(self, request):
        users = User.objects.all()
        ctx = {
            'users': users,
        }
        return render(request, self.template_name, ctx)
        
    def post(self, request):
       template = "main_entry.html" 
       # if 'search' in request.POST:
       #     template = "result.html"  
       #     query = request.POST['search']
       #     result_list = User.objects.filter(id = query)
       #     if result_list.count() != 0:
    	  #      	context = {
    	  #      		'result_list': result_list,
    	  #      		'query': query,
    	  #      	}
       #     else:
       #     		context = {
       #     			'empty': "Nothing founded. 404!",
       #     			'query': query,
       #     		}
       

       # if 'deluser' in request.POST:
       #     query = request.POST['deluser']
       #     User.objects.filter(id = query).delete()
       #     users = User.objects.all()
       #     context = {
       #              'users': users,
       #          } 
 
       # if 'upduser' in request.POST:
       #     query = request.POST['upduser']
       #     usr = User().objects.get(id = query)
       #     usr.address = request.POST.get("address")
       #     usr.phone  = request.POST.get("phone")
       #     usr.save()
       #     users = User.objects.all()
       #     context = {
       #      'users': users,
       #      }
       return render(request, template, context)

class MainView(TemplateView):
	template_name = "main_entry.html"

	def get(self, request):
		# if request.user.is_authenticated:
			users = User.objects.all()
			ctx = {}
			ctx['users'] = users
			return render(request, self.template_name, ctx)
		# else:
  #           users = User.objects.all()
  #           ctx = {}
  #           ctx['users'] = users
  #           return render(request, self.template_name, ctx)


class LoginFormView(FormView):
	form_class = AuthenticationForm

	template_name = "login.html"

	success_url = "../"

	def form_valid(self, form):

		self.user = form.get_user()

		login(self.request, self.user)
		return super(LoginFormView, self).form_valid(form)
		


class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponseRedirect("/#")

class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "../"

    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):

        return super(RegisterFormView, self).form_invalid(form)

def updateUser(request, pk):

    user = get_object_or_404(User, id = pk)
    if (request.user.position != 'director' and request.user.position != 'associate director'):
        return redirect('/')
    form = UserUpdateForm(request.POST or None, instance = user)

    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form}    
    return render(request, 'update.html', context)

def deleteUser(request, pk):
    user = User.objects.get(id=pk)

    if request.method == "POST":
        user.delete()
        return redirect('/')

    context = {'item':user}
    return render(request, 'delete.html', context)