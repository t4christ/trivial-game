# Generated by Django 3.0 on 2020-09-16 13:54

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
            name='ActivePlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_num', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BonusPointAirtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(default='', max_length=100)),
                ('list_numbers', models.TextField(default='')),
                ('bonus_points', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HighestLevelScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=100)),
                ('difficulty', models.CharField(max_length=10)),
                ('score', models.IntegerField(default=0)),
                ('phone_number', models.CharField(max_length=13)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JAccountQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JBioQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JChemistryQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JCommerceQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JCrkQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JEconomicsQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JEngQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JGeoQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JGovQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JIctQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JLiteratureQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JMathQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JPhysicsQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(max_length=150)),
                ('question_name', models.CharField(max_length=100)),
                ('publish_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserCorrectAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(default='', max_length=13)),
                ('difficulty', models.CharField(max_length=10)),
                ('winner', models.BooleanField(default=False)),
                ('score', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(max_length=10)),
                ('phone_number', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('score', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_stats', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MediumQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('question_detail', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='medium_question_detail', to='recharge.QuestionDetail')),
            ],
        ),
        migrations.CreateModel(
            name='LevelTwoQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('question_detail', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='leveltwo_question_detail', to='recharge.QuestionDetail')),
            ],
        ),
        migrations.CreateModel(
            name='LevelThreeQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('question_detail', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='levelthree_question_detail', to='recharge.QuestionDetail')),
            ],
        ),
        migrations.CreateModel(
            name='LevelOneQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('question_detail', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='levelone_question_detail', to='recharge.QuestionDetail')),
            ],
        ),
        migrations.CreateModel(
            name='LevelFourQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('question_detail', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='levelfour_question_detail', to='recharge.QuestionDetail')),
            ],
        ),
        migrations.CreateModel(
            name='LevelFiveQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('question_detail', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='levelfive_question_detail', to='recharge.QuestionDetail')),
            ],
        ),
        migrations.CreateModel(
            name='HighestScoreStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(max_length=10)),
                ('score', models.IntegerField(default=0)),
                ('phone_number', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_stats', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HardQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('question_detail', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='hard_question_detail', to='recharge.QuestionDetail')),
            ],
        ),
        migrations.CreateModel(
            name='EasyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('question_detail', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='easy_question_detail', to='recharge.QuestionDetail')),
            ],
        ),
        migrations.CreateModel(
            name='EasyAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='easy_answer', to='recharge.EasyQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='AkwaIbomQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('question_detail', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='akwaibom_question_detail', to='recharge.QuestionDetail')),
            ],
        ),
        migrations.CreateModel(
            name='MediumAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medium_answer', to='recharge.MediumQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4')},
            },
        ),
        migrations.CreateModel(
            name='LevelTwoAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leveltwo_answer', to='recharge.LevelTwoQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4')},
            },
        ),
        migrations.CreateModel(
            name='LevelThreeAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levelthree_answer', to='recharge.LevelThreeQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4')},
            },
        ),
        migrations.CreateModel(
            name='LevelOneAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levelone_answer', to='recharge.LevelOneQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4')},
            },
        ),
        migrations.CreateModel(
            name='LevelFourAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levelfour_answer', to='recharge.LevelFourQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4')},
            },
        ),
        migrations.CreateModel(
            name='LevelFiveAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levelfive_answer', to='recharge.LevelFiveQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4')},
            },
        ),
        migrations.CreateModel(
            name='JPhysicsAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('choice5', models.CharField(default='', max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jphy_answer', to='recharge.JPhysicsQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4', 'choice5')},
            },
        ),
        migrations.CreateModel(
            name='JMathAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('choice5', models.CharField(default='', max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jmath_answer', to='recharge.JMathQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4', 'choice5')},
            },
        ),
        migrations.CreateModel(
            name='JLiteratureAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('choice5', models.CharField(default='', max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jlit_answer', to='recharge.JLiteratureQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4', 'choice5')},
            },
        ),
        migrations.CreateModel(
            name='JIctAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('choice5', models.CharField(default='', max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jict_answer', to='recharge.JIctQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4', 'choice5')},
            },
        ),
        migrations.CreateModel(
            name='JGovAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('choice5', models.CharField(default='', max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jgov_answer', to='recharge.JGovQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4', 'choice5')},
            },
        ),
        migrations.CreateModel(
            name='JGeoAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('choice5', models.CharField(default='', max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jgeo_answer', to='recharge.JGeoQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4', 'choice5')},
            },
        ),
        migrations.CreateModel(
            name='JEngAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('choice5', models.CharField(default='', max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jeng_answer', to='recharge.JEngQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4', 'choice5')},
            },
        ),
        migrations.CreateModel(
            name='JEconomicsAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('choice5', models.CharField(default='', max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jeco_answer', to='recharge.JEconomicsQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4', 'choice5')},
            },
        ),
        migrations.CreateModel(
            name='JCrkAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('choice5', models.CharField(default='', max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jcrk_answer', to='recharge.JCrkQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4', 'choice5')},
            },
        ),
        migrations.CreateModel(
            name='JCommerceAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('choice5', models.CharField(default='', max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jcmm_answer', to='recharge.JCommerceQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4', 'choice5')},
            },
        ),
        migrations.CreateModel(
            name='JChemistryAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('choice5', models.CharField(default='', max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jchem_answer', to='recharge.JChemistryQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4', 'choice5')},
            },
        ),
        migrations.CreateModel(
            name='JBioAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('choice5', models.CharField(default='', max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jbio_answer', to='recharge.JBioQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4', 'choice5')},
            },
        ),
        migrations.CreateModel(
            name='JAccountAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('choice5', models.CharField(default='', max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jacct_answer', to='recharge.JAccountQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4', 'choice5')},
            },
        ),
        migrations.CreateModel(
            name='HardAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hard_answer', to='recharge.HardQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4')},
            },
        ),
        migrations.CreateModel(
            name='AkwaIbomAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=500)),
                ('choice2', models.CharField(max_length=500)),
                ('choice3', models.CharField(max_length=500)),
                ('choice4', models.CharField(max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='akwaibom_answer', to='recharge.AkwaIbomQuestion')),
            ],
            options={
                'unique_together': {('questions', 'choice1', 'choice2', 'choice3', 'choice4')},
            },
        ),
    ]
