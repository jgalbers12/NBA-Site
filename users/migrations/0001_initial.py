# Generated by Django 4.1.7 on 2023-02-25 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('teams', '0004_basicteam_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('favorite_team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.basicteam')),
            ],
        ),
    ]
