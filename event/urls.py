
from django.contrib import admin
from django.urls import path
from  django.urls import path, include
from . import views

urlpatterns = [

    path('',views.event,name='event'),
    path('<int:year>/<str:month>/',views.event,name='event'),
    path('all/',views.all_events,name='all_events'),
    path('add_venue/',views.add_venue,name='add_venue'),
    path('all_venues/',views.all_venues,name='all_venues'),
    path('show_venue/<venue_id>',views.show_venue,name='show_venue'),
    path('search_venue/',views.search_venue,name='search_venue'),
]
