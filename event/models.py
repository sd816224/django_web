from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name=models.CharField('Venue Name', max_length=120)
    address=models.CharField(max_length=120)
    postcode=models.CharField('Postcode',max_length=15)
    phone=models.CharField('Contact Phone',max_length=120,blank=True)
    web=models.URLField('Weibsite Address',blank=True)
    email=models.EmailField('Email Address',blank=True)

    def __str__(self):
        return self.name

class MyClubUser(models.Model):
    first_name=models.CharField('Fisrt Name', max_length=120)
    last_name=models.CharField('Last Name', max_length=120)
    email=models.EmailField('User Email')

    def __str__(self):
        return self.first_name+' '+self.last_name


class Event(models.Model):
    name=models.CharField('Event Name', max_length=120)
    event_date=models.DateTimeField('Event Date')
    # venue= models.CharField('Venue',max_length=120)
    venue=models.ForeignKey(Venue,blank=True,null=True,on_delete=models.CASCADE)
    manager=models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    description=models.TextField(blank=True)
    attendees=models.ManyToManyField(MyClubUser,blank=True)

    def __str__(self):
        return self.name

