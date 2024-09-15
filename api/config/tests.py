from config.models import Config
from config.models import Rate
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class ConfigViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")
        self.config = Config.objects.create(params="param1", step_number=1)
        self.url = reverse("config-list")
        self.token = self.get_token()

    def get_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)

    def test_get_configs(self):
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_config(self):
        data = {"params": "param2", "step_number": 2}
        response = self.client.post(
            self.url, data, format="json", HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Config.objects.count(), 2)
        config = Config.objects.get(params="param2")
        self.assertEqual(config.step_number, 2)


class RateViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")
        self.rate = Rate.objects.create(
            currency_code="USD",
            date="2023-01-01",
            currency_abbreviation="USD",
            currency_unit=1,
            currency_name="US Dollar",
            currency_exchange_rate=1.0,
        )
        self.url = reverse("rate-list")
        self.token = self.get_token()

    def get_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)

    def test_get_rates(self):
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_rate(self):
        data = {
            "currency_code": "EUR",
            "date": "2023-01-02",
            "currency_abbreviation": "EUR",
            "currency_unit": 1,
            "currency_name": "Euro",
            "currency_exchange_rate": 0.85,
        }
        response = self.client.post(
            self.url, data, format="json", HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rate.objects.count(), 2)
        rate = Rate.objects.get(currency_code="EUR")
        self.assertEqual(rate.currency_abbreviation, "EUR")
        self.assertEqual(rate.currency_unit, 1)
        self.assertEqual(rate.currency_name, "Euro")
        self.assertEqual(rate.currency_exchange_rate, 0.85)
