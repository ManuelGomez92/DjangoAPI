# Generated by Django 4.2.5 on 2023-10-19 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_usuario_idusuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='usuario_has_genero',
        ),
    ]
