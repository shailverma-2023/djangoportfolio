# Generated by Django 4.2.3 on 2023-08-10 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emails', models.CharField(max_length=40)),
                ('msg', models.CharField(max_length=255)),
            ],
        ),
    ]
