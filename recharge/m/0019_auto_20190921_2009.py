# Generated by Django 2.0 on 2019-09-21 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recharge', '0018_auto_20190302_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='AkwaIbomAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='AkwaIbomQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='aksg_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='akwaibomanswer',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='akwaibom_answer', to='recharge.AkwaIbomQuestion'),
        ),
        migrations.AlterUniqueTogether(
            name='akwaibomanswer',
            unique_together={('questions', 'choice1', 'choice2', 'choice3', 'choice4')},
        ),
    ]
