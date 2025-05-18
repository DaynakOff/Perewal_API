from django.utils import timezone
from .models import Coords, PerewalAdd, Image


class DataManager:
	def __init__(self):
		pass


	def save_perewal(self, data):

		# создаем координаты
		coords = Coords.objects.create(
			latitude=data['latitude'],
			longitude=data['longitude'],
			height=data['height'])

		# создаем перевал
		perewal = PerewalAdd.objects.create(
			title=data['title'],
			beauty_title=data['beauty_title'],
			other_title=data.get('other_title',''),
			connect=data.get('connect', ''),
			add_time=data.get('add_time', timezone.now()),
			summer_level=data['summer_level'],
			winter_level=data['winter_level'],
			autumn_level=data['autumn_level'],
			spring_level=data['spring_level'],
			coords=coords)

		# добавляем изображения
		for img in data.get('images', []):
			Image.objects.create(
				image=img,
				perewal_added=perewal)

		return perewal.id
