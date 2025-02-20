# Generated by Django 5.1.5 on 2025-01-31 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('address_line1', models.CharField(blank=True, default='', max_length=255)),
                ('address_line2', models.CharField(blank=True, default='', max_length=255)),
                ('gender', models.CharField(default='Not Selected', max_length=50)),
                ('dob', models.DateField()),
                ('phone', models.CharField(default='0000000000', max_length=10)),
            ],
        ),
    ]
