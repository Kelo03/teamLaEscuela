# Generated by Django 4.1.2 on 2022-11-21 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_juegos_imagen2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='juegos',
            old_name='imagen2',
            new_name='imagenBig',
        ),
        migrations.RenameField(
            model_name='juegos',
            old_name='imagen',
            new_name='imagenSmall',
        ),
    ]
