# Generated by Django 3.0 on 2019-12-11 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20191210_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chirp',
            name='text',
            field=models.CharField(max_length=320),
        ),
    ]
