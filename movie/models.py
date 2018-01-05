from django.db import models

# Create your models here.

class Film(models.Model):
	film_id = models.CharField(max_length=5,primary_key=True)
	judul = models.CharField(max_length=100)
	genre = models.ManyToManyField('Genre',blank=True)
	tahun = models.IntegerField()
	ket = models.CharField(max_length=100)
	gmr = models.FileField()
	def __str__(self):
		return self.judul;
	def getrating(self):
		nilai = 0
		data = self.rating_set.all()
		if data.count()>0:
			for a in data:
				nilai += a.nilai
			nilai = nilai / data.count()
		return round(nilai,2)
			
			
class Genre(models.Model):
	genre_id = models.CharField(max_length=2,primary_key=True)
	nama_genre = models.CharField(max_length=20)
	ket = models.CharField(max_length=100,blank=True)
	def __str__(self):
		return self.nama_genre

class Pengunjung(models.Model):
	pengunjung_id = models.CharField(max_length=16,primary_key=True)
	first_name = models.CharField(max_length=10)
	last_name = models.CharField(max_length=10)
	password = models.CharField(max_length=30)
	def __str__(self):
		return (self.first_name + ' ' + self.last_name)

class rating(models.Model):
	film = models.ForeignKey('Film',on_delete=models.CASCADE)
	pengunjung = models.ForeignKey('Pengunjung',on_delete=models.CASCADE)
	nilai = models.IntegerField()
