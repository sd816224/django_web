import calendar

from django.shortcuts import render
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event,Venue
from .forms import VenueForm
from django.http import HttpResponseRedirect

# Create your views here.
def event(request,year=datetime.now().year,month=datetime.now().strftime('%B')):
    name='Leee'

    # convert month from name to number
    month=month.title()
    month_number=list(calendar.month_name).index(month)
    month_number=int(month_number)

    #create a calender
    cal=HTMLCalendar().formatmonth(
        year,
        month_number
    )

    #get current year
    now=datetime.now()
    current_year=now.year

    #get current time
    time=now.strftime('%I:%M %p')
    return render(request,'event/home.html',{
        'first_name':name,
        'year':year,
        'month':month,
        "month_number":month_number,
        'cal':cal,
        'current_year':current_year,
        'time':time,

    })

def all_events(request):
    event_list=Event.objects.all()
    return render(request,'event/event_list.html',{
        'event_list':event_list,
    })

def add_venue(request):
    submitted=False
    if request.method=='POST':
        form =VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/event/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted=True

    return render(request,'event/add_venue.html',{'form':form,'submitted':submitted})

def all_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'event/venue_list.html', {
        'venue_list': venue_list,
    })

def show_venue(request,venue_id):
    venue=Venue.objects.get(pk=venue_id)
    return render(request, 'event/show_venue.html', {
        'venue': venue,
    })

def search_venue(request):
    if request.method =='POST':
        searched=request.POST['searched']
        venues=Venue.objects.filter(name__contains=searched)
        return render(request, 'event/search_venue.html',
                      {
                          'searched':searched,
                          'venues':venues
                      })
    else:
        return render(request, 'event/search_venue.html')