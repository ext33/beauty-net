from django.test import TestCase
from rest_framework.test import APIClient


# Создается класс для юнит-тестов
class ApiTests(TestCase):
    # Создается виртуальный клиент
    client = APIClient()

    def setUp(self) -> None:
        pass

    # Функция тестирования API получения списка услуг
    def test_api_services_list(self):
        # Производится запрос к API
        response = self.client.get('/api/services-list/')
        # Полученный результат сравнивается с ожидаемым
        assert response.status_code == 200

    def test_api_offices_list(self):
        # Производится запрос к API
        response = self.client.get('/api/offices-list/')
        # Полученный результат сравнивается с ожидаемым
        assert response.status_code == 200
