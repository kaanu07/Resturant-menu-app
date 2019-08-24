
from django.conf.urls import url
#from restaurants.views import ContactView, HomeView, AboutView
from .views import (
	#restaurant_listView,
	RestaurantListView,
	RestaurantDetailView,
	#restaurant_createview,
	RestaurantCreateView,
    RestaurantUpdateView
    )
urlpatterns = [
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
    #url(r'^restaurants/create/$', restaurant_createview) ,
    #url(r'^(?P<slug>[\w-]+)/edit/$', RestaurantUpdateView.as_view(), name='edit'),
    #url(r'^(?P<rest_id>\w+)/$', RestaurantDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name='detail'),
    url(r'$', RestaurantListView.as_view(), name='list'),

]
