# Generated by Django 3.0 on 2019-12-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191212_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='users_followed',
            field=models.ManyToManyField(to='users.Profile'),
        ),
    ]
