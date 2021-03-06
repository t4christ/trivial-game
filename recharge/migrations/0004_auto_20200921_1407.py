# Generated by Django 3.0 on 2020-09-21 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recharge', '0003_tempanswer_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='jaccountquestion',
            name='question_detail',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='jaccount', to='recharge.QuestionDetail'),
        ),
        migrations.AddField(
            model_name='jbioquestion',
            name='question_detail',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='jbio', to='recharge.QuestionDetail'),
        ),
        migrations.AddField(
            model_name='jchemistryquestion',
            name='question_detail',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='jchemistry', to='recharge.QuestionDetail'),
        ),
        migrations.AddField(
            model_name='jcommercequestion',
            name='question_detail',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='jcommerce', to='recharge.QuestionDetail'),
        ),
        migrations.AddField(
            model_name='jcrkquestion',
            name='question_detail',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='jcrk', to='recharge.QuestionDetail'),
        ),
        migrations.AddField(
            model_name='jeconomicsquestion',
            name='question_detail',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='jeconomics', to='recharge.QuestionDetail'),
        ),
        migrations.AddField(
            model_name='jengquestion',
            name='question_detail',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='jeng', to='recharge.QuestionDetail'),
        ),
        migrations.AddField(
            model_name='jgeoquestion',
            name='question_detail',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='jgeo', to='recharge.QuestionDetail'),
        ),
        migrations.AddField(
            model_name='jgovquestion',
            name='question_detail',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='jgov', to='recharge.QuestionDetail'),
        ),
        migrations.AddField(
            model_name='jictquestion',
            name='question_detail',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='jict', to='recharge.QuestionDetail'),
        ),
        migrations.AddField(
            model_name='jliteraturequestion',
            name='question_detail',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='jliterature', to='recharge.QuestionDetail'),
        ),
        migrations.AddField(
            model_name='jmathquestion',
            name='question_detail',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='jmath', to='recharge.QuestionDetail'),
        ),
        migrations.AddField(
            model_name='jphysicsquestion',
            name='question_detail',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='jphysics', to='recharge.QuestionDetail'),
        ),
    ]
