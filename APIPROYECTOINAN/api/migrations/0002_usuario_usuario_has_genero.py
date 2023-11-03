# Generated by Django 4.2.5 on 2023-09-21 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.IntegerField(db_column='idUsuario', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='nombre', max_length=100)),
                ('paterno', models.CharField(db_column='paterno', max_length=100)),
                ('materno', models.CharField(db_column='materno', max_length=100)),
                ('correo', models.CharField(db_column='correo', max_length=100)),
                ('alias', models.CharField(db_column='alias', max_length=100)),
                ('password', models.CharField(db_column='password', max_length=100)),
            ],
            options={
                'db_table': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='usuario_has_genero',
            fields=[
                ('idusuario_has_genero', models.AutoField(db_column='idalumno_has_genero', default=1, primary_key=True, serialize=False)),
                ('fk_alumno', models.ForeignKey(db_column='fk_alumno', on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
                ('fk_genero', models.ForeignKey(db_column='fk_genero', on_delete=django.db.models.deletion.CASCADE, to='api.genero')),
            ],
            options={
                'db_table': 'usuario_has_genero',
            },
        ),
    ]