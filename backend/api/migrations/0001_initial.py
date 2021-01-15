# Generated by Django 3.1.1 on 2021-01-15 22:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_name', models.CharField(max_length=200, verbose_name='Наименование филиала')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес филиала')),
                ('telephone', models.CharField(max_length=12, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Филиалы',
                'verbose_name_plural': 'Филиалы',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=200, verbose_name='ФИО')),
                ('telephone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('address', models.CharField(max_length=300, verbose_name='Адрес')),
                ('employment_date', models.DateField(null=True, verbose_name='Дата найма')),
                ('branch_office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.branchoffice', verbose_name='Филиал')),
            ],
            options={
                'verbose_name': 'Персонал',
                'verbose_name_plural': 'Персонал',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('duration', models.IntegerField(verbose_name='Примерная длительность')),
                ('price', models.IntegerField(verbose_name='Цена (руб.)')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.personal', verbose_name='Мастер')),
            ],
            options={
                'verbose_name': 'Услуги',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='SignupTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_time', models.IntegerField(choices=[(1, '10:00'), (2, '10:30'), (3, '11:00'), (4, '11:30'), (5, '12:00'), (6, '12:30'), (7, '13:00'), (8, '13:30'), (9, '14:00'), (10, '14:30'), (11, '15:00'), (12, '15:30'), (13, '16:00'), (14, '16:30'), (15, '17:00'), (16, '17:30'), (17, '18:00'), (18, '18:30'), (19, '19:00'), (20, '19:30'), (21, '20:00'), (22, '20:30')], verbose_name='Доступное время')),
                ('a_date', models.DateField(null=True, verbose_name='Дата')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.personal', verbose_name='Мастер')),
            ],
            options={
                'verbose_name': 'Доступные интервалы',
                'verbose_name_plural': 'Доступные интервалы',
            },
        ),
        migrations.CreateModel(
            name='ServiceSignup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('FIO', models.CharField(max_length=255, verbose_name='ФИО клиента')),
                ('signup_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания записи')),
                ('branch_office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.branchoffice', verbose_name='Филиал')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.personal', verbose_name='Мастер')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.services', verbose_name='Услуга')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.signuptime', verbose_name='Время записи')),
            ],
            options={
                'verbose_name': 'Записи',
                'verbose_name_plural': 'Записи',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование инвентаря')),
                ('serial_number', models.CharField(max_length=100, unique=True, verbose_name='Серийный номер')),
                ('price', models.IntegerField(verbose_name='Стоимость (руб.)')),
                ('quantity', models.IntegerField(verbose_name='Количество (шт.)')),
                ('delivery_date', models.DateField(null=True, verbose_name='Дата появления')),
                ('branch_office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.branchoffice', verbose_name='Филиал')),
            ],
            options={
                'verbose_name': 'Инвентарь',
                'verbose_name_plural': 'Инвентарь',
            },
        ),
    ]
