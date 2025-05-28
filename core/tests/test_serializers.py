import pytest
from perewal_api.core.serializers import *
from perewal_api.core.models import *


@pytest.fixture
def setup_objects():
	user = Users.objects.create(email='test1@test.com', family='Test1', name='Test2', otc='Test3', phone='+79876543210')
	coords = Coords.objects.create(latitude=10.0, longitude=20.0, height=100)
	level = Level.objects.create(summer="A", winter="B", autumn="C", spring="D")
	return user, coords, level


@pytest.mark.django_db
def test_users_serializer(setup_objects):
	user, _ = setup_objects
	serializer = UsersSerializer(user)
	expected_data = {
		'email': 'test1@test.com',
		'family': 'Test1',
		'name': 'Test2',
		'otc': 'Test3',
		'phone': '+79876543210'
	}
	assert serializer.data['email'] == expected_data['email']


@pytest.mark.django_db
def test_perewal_serializer(setup_objects):
	user, coords, level = setup_objects
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
	serializer = PerewalAddSerializer(perewal)
	assert 'beauty_title' in serializer.data
