# Generated by Django 4.1.5 on 2023-01-25 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_basicteam_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicteam',
            name='logo',
            field=models.ImageField(default='images/logos/_NBA_logo.png', upload_to='images/logos'),
        ),
    ]
