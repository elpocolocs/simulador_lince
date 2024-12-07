# Generated by Django 5.1.4 on 2024-12-07 00:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_curso_precio'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CursosComprados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_compra', models.CharField(max_length=20)),
                ('fecha_compra', models.DateTimeField(auto_now=True)),
                ('curso_comprado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios_inscritos', to='cursos.curso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos_comprados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]