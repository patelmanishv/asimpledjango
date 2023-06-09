# Generated by Django 4.2 on 2023-04-13 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=300)),
                ('year', models.IntegerField(max_length=4)),
                ('director', models.CharField(max_length=50)),
            ],
        ),
    ]
