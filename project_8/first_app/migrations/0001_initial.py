# Generated by Django 5.1.4 on 2024-12-27 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
            ],
        ),
    ]
