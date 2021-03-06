# Generated by Django 3.0 on 2020-10-02 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recharge', '0006_highestscorestatistic_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highestlevelscore',
            name='player',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='highestscorestatistic',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='highest_score', to=settings.AUTH_USER_MODEL),
        ),
    ]
