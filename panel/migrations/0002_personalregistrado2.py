# Generated by Django 4.2.4 on 2023-09-11 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalRegistrado2',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('n_persona', models.CharField(max_length=8)),
            ],
        ),
    ]
