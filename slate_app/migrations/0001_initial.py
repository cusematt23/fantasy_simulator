# Generated by Django 4.2.4 on 2023-09-01 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=20)),
                ('name_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('player_slate_id', models.CharField(max_length=20)),
                ('roster_position', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('game_info', models.CharField(max_length=200)),
                ('teamabbrev', models.CharField(max_length=20)),
                ('avgpointspergame', models.DecimalField(decimal_places=6, max_digits=10)),
            ],
        ),
    ]
