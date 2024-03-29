# Generated by Django 2.0 on 2018-09-12 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recharge', '0006_playerstatistic'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivePlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_num', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_num', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
