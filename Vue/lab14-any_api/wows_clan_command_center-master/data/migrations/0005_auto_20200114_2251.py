# Generated by Django 3.0.2 on 2020-01-15 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20200114_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipinstance',
            name='shipinstance_ship',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_fleet', to='data.Ship'),
        ),
    ]
