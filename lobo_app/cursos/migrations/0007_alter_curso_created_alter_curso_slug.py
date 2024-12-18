# Generated by Django 5.1.4 on 2024-12-12 03:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cursos", "0006_alter_curso_options_curso_available_curso_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="curso",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 12, 12, 3, 12, 38, 773312, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="curso",
            name="slug",
            field=models.SlugField(max_length=200),
        ),
    ]
