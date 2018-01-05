from django.urls import path,re_path
from . import views

urlpatterns = [
	
	
	path('',views.index,name='index'),
	#path('bintang/<int:no>/<str:film>',views.bintang,name='bintang'),
	path('browse',views.browsea,name='browsea'),
	path('browse/<int:thn>',views.browset,name='browset'),
	path('browse/<str:gnr>',views.browseg,name='browseg'),
	path('login',views.login,name='login'),
	path('daftar',views.register,name='register'),
	path('logout',views.logout,name='logout'),
	path('about',views.about,name='about'),
	path('movie/<str:filmid>',views.content,name='content'),
]
