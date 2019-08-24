from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm

'''@login_required()
def restaurant_createview(request):
	form= RestaurantLocationCreateForm(request.POST or None)
	errors = None
	
		#title= request.POST.get("title")
		#location= request.POST.get("location")
		#category= request.POST.get("category")
		
	if form.is_valid():
		#if request.user.is_authenticated():
		instance = form.save(commit=False)
		instance.owner = request.user
		instance.save()
	        #form.save()
	        #''obj= RestaurantLocation.objects.create(
		    #name= form.cleaned_data.get('name'),
		    #location= form.cleaned_data.get('location'),
		    #category= form.cleaned_data.get('category')
		    #)
		return HttpResponseRedirect ("/restaurants/")
		#else:
		#	return HttpResponseRedirect("/login/")
	if form.errors:
		errors= form.errors

	template_name= 'restaurants/form.html'
	context={ "form" : form, "errors" : errors }
	return render(request , template_name, context)


''
# Create your views here.
def home1(request):
	context= { "num" : 5}
	return render(request, "home.html",context)

def about(request):
	context= { "num" : 4}
	return render(request, "about.html",context)

def contact(request):
	context= { "num" : 3}
	return render(request, "contact.html",context)
	#return render(request,"home.html",{})
class ContactView(View):
 	def get(self,request,*args,**kwargs):
 		context={}
 		return render(request, "contact.html",context)

class HomeView(TemplateView):
	template_name='home.html'

	def get_context_data(self,*args, **kwargs):
		context= super(HomeView, self).get_context_data(*args, **kwargs)
		context= { "num" : 5}
		return context

class AboutView(TemplateView):
	template_name='about.html'

class ContactView(TemplateView):
	template_name='contact.html'
	''
def restaurant_listView(request):
	template_name='restaurants/restaurants_list.html'
	queryset=RestaurantLocation.objects.all()
	context={
	    "object_list": queryset
	}
	return render(request,template_name,context)'''

class RestaurantListView(LoginRequiredMixin, ListView):
	#template_name='restaurants/restaurantlocation_list.html'

	def get_queryset(self):
		'''slug = self.kwargs.get("slug")
		if slug:
			queryset=RestaurantLocation.objects.filter(
				Q(category__iexact=slug) |
				Q(category__icontains=slug)
				)
		else:
			queryset=RestaurantLocation.objects.all()'''
		return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)
	'''def get_object(self, *args , **kwargs):
	    rest_id= self.kwargs.get('rest_id')
	    obj= get_object_or_404(RestaurantLocation, id=rest_id)
	    return obj'''
class RestaurantCreateView(LoginRequiredMixin, CreateView):
	form_class = RestaurantLocationCreateForm
	template_name= 'form.html'
	#success_url = "/restaurants/"
	def form_valid(self, form):
		instance= form.save(commit=False)
		instance.owner= self.request.user
		return super(RestaurantCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context= super(RestaurantCreateView,self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Restaurant'
		return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
	form_class = RestaurantLocationCreateForm
	login_url='/login/'
	template_name= 'restaurants/detail-update.html'
	#success_url = "/restaurants/"
	def get_context_data(self, *args, **kwargs):
		context= super(RestaurantUpdateView,self).get_context_data(*args, **kwargs)
		context['title'] = 'Update Restaurant'
		return context

	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)

'''class MexicanRestaurantListView(ListView):
	queryset = RestaurantLocation.objects.filter(category__iexact='mexican')
	template_name='restaurants/restaurants_list.html'

class AsianFusionRestaurantListView(ListView):
	queryset = RestaurantLocation.objects.filter(category__iexact='asian fusion')
	template_name='restaurants/restaurants_list.html'
'''