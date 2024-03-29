# Generated by Django 2.0 on 2018-09-06 15:02

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
            name='EasyAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=150)),
                ('choice2', models.CharField(max_length=150)),
                ('choice3', models.CharField(max_length=150)),
                ('choice4', models.CharField(max_length=150)),
                ('correct_answer', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='EasyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_easy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HardAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=50)),
                ('choice2', models.CharField(max_length=50)),
                ('choice3', models.CharField(max_length=50)),
                ('choice4', models.CharField(max_length=50)),
                ('correct_answer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HardQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_hard', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LevelFiveAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=50)),
                ('choice2', models.CharField(max_length=50)),
                ('choice3', models.CharField(max_length=50)),
                ('choice4', models.CharField(max_length=50)),
                ('correct_answer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LevelFiveQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_five', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LevelFourAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=50)),
                ('choice2', models.CharField(max_length=50)),
                ('choice3', models.CharField(max_length=50)),
                ('choice4', models.CharField(max_length=50)),
                ('correct_answer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LevelFourQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_levelfour', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LevelOneAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=50)),
                ('choice2', models.CharField(max_length=50)),
                ('choice3', models.CharField(max_length=50)),
                ('choice4', models.CharField(max_length=50)),
                ('correct_answer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LevelOneQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_levelone', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LevelThreeAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=50)),
                ('choice2', models.CharField(max_length=50)),
                ('choice3', models.CharField(max_length=50)),
                ('choice4', models.CharField(max_length=50)),
                ('correct_answer', models.CharField(max_length=50)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levelthree_answer', to='recharge.LevelOneQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='LevelThreeQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_levelthree', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LevelTwoAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=50)),
                ('choice2', models.CharField(max_length=50)),
                ('choice3', models.CharField(max_length=50)),
                ('choice4', models.CharField(max_length=50)),
                ('correct_answer', models.CharField(max_length=50)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leveltwo_answer', to='recharge.LevelOneQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='LevelTwoQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_leveltwo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MediumAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=50)),
                ('choice2', models.CharField(max_length=50)),
                ('choice3', models.CharField(max_length=50)),
                ('choice4', models.CharField(max_length=50)),
                ('correct_answer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MediumQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_medium', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCorrectAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(max_length=10)),
                ('score', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='mediumanswer',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medium_answer', to='recharge.MediumQuestion'),
        ),
        migrations.AddField(
            model_name='leveloneanswer',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levelone_answer', to='recharge.LevelOneQuestion'),
        ),
        migrations.AddField(
            model_name='levelfouranswer',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levelfour_answer', to='recharge.LevelOneQuestion'),
        ),
        migrations.AddField(
            model_name='levelfiveanswer',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levelfive_answer', to='recharge.LevelOneQuestion'),
        ),
        migrations.AddField(
            model_name='hardanswer',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hard_answer', to='recharge.HardQuestion'),
        ),
        migrations.AddField(
            model_name='easyanswer',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='easy_answer', to='recharge.EasyQuestion'),
        ),
        migrations.AlterUniqueTogether(
            name='mediumanswer',
            unique_together={('questions', 'choice1', 'choice2', 'choice3', 'choice4')},
        ),
        migrations.AlterUniqueTogether(
            name='leveltwoanswer',
            unique_together={('questions', 'choice1', 'choice2', 'choice3', 'choice4')},
        ),
        migrations.AlterUniqueTogether(
            name='levelthreeanswer',
            unique_together={('questions', 'choice1', 'choice2', 'choice3', 'choice4')},
        ),
        migrations.AlterUniqueTogether(
            name='leveloneanswer',
            unique_together={('questions', 'choice1', 'choice2', 'choice3', 'choice4')},
        ),
        migrations.AlterUniqueTogether(
            name='levelfouranswer',
            unique_together={('questions', 'choice1', 'choice2', 'choice3', 'choice4')},
        ),
        migrations.AlterUniqueTogether(
            name='levelfiveanswer',
            unique_together={('questions', 'choice1', 'choice2', 'choice3', 'choice4')},
        ),
        migrations.AlterUniqueTogether(
            name='hardanswer',
            unique_together={('questions', 'choice1', 'choice2', 'choice3', 'choice4')},
        ),
    ]
