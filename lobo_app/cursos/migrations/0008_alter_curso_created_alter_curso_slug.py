# Generated by Django 5.1.4 on 2024-12-12 03:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cursos", "0007_alter_curso_created_alter_curso_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="curso",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 12, 12, 3, 13, 49, 175950, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="curso",
            name="slug",
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
