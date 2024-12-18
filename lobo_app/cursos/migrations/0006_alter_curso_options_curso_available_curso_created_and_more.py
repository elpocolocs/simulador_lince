# Generated by Django 5.1.4 on 2024-12-12 02:15

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cursos", "0005_cursoscomprados_cursos_curs_curso_c_2a8caa_idx"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="curso",
            options={"ordering": ["nombre"]},
        ),
        migrations.AddField(
            model_name="curso",
            name="available",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="curso",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 12, 12, 2, 15, 43, 984167, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AddField(
            model_name="curso",
            name="slug",
            field=models.SlugField(default="abc", max_length=200),
        ),
        migrations.AddField(
            model_name="curso",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="curso",
            name="precio",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
                "ordering": ["name"],
                "indexes": [
                    models.Index(fields=["name"], name="cursos_cate_name_7df174_idx")
                ],
            },
        ),
        migrations.AddField(
            model_name="curso",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cursos",
                to="cursos.category",
            ),
        ),
        migrations.AddIndex(
            model_name="curso",
            index=models.Index(fields=["id", "slug"], name="cursos_curs_id_b548aa_idx"),
        ),
        migrations.AddIndex(
            model_name="curso",
            index=models.Index(fields=["nombre"], name="cursos_curs_nombre_d1c82d_idx"),
        ),
        migrations.AddIndex(
            model_name="curso",
            index=models.Index(
                fields=["-created"], name="cursos_curs_created_2d4c10_idx"
            ),
        ),
    ]
