from django.db import models
from uuid import uuid4
from operator import itemgetter


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


class SignupTime(models.Model):
    TIMES = {
        (1, '10:00'),
        (2, '10:30'),
        (3, '11:00'),
        (4, '11:30'),
        (5, '12:00'),
        (6, '12:30'),
        (7, '13:00'),
        (8, '13:30'),
        (9, '14:00'),
        (10, '14:30'),
        (11, '15:00'),
        (12, '15:30'),
        (13, '16:00'),
        (14, '16:30'),
        (15, '17:00'),
        (16, '17:30'),
        (17, '18:00'),
        (18, '18:30'),
        (19, '19:00'),
        (20, '19:30'),
        (21, '20:00'),
        (22, '20:30'),
    }

    master = models.ForeignKey(
        to=Personal,
        on_delete=models.CASCADE,
        verbose_name='Мастер'
    )
    a_time = models.IntegerField(
        choices=sorted(TIMES, key=itemgetter(0)),
        verbose_name='Доступное время'
    )
    a_date = models.DateField(
        null=True,
        verbose_name='Дата'
    )

    class Meta:
        verbose_name = 'Доступные интервалы'
        verbose_name_plural = 'Доступные интервалы'

    def __str__(self):
        return str(str(self.a_date) + str(f' {self.get_a_time_display()}'))


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
    master = models.ForeignKey(
        to=Personal,
        on_delete=models.CASCADE,
        verbose_name='Мастер'
    )
    time = models.ForeignKey(
        to=SignupTime,
        on_delete=models.CASCADE,
        verbose_name='Время записи',
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
