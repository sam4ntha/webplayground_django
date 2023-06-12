from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    #En setUp se debe de preparar la prueba
    def setUp(self):
        User.objects.create_user('test', 'test@gmail.com', 'hola1test')

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)