from rest_framework import serializers
from .models import Users, Coords, PerewalAdd, Image, Level


class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = ['email', 'family', 'name', 'otc', 'phone']


class CoordsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Coords
		fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Level
		fields = ['summer', 'winter', 'autumn', 'spring']


class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = ['data', 'title']


class PerewalAddSerializer(serializers.ModelSerializer):
	coords = CoordsSerializer()
	user = UsersSerializer()
	images = ImageSerializer(many=True)
	level = LevelSerializer(required=False)
	connect = serializers.CharField(allow_blank=True, allow_null=True)
	status = serializers.CharField(read_only=True)

	class Meta:
		model = PerewalAdd
		fields = [
			'beauty_title', 'title', 'other_title', 'connect',
			'add_time', 'status', 'coords', 'level', 'user', 'images'
		]

	def create(self, validated_data):
		coords_data = validated_data.pop('coords', {})
		user_data = validated_data.pop('user', {})
		images_data = validated_data.pop('images', [])
		level_data = validated_data.pop('level', {})

		user_obj, _ = Users.objects.get_or_create(**user_data)
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
