from django.db import models

# Create your models here.


class Users(models.Model):
	email = models.EmailField(unique=True)
	family = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	otc = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)


class Coords(models.Model):
	latitude = models.DecimalField(max_digits=10, decimal_places=6)
	longitude = models.DecimalField(max_digits=10, decimal_places=6)
	height = models.IntegerField()


class Level(models.Model):
	summer = models.CharField(max_length=20, blank=True)
	winter = models.CharField(max_length=20, blank=True)
	autumn = models.CharField(max_length=20, blank=True)
	spring = models.CharField(max_length=20, blank=True)


class PerewalAdd(models.Model):

	STATUS_CHOICES = [
		('new', 'Новый'),
		('pending', 'В обработке'),
		('accepted', 'Принятый'),
		('rejected', 'Отклоненный'),
	]

	beauty_title = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	other_title = models.CharField(max_length=100)
	connect = models.CharField(max_length=100, blank=True, null=True)
	add_time = models.DateTimeField()
	status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='new')
	coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
	user = models.ForeignKey(Users, on_delete=models.CASCADE)
	level = models.ForeignKey(Level, on_delete=models.CASCADE)


class Image(models.Model):
	data = models.TextField()
	title = models.CharField(max_length=255)
	perewal_added = models.ForeignKey(PerewalAdd, related_name='images', on_delete=models.CASCADE)

