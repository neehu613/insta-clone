# Generated by Django 2.0.6 on 2018-11-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20181114_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
