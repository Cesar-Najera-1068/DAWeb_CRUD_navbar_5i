# Generated by Django 5.1.3 on 2024-11-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conductores',
            fields=[
                ('id_conductor', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=50)),
                ('Apellidos', models.CharField(max_length=50)),
                ('Numerolicencia', models.CharField(max_length=50)),
                ('Horario', models.CharField(max_length=50)),
                ('Numerotelefono', models.CharField(max_length=10)),
                ('Correoelectronico', models.CharField(max_length=10)),
            ],
        ),
    ]