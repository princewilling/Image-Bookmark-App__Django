# Generated by Django 4.1.2 on 2022-11-27 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
