# Generated by Django 5.1.4 on 2024-12-13 21:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0011_alter_curso_category_alter_curso_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 13, 21, 2, 42, 588, tzinfo=datetime.timezone.utc)),
        ),
    ]
