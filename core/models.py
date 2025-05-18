from django.db import models

# Create your models here.


class Users(models.Model):
	full_name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=15)


class Coords(models.Model):
	latitude = models.DecimalField(max_digits=10, decimal_places=6)
	longitude = models.DecimalField(max_digits=10, decimal_places=6)
	height = models.IntegerField()


class PerewalAdd(models.Model):
	title = models.CharField(max_length=100)
	beauty_title = models.CharField(max_length=100)
	other_title = models.CharField(max_length=100)
	connect = models.CharField(max_length=100)
	add_time = models.DateTimeField(auto_now_add=True)
	summer_level = models.CharField(max_length=20)
	winter_level = models.CharField(max_length=20)
	autumn_level = models.CharField(max_length=20)
	spring_level = models.CharField(max_length=20)
	coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
	users = models.ForeignKey(Users, on_delete=models.CASCADE)


class Image(models.Model):
	image = models.ImageField(upload_to='images/')
	perewal_added = models.ForeignKey(PerewalAdd, on_delete=models.CASCADE)


