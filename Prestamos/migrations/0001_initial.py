# Generated by Django 2.2.2 on 2019-10-09 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_equipo', models.CharField(max_length=12)),
                ('nombre_equipo', models.CharField(max_length=50)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_facultad', models.CharField(max_length=12)),
                ('nombre_facultad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.Rol')),
            ],
        ),
        migrations.CreateModel(
            name='facultad_equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.Equipo')),
                ('id_facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.Facultad')),
            ],
        ),
        migrations.CreateModel(
            name='Espacio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_espacio', models.CharField(max_length=12)),
                ('nombre_espacio', models.CharField(max_length=50)),
                ('id_facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.Categoria')),
            ],
        ),
    ]