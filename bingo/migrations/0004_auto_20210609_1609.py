# Generated by Django 3.0.6 on 2021-06-09 10:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bingo', '0003_auto_20200606_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='ticket',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.int_list_validator]),
        ),
        migrations.AlterField(
            model_name='player',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
