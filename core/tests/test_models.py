import pytest
from django.core.exceptions import ValidationError
from perewal_api.core.models import Users, Coords, Level, PerewalAdd


@pytest.mark.django_db
def test_user_model():
	user = Users.objects.create(
		email="test0@example.com",
		family="Test0",
		name="Test1",
		otc="Test2",
		phone="+71234567890"
	)
	assert str(user.email) == "test0@example.com"


@pytest.mark.django_db
def test_invaid_email():
	with pytest.raises(ValidationError):
		Users.objects.create(email='')


@pytest.mark.django_db
def test_coords_model():
	coord = Coords.objects.create(latitude=12.0, longitude=20.0, height=10)
	assert float(coord.latitude) == 12.0


@pytest.mark.django_db
def test_level_model():
	level = Level.objects.create(summer="A", winter="B",autumn="C",spring="D")
	assert level.summer == "A"


@pytest.mark.django_db
def test_perewal_model():
	user = Users.objects.create(
		email="test0@example.com",
		family="Test0",
		name="Test1",
		otc="Test2",
		phone="+71234567890"
	)
	coords = Coords.objects.create(latitude=12.0, longitude=20.0, height=10)
	level = Level.objects.create(summer="A", winter="B",autumn="C",spring="D")
	perewal = PerewalAdd.objects.create(
		beauty_title='Горный перевал',
		title='Перевал Дятлова',
		other_title='',
		connect='',
		add_time='2023-01-01T12:00:00Z',
		status='new',
		coords=coords,
		user=user,
		level=level
	)
	assert perewal.beauty_title == 'Горный перевал'
