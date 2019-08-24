"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
#from restaurants.views import ContactView, HomeView, AboutView
'''from restaurants.views import (
	restaurant_listView,
	RestaurantListView,
	RestaurantDetailView,
	restaurant_createview,
	RestaurantCreateView
    )'''
urlpatterns = [
    #url(r'^$',include('posts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/',include('posts.urls')),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^u/', include(('profiles.urls', 'profiles') , namespace='profiles')),
    url(r'^items/', include(('menus.urls', 'menus') , namespace='menus')),
    url(r'^restaurants/', include(('restaurants.urls', 'restaurants') , namespace='restaurants')),
    #url(r'^restaurants/$', RestaurantListView.as_view(), name='restaurants'),
    #url(r'^restaurants/create/$', RestaurantCreateView.as_view(), name='restaurants-create'),
    #url(r'^restaurants/create/$', restaurant_createview) ,
    #url(r'^restaurants/(?P<rest_id>\w+)/$', RestaurantDetailView.as_view(), name='restaurant-detail'),
    #url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantListView.as_view(), name='restaurant-detail'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact')

]
