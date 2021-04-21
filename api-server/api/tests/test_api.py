from django.test import TestCase
from rest_framework.test import APIClient
from ..models import *


# Создается класс для юнит-тестов
class ApiTests(TestCase):
    # Создается виртуальный клиент
    client = APIClient()

    # Cоздается виртуальная база данных с тестовыми объектами
    def setUp(self) -> None:
        # Тестовый объект филиала
        BranchOffice.objects.create(
            id=1,
            office_name='test',
            address='test',
            telephone='89456774372',
        )
        # Тестовый объект сотрудника
        Personal.objects.create(
            id=1,
            FIO='test',
            telephone='89164567345',
            address='test',
            employment_date='2021-02-01',
            branch_office_id=1,
        )
        # Тестовый объект услуги
        Services.objects.create(
            id=1,
            name='test',
            duration=1,
            price=1000,
            master_id=1,
        )
        # Тестовый объект интервала для записи
        SignupTime.objects.create(
            id=1,
            a_time=1,
            a_date='2021-02-01',
            master_id=1,
        )

    # Тестирование функции получения списка филиалов
    def test_api_services_list(self):
        # Производится запрос к API
        response = self.client.get('/api/services-list/')
        # Полученный результат сравнивается с ожидаемым
        print(f'test_api_services_list \n response data: {response.data}')
        assert response.status_code == 200

    # Тестирование функции получения списка филиалов
    def test_api_offices_list(self):
        # Производится запрос к API
        response = self.client.get('/api/offices-list/')
        # Полученный результат сравнивается с ожидаемым
        print(f'test_api_offices_list \n response data: {response.data}')
        assert response.status_code == 200

    # Тестирование функции создания записи с корректными входными данными
    def test_api_create_signup_valid(self):
        # Производится запрос к API с корректными данными
        response = self.client.post(
            path='/api/create-signup/',
            data={
                'FIO': 'Александр',
                'service': 1,
                'email': 'test@test.com',
                'time': 1,
                'master': 1,
                'branch_office': 1
            },
            format='json'
        )
        # Результат сравинвается с ожидаемым
        print(f'test_api_create_signup_valid \n response data: {response.data}')
        assert response.status_code == 200

    # Тестирование функции создания записи с некорректными входными данными
    def test_api_create_signup_invalid(self):
        # Производится запрос к API с некорректными данными
        response = self.client.post(
            path='/api/create-signup/',
            data={
                'FIO': 'Александр',
                'service': 1,
                'email': 'test.com',
                'time': 1,
                'master': 1,
                'branch_office': 1
            },
            format='json'
        )
        # Результат сравинвается с ожидаемым
        print(f'test_api_create_signup_invalid: \n response data: {response.data}')
        assert response.status_code == 400
