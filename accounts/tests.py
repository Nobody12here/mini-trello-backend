from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class AccountAPITest(APITestCase):

    def setUp(self):
        self.register_url = reverse("register-user")

    def test_register_user(self):
        data = {"email": "testuser27@test.com", "password": "test123"}
        response = self.client.post(self.register_url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED, msg="User unable to register"
        )

    def test_register_with_missing_data(self):
        data = {"email": "testuser28@test.com", "password": "test123"}
        data.pop("email", None)
        response_without_email = self.client.post(self.register_url, data)
        resposne_without_any_fields = self.client.post(self.register_url, None)
        self.assertEqual(
            response_without_email.status_code, status.HTTP_400_BAD_REQUEST
        )
        self.assertEqual(
            resposne_without_any_fields.status_code, status.HTTP_400_BAD_REQUEST
        )
