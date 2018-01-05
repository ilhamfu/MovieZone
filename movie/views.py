from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from .models import *
from .forms import *
# Create your views here.

islogin = False
useraktif = None

def headbar():
	dtahun = [i for i in range(2020,2005,-1)]
	dgenre = Genre.objects.all()
	konten = {'tahun':dtahun,'genre':dgenre,'islogin':islogin,'user':useraktif}
	return konten

def index(request):
	a = Film.objects.all().order_by('-tahun')
	b = [x.getrating() for x in a]
	dtoplist = list(reversed(sorted(zip(b,a),key=(lambda x: x[0]))))
	dlatest = list(zip(b,a))
	konten = {'top':dtoplist[:8],'latest':dlatest[:8]}
	konten.update(headbar())
	return render(request,"index.html",konten)
	
	
def browsea(request):
	a = Film.objects.all().order_by('-tahun')
	b = [x.getrating() for x in a]
	dtoplist = list(reversed(sorted(zip(b,a),key=(lambda x: x[0]))))
	konten = {'film':dtoplist,'ket':'Daftar Semua Film'}
	konten.update(headbar())
	return render(request,"browse.html",konten)

def browset(request,thn):
	a = Film.objects.filter(tahun=thn)
	b = [x.getrating() for x in a]
	dtoplist = list(reversed(sorted(zip(b,a),key=(lambda x: x[0]))))
	konten = {'film':dtoplist,'ket':'Film pada tahun : ' + str(thn)}
	konten.update(headbar())
	return render(request,"browse.html",konten)
	
def browseg(request,gnr):
	a = Film.objects.filter(genre=gnr)
	b = [x.getrating() for x in a]
	dtoplist = list(reversed(sorted(zip(b,a),key=(lambda x: x[0]))))
	konten = {'film':dtoplist,'ket':'Film dengan genre : ' + str(Genre.objects.get(pk=gnr))}
	konten.update(headbar())
	return render(request,"browse.html",konten)

def content(request,filmid):
	global useraktif
	global islogin
	dfilm = Film.objects.get(pk=filmid)
	nilai = [(x < int(dfilm.getrating())) for x in range(10) ]
	konten = {'film':dfilm,'nilai':nilai}
	konten.update(headbar())
	if islogin:
		nilaiu=0
		if not useraktif.rating_set.filter(film=dfilm):
			tempr = rating(film=dfilm,pengunjung=useraktif,nilai=0)
			tempr.save()
		nilaiu=dfilm.rating_set.get(pengunjung=useraktif).nilai
		konten['nilaiu'] =[((x<nilaiu),x) for x in range(10)]
		if request.GET:
			pos = list(request.GET.keys())[0]
			tempr = rating.objects.get(film=dfilm,pengunjung=useraktif)
			if nilaiu < (int(pos[1])+1):
				tempr.nilai = int(pos[1])+1
				tempr.save()
			elif nilaiu > (int(pos[1])+1):
				tempr.nilai = int(pos[1])+1
				tempr.save()
			return HttpResponseRedirect('/movie/'+filmid)
	return render(request,"content.html",konten)

def login(request):
	global islogin,useraktif
	form = LoginForm(None)
	konten=headbar()
	konten['form'] = form
	if request.method == 'POST':
		form = LoginForm(request.POST)
		temp = Pengunjung.objects.filter(pengunjung_id=request.POST['Username'], password=request.POST['Password'])
		if temp:
			islogin = True
			useraktif = temp[0]
			return HttpResponseRedirect('browse')
		else:
			konten['warning']='Password atau username salah'
	return render(request,"login.html",konten)

def about(request):
	konten=headbar()
	return render(request,"about.html",konten)
	
def logout(request):
	global islogin
	islogin=False
	return HttpResponseRedirect('login')
	
def register(request):
	global useraktif,islogin
	form = RegisterForm(None)
	konten=headbar()
	konten['form'] =form
	if request.method == 'POST':
		newdata = Pengunjung()
		newdata.pengunjung_id = request.POST['Username']
		newdata.password = request.POST['Password']
		newdata.first_name = request.POST['First']
		newdata.last_name = request.POST['Last']
		newdata.save()
		useraktif = newdata
		islogin=True
		return HttpResponseRedirect('browse')
	return render(request,"register.html",konten)

