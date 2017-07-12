from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
import factory
from .models import BaseAccount


class UserFactory(factory.Factory):

    class Meta:
        model = BaseAccount

    first_name = 'John'
    last_name = 'Doe'
    email = '{}.{}@email.com'.format(first_name, last_name)
    password = 'passjohn1'


class CreateUserTest(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client.login(email=self.user.email, password=self.user.password)

    def test_can_create_user(self):
        response = self.client.get(
                reverse('_accounts:account-list'),)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
