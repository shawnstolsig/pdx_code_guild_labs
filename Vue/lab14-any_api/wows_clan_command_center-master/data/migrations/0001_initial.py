# Generated by Django 3.0 on 2020-01-14 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clan_wgid', models.IntegerField()),
                ('clan_tag', models.CharField(max_length=10, null=True)),
                ('clan_name', models.CharField(max_length=50, null=True)),
                ('clan_members_count', models.IntegerField(null=True)),
                ('clan_realm', models.CharField(max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_wgid', models.IntegerField()),
                ('player_nickname', models.CharField(max_length=50, null=True)),
                ('player_clan_role', models.CharField(max_length=20, null=True)),
                ('player_joined_at', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('player_clan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.Clan')),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_id', models.IntegerField()),
                ('ship_name', models.CharField(max_length=50)),
                ('ship_class', models.CharField(max_length=2)),
                ('ship_tier', models.IntegerField()),
                ('ship_nation', models.CharField(max_length=50)),
                ('ship_upgrade_slots', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_id', models.IntegerField()),
                ('skill_name', models.CharField(max_length=100)),
                ('skill_tier', models.IntegerField()),
                ('skill_picture_url', models.URLField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upgrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upgrade_id', models.IntegerField()),
                ('upgrade_name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShipInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipinstance_main_battery_hits', models.IntegerField(null=True)),
                ('shipinstance_main_battery_shots', models.IntegerField(null=True)),
                ('shipinstance_xp', models.IntegerField(null=True)),
                ('shipinstance_battles', models.IntegerField(null=True)),
                ('shipinstance_torpedoes_hits', models.IntegerField(null=True)),
                ('shipinstance_torpedoes_shots', models.IntegerField(null=True)),
                ('shipinstance_wins', models.IntegerField(null=True)),
                ('shipinstance_losses', models.IntegerField(null=True)),
                ('shipinstance_damage_dealt', models.IntegerField(null=True)),
                ('shipinstance_potential_damage', models.IntegerField(null=True)),
                ('shipinstance_spotting_damage', models.IntegerField(null=True)),
                ('shipinstance_cb_battles', models.IntegerField(default=0)),
                ('shipinstance_cb_wins', models.IntegerField(default=0)),
                ('shipinstance_cb_battles_survived', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('shipinstance_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Player')),
                ('shipinstance_ship', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.Ship')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='player_ships',
            field=models.ManyToManyField(to='data.Ship'),
        ),
        migrations.AddField(
            model_name='player',
            name='player_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]