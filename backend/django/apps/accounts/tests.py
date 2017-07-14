from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
import factory
import json
from .models import BaseAccount
from .serializers import WholeAccountSerializer


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = BaseAccount

    first_name = 'John'
    last_name = 'Doe'
    email = '{}.{}@email.com'.format(first_name, last_name)
    password = 'passjohn1'


class FactoryBoyCreateUserTest(APITestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_can_create_user(self):
        response = self.client.get(
            reverse('_accounts:account-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            raw=json.dumps(response.data),
            expected_data=WholeAccountSerializer(self.user).data)
