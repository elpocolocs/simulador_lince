# Generated by Django 5.1.4 on 2024-12-14 21:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0014_alter_curso_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 14, 21, 58, 42, 608393, tzinfo=datetime.timezone.utc)),
        ),
    ]