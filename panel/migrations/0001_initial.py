# Generated by Django 4.2.4 on 2023-09-11 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='deviceID',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('deviceID', models.CharField(max_length=8, null=True)),
                ('ubicacion', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'deviceID',
            },
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ubicacion', models.CharField(max_length=50, null=True)),
                ('cardidHex', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('apellido', models.CharField(max_length=50, null=True)),
                ('empresa', models.CharField(max_length=50, null=True)),
                ('cargo', models.CharField(max_length=50, null=True)),
                ('f_evento', models.DateField(null=True)),
                ('h_evento', models.TimeField(null=True)),
                ('evento', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(default='0', max_length=2)),
            ],
            options={
                'db_table': 'Historial',
            },
        ),
        migrations.CreateModel(
            name='LiveData',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ubicacion', models.CharField(max_length=50, null=True)),
                ('cardidHex', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('apellido', models.CharField(max_length=50, null=True)),
                ('empresa', models.CharField(max_length=50, null=True)),
                ('cargo', models.CharField(max_length=50, null=True)),
                ('f_ingreso', models.DateField(null=True)),
                ('h_ingreso', models.TimeField(null=True)),
            ],
            options={
                'db_table': 'LiveData',
            },
        ),
        migrations.CreateModel(
            name='NoRegistrados',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ubicacion', models.CharField(max_length=50, null=True)),
                ('cardidHex', models.CharField(max_length=8, null=True)),
                ('f_evento', models.DateField(null=True)),
                ('h_evento', models.TimeField(null=True)),
                ('evento', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'NoRegistrados',
            },
        ),
        migrations.CreateModel(
            name='PersonalRegistrado',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('n_persona', models.CharField(max_length=8)),
                ('ap_paterno', models.CharField(max_length=50)),
                ('ap_materno', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=8)),
                ('f_nac', models.DateField(null=True)),
                ('proyecto', models.CharField(max_length=50)),
                ('centro_coste', models.CharField(max_length=50)),
                ('tipo_trabajador', models.CharField(max_length=50)),
                ('clave_sexo', models.CharField(max_length=1)),
                ('f_alta', models.DateField()),
                ('f_baja', models.DateField(null=True)),
                ('motivo_cese', models.CharField(max_length=50, null=True)),
                ('cargo', models.CharField(max_length=50)),
                ('card_id', models.CharField(max_length=8)),
                ('area', models.CharField(max_length=50)),
                ('servicio', models.CharField(max_length=50)),
                ('supervicion', models.CharField(max_length=50)),
                ('guardia', models.CharField(max_length=1)),
                ('correo', models.CharField(max_length=50, null=True)),
                ('n_celular', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'PersonalRegistrado',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=8)),
                ('Telefono', models.CharField(max_length=9)),
                ('SegundoApellido', models.CharField(max_length=50)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]