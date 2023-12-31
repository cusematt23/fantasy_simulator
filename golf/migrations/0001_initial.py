# Generated by Django 4.2.4 on 2023-09-01 23:14

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
            name='Golfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('name_id', models.CharField(max_length=100, null=True)),
                ('salary', models.IntegerField(null=True)),
                ('proj', models.DecimalField(decimal_places=3, max_digits=7, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lineup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('salary', models.IntegerField(null=True)),
                ('players', models.CharField(max_length=1000, null=True)),
                ('creator', models.ForeignKey(default=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='optimized_lineups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
