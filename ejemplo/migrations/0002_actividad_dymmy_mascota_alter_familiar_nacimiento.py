# Generated by Django 4.1.4 on 2022-12-14 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('dia', models.CharField(max_length=200)),
                ('horario', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dymmy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('raza', models.CharField(max_length=200)),
                ('edad', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='familiar',
            name='nacimiento',
            field=models.CharField(max_length=100),
        ),
    ]
