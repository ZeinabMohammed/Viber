from django.views import generic
from django.views.generic import ListView
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import Authentication
from django.views import generic
from django.views.generic import View
from .forms import *
from django.db.models import Q
# from django.contrib import messages
# from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
class SearchMusicView(ListView):
	model = Album
	template_name = "music/search.html"
	def get_queryset(self, *args, **kwargs):
		qs = Album.objects.all()
		keywords = self.request.GET.get('q', None)
		if keywords is not None:
			qs = qs.filter(
						Q(album_title__icontains=keywords)|
						Q(artist__icontains=keywords))
		return qs
class IndexView(generic.ListView):
	template_name= "music/index.html"

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model 		  = Album
	template_name ="music/detail.html"


class AlbumCreate(CreateView):
	model  = Album
	fields = ["album_title", "artist", "album_logo", "genere"]

class AlbumUpdate(UpdateView):
	model  = Album
	fields = ["album_title", "artist", "album_logo", "genere"]

class AlbumDelete(DeleteView):
	model       = Album
	success_url = reverse_lazy("music:index")

class UserFormView(View):
	form_class    = UserForm
	template_name = "music/register.html"



	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})


	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			#cleaned(normalized data)
			username =form.cleaned_data['username']
			password =form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user= authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect("music:index")
		else:
			print (form.errors)
			return render(request, self.template_name, {'form': form})

			
			
		return render(request, self.template_name, {'form': form})
def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
			"form": form
			}
	# print("user authenticated")
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user 	 = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return(redirect("music:index"))
		else:
		    print("Error!")
		
	return render(request, "music/login.html",context)
def logout_request(request):
	logout(request)
	# messages.info(request, "logged out succesfully!")
	return redirect("music:index")