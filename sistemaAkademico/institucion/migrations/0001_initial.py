# Generated by Django 5.1.4 on 2025-01-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PeriodoEscolar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.PositiveIntegerField()),
                ('division', models.CharField(choices=[('Bimestral', 'Bimestral'), ('Semestral', 'Semestral'), ('Trimestral', 'Trimestral')], max_length=50)),
            ],
        ),
    ]
