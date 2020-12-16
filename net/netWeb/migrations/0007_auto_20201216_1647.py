# Generated by Django 3.1.1 on 2020-12-16 13:47

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('netWeb', '0006_auto_20201215_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesignup',
            name='time',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='master', chained_model_field='master', on_delete=django.db.models.deletion.CASCADE, to='netWeb.signuptime', verbose_name='Время записи'),
        ),
    ]
