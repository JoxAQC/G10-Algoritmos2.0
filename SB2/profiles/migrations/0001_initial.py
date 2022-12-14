# Generated by Django 4.1.4 on 2022-12-07 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosGenerales',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('dni', models.IntegerField()),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateField()),
                ('num_celular', models.IntegerField()),
                ('sexo', models.CharField(max_length=10)),
                ('edad', models.IntegerField()),
                ('domicilio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transferencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingresar_usuario', models.CharField(default=None, max_length=150)),
                ('ingresar_cuenta_destino', models.IntegerField()),
                ('ingresar_monto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_tarjeta', models.IntegerField()),
                ('fecha_vencimiento', models.DateField()),
                ('ccv', models.IntegerField()),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.datosgenerales')),
            ],
        ),
        migrations.CreateModel(
            name='SesionWeb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_password', models.CharField(max_length=6)),
                ('persona', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.datosgenerales')),
            ],
        ),
    ]
