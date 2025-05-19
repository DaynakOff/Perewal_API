from unittest import registerResult

from rest_framework import serializers
from .models import Users, Coords, PerewalAdd, Image, Level


class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = ['email', 'family', 'name', 'otc', 'phone']


class CoordsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Coords
		fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Level
		fields = '__all__'

	def to_representation(self, obj):
		return {'summer': obj.summer, 'winter': obj.winter, 'autumn': obj.autumn, 'spring': obj.spring}


class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = ['data', 'title']


class PerewalAddSerializer(serializers.ModelSerializer):
	coords = CoordsSerializer(required=False)
	user = UsersSerializer(write_only=True)
	images = ImageSerializer(many=True, write_only=True)
	level = LevelSerializer(required=False, read_only=True)
	connect = serializers.CharField(allow_blank=True, allow_null=True)

	class Meta:
		model = PerewalAdd
		fields = '__all__'

	def validate(self, attrs):
		result = super().validate(attrs)
		return result

	def create(self, validated_data):

		coords_data = validated_data.pop('coords', {})
		user_data = validated_data.pop('user', {})
		images_data = validated_data.pop('images', [])
		level_data = validated_data.pop('level', {})

		# Получаем email пользователя
		email = user_data.get('email')

		# Проверяем, существует ли пользователь с таким email
		existing_user = Users.objects.filter(email=email).first()

		if existing_user:
			# Пользователь уже существует, используем его
			user_obj = existing_user
		else:
			# Пользователя нет, создаём нового
			user_obj = Users.objects.create(**user_data)

		coords_obj = Coords.objects.create(**coords_data)
		level_obj = Level.objects.create(**level_data)

		perewal_add = PerewalAdd.objects.create(
			coords=coords_obj,
			user=user_obj,
			level=level_obj,
			status="new",
			**validated_data
		)

		for image_data in images_data:
			Image.objects.create(perewal_added=perewal_add, **image_data)

		return perewal_add
