# Generated by Django 4.1.7 on 2023-02-25 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicPlayer',
            fields=[
                ('id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('id_active', models.BooleanField(default=True)),
            ],
        ),
    ]
