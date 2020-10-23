from django.db import models
from uuid import uuid4


class BranchOffice(models.Model):
    office_name = models.CharField(
        max_length=200,
        verbose_name='Наименование филиала',
    )
    address = models.CharField(
        max_length=200,
        verbose_name='Адрес филиала',
    )
    telephone = models.CharField(
        max_length=12,
        verbose_name='Номер телефона',
    )

    class Meta:
        verbose_name = 'Филиалы'
        verbose_name_plural = 'Филиалы'

    def __str__(self):
        return self.address


class Inventory(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Наименование инвентаря',
    )
    serial_number = models.CharField(
        max_length=100,
        verbose_name='Серийный номер',
        unique=True,
    )
    price = models.IntegerField(
        verbose_name='Стоимость (руб.)',
    )
    quantity = models.IntegerField(
        verbose_name='Количество (шт.)',
    )
    delivery_date = models.DateField(
        null=True,
        verbose_name='Дата появления',
    )
    branch_office = models.ForeignKey(
        to=BranchOffice,
        on_delete=models.CASCADE,
        verbose_name='Филиал',
    )

    class Meta:
        verbose_name = 'Инвентарь'
        verbose_name_plural = 'Инвентарь'

    def __str__(self):
        return self.serial_number


class Personal(models.Model):
    FIO = models.CharField(
        max_length=200,
        verbose_name='ФИО',
    )
    telephone = models.CharField(
        max_length=12,
        verbose_name='Телефон',
    )
    address = models.CharField(
        max_length=300,
        verbose_name='Адрес',
    )
    employment_date = models.DateField(
        null=True,
        verbose_name='Дата найма',
    )
    branch_office = models.ForeignKey(
        to=BranchOffice,
        on_delete=models.CASCADE,
        verbose_name='Филиал',
    )

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'

    def __str__(self):
        return self.FIO


class Services(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Наименование',
    )
    duration = models.IntegerField(
        verbose_name='Примерная длительность',
    )
    price = models.IntegerField(
        verbose_name='Цена (руб.)',
    )
    master = models.ForeignKey(
        to=Personal,
        on_delete=models.CASCADE,
        verbose_name='Мастер'
    )

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class ServiceSignup(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    FIO = models.CharField(
        max_length=255,
        verbose_name='ФИО клиента'
    )
    service = models.ForeignKey(
        to=Services,
        on_delete=models.CASCADE,
        verbose_name='Услуга'
    )
    time = models.DateTimeField(
        null=True,
        verbose_name='Время',
    )
    master = models.ForeignKey(
        to=Personal,
        on_delete=models.CASCADE,
        verbose_name='Мастер'
    )
    branch_office = models.ForeignKey(
        to=BranchOffice,
        on_delete=models.CASCADE,
        verbose_name='Филиал'
    )
    signup_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания записи',
    )

    class Meta:
        verbose_name = 'Записи'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return str(self.time)
