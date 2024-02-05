from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
	c=[
		('0','Guest'),
		('1','Customer'),
		('2','TicketAdmin'),
	]
	
	role_type = models.CharField(max_length=5,choices=c,default='0')
	uid=models.CharField(max_length=15)
	has_interest=models.BooleanField(default=False)
	has_movie=models.BooleanField(default=False)

class Movie(models.Model):
	y=[
		('11:00AM-1:30PM','11:00AM-1:30PM'),
		('2:30PM-5:00PM','2:30PM-5:00PM'),
		('5:30PM-8:00PM','5:30PM-8:00PM'),
		('8:30PM-11:00PM','8:30PM-11:00PM'),
	]
	movie=models.CharField(max_length=100)
	moviename=models.CharField(max_length=100)
	language=models.CharField(max_length=100)
	showtime=models.CharField(max_length=100,default='0',choices=y)
	price=models.PositiveIntegerField(default=200)
	is_avail=models.BooleanField(default=True)
	usmovie=models.ForeignKey(User,on_delete=models.CASCADE)
	
	     