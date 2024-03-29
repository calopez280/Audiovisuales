# Generated by Django 2.2.6 on 2019-11-18 07:16

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
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id_equipo', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre_equipo', models.CharField(max_length=50)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Espacio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_espacio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_facultad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='facultad_equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingresado', models.DateField(auto_now=True, verbose_name='Fecha De Creacion')),
                ('id_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.Equipo')),
                ('id_facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.Facultad')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle_reserva', models.TextField()),
                ('fecha_solicitud', models.DateTimeField(verbose_name='Fecha De Solicitud')),
                ('id_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.facultad_equipo')),
                ('id_espacio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.Espacio')),
            ],
        ),
        migrations.AddField(
            model_name='espacio',
            name='id_facultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.Facultad'),
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle_reserva', models.TextField()),
                ('id_estado', models.CharField(choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', max_length=1)),
                ('id_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.Reserva')),
            ],
        ),
    ]
