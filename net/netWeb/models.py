from django.db import models
from uuid import uuid4


class BranchOffice(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        verbose_name='',
    )
    office_name = models.CharField(
        max_length=200,
        verbose_name='',
    )
    address = models.CharField(
        max_length=200,
        verbose_name='',
    )
    telephone = models.CharField(
        max_length=12,
        verbose_name='',
    )

    class Meta:
        verbose_name = '',
        verbose_name_plural = '',

    def __str__(self):
        return self.address


class Inventory(models.Model):
    id = models.UUIDField(
        primary_key='True',
        default=uuid4,
        verbose_name='',
    )
    name = models.CharField(
        max_length=200,
        verbose_name='',
    )
    serial_number = models.CharField(
        max_length=100,
        verbose_name='',
        unique=True,
    )
    price = models.IntegerField(
        verbose_name='',
    )
    quantity = models.IntegerField(
        verbose_name='',
    )
    branch_office = models.ForeignKey(
        to=BranchOffice,
        on_delete=models.CASCADE,
        verbose_name='',
    )

    class Meta:
        verbose_name = '',
        verbose_name_plural = '',

    def __str__(self):
        return self.serial_number


class Personal(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        verbose_name='',
    )
    FIO = models.CharField(
        max_length=200,
        verbose_name='',
    )
    telephone = models.CharField(
        max_length=12,
        verbose_name='',
    )
    address = models.CharField(
        max_length=300,
        verbose_name='',
    )
    branch_office = models.ForeignKey(
        to=BranchOffice,
        on_delete=models.CASCADE,
        verbose_name='',
    )

    class Meta:
        verbose_name = '',
        verbose_name_plural = '',

    def __str__(self):
        return self.FIO


class Services(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        verbose_name='',
    )
    name = models.CharField(
        max_length=200,
        verbose_name='',
    )
    duration = models.IntegerField(
        verbose_name='',
    )
    price = models.IntegerField(
        verbose_name='',
    )
    master = models.ForeignKey(
        to=Personal,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = '',
        verbose_name_plural = '',

    def __str__(self):
        return self.name


class ServiceSignup(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        verbose_name='',
    )
    service = models.ForeignKey(
        to=Services,
        on_delete=models.CASCADE
    )
    time = models.DateTimeField(
        null=True,
        verbose_name='',
    )
    master = models.ForeignKey(
        to=Personal,
        on_delete=models.CASCADE
    )
    branch_office = models.ForeignKey(
        to=BranchOffice,
        on_delete=models.CASCADE
    )
    signup_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='',
    )

    class Meta:
        verbose_name = '',
        verbose_name_plural = '',

    def __str__(self):
        return self.time
