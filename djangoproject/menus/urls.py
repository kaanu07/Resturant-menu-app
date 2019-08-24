
from django.conf.urls import url
#from restaurants.views import ContactView, HomeView, AboutView
from .views import (
    ItemCreateView,
    ItemDetailView,
    ItemListView,
    ItemUpdateView
	)
urlpatterns = [
    
    url(r'^create/$', ItemCreateView.as_view(), name='create'),
    #url(r'^restaurants/create/$', restaurant_createview) ,
    #url(r'^(?P<rest_id>\w+)/$', RestaurantDetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/edit/$', ItemUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='detail'),
    url(r'$', ItemListView.as_view(), name='list'),
]
