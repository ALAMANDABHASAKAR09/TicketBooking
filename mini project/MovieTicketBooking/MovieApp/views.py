from django.shortcuts import render,redirect
from . forms import UserForm,MovieForm
from . models import User,Movie
from django.core.mail import send_mail
from MovieTicketBooking import settings
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def homeView(request):
	k = Movie.objects.filter(usmovie_id=request.user.id)
	f = Movie.objects.all()
	cdt = {}
	for j in f:
		cdt[j.id]=j.movie	
		if j.usmovie_id in cdt:
			cdt[j.id]=j.movie,j.moviename,j.language,j.showtime,j.price,cdt[j.usmovie_id]
	return render(request,'html/home.html',{'rj':k,'uj':cdt.values()})
def signupView(request):
	if request.method=="POST":
		g=UserForm(request.POST)
		if g.is_valid():
			g.save()
			return redirect('/login')
	g=UserForm()
	return render(request,'html/signup.html',{'t':g})

def movieView(request):
	h=Movie.objects.filter(usmovie_id=request.user.id)
	if request.method=="POST":
		j=MovieForm(request.POST)
		if j.is_valid():
			c=j.save(commit=False)
			c.usmovie_id=request.user.id 
			c.save()
			return redirect('/movie_list')
	j=MovieForm()
	return render(request,'html/movieslist.html',{'w':j,'s':h})
def movieDeleteView(request,y):
	p=Movie.objects.get(id=y)
	if request.method=="POST":
		p.delete()
		return redirect('/movie_list')
	return render(request,"html/movie_delete.html",{'h':p})
def movieUpdateView(request,w):
	f=Movie.objects.get(id=w)
	if request.method=="POST":
		f.movie=request.POST['r']
		f.moviename=request.POST['n']
		f.language=request.POST['y']
		f.showtime=request.POST['b']
		f.price=request.POST['a']
		f.save()
		return redirect("/movie_list")
	return render(request,'html/movie_update.html',{'s':f})
def about(request):
	return render(request,'html/about.html')
def bookingView(request):
	context  ={
	"Confirmation" : "Ticket Booked Succesfully",
	"Greetings" : "Enjoy your show !",
	}
	if request.method == "POST":
		e = request.POST['email'].split(',')
		s = "Ticket Booked Succesfully"
		d = "Thankyou for booking tickets in our website and hope you come back soon to book again.It's pleasure to have you !.Enjoy Your showtime"
		y = settings.EMAIL_HOST_USER
		z = send_mail(s,d,y,e)
		if z==1:
			messages.success(request,"Your Ticket booked succesfully")
			return redirect('/ticket_booking')
		else:
			return HttpResponse("Not Sent")
	return render(request,'html/booking.html',context)