# from django.db.models import Count
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import datetime
from datetime import time
from datetime import datetime as xmas_time
import random
from django.template.loader import get_template,render_to_string
from random import randint
from django.conf import settings
from accounts.models import MyUser
from django.http import JsonResponse
from django.contrib import messages
from django.db.models.aggregates import Max
from django.core import serializers
from django.utils import timezone
from .models import *
from erc.models import ERCTransaction
from itertools import chain
# from django.views.decorators.csrf import csrf_exempt
import datetime
import json
# import pandas as pd
import csv
from utils.smsclient import SmsClient

sms_client = SmsClient()


def answer():
    question=LevelFourQuestion.objects.all()
    with open('answer.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row, quest in zip(reader,question):
            # if len(row) > 5:
                choice1 = row['choice1']
                choice2 = row['choice2']
                choice3 = row['choice3']
                choice4 = row['choice4']
                correct_answer = row['correct_answer']
                get_answer=LevelFourAnswer(choice1=choice1,choice2=choice2,choice3=choice3,choice4=choice4,correct_answer=correct_answer,questions=quest)
                get_answer.save()
            # else:
            #     choice1 = row['choice1']
            #     choice2 = row['choice2']
            #     choice3 = row['choice3']
            #     choice4 = row['choice4']
            #     correct_answer = row['correct_answer']
            #     get_answer=JMathAnswer(choice1=choice1,choice2=choice2,choice3=choice3,choice4=choice4,correct_answer=correct_answer,questions=quest)
            #     get_answer.save()


def question(request):
    question=LevelFourQuestion.objects.all()
    with open('question.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            content = row['content']
            poster = request.user
            get_question = LevelFourQuestion(content=content,poster=poster)
            get_question.save()

def del_answer():
    # account = JAccountAnswer.objects.all()
    # bio = JBioAnswer.objects.all()
    # eng = JEngAnswer.objects.all()
    # chem = JChemistryAnswer.objects.all()
    math = JMathAnswer.objects.all()
    # question=chain(account,eng,bio,chem,math)
    for ans in math:
        ans.delete()
    return math
    

from itertools import chain
def del_question():
    level_one=LevelOneQuestion.objects.all()
    level_two=LevelTwoQuestion.objects.all()
    level_three=LevelThreeQuestion.objects.all()
    level_four=LevelFourQuestion.objects.all()
    level_five=LevelFiveQuestion.objects.all()
    easy=EasyQuestion.objects.all()
    medium=MediumQuestion.objects.all()
    hard=HardQuestion.objects.all()
    JAccount_Question = JAccountQuestion.objects.all()
    JBio_Question = JBioQuestion.objects.all()
    JGeo_Question = JGeoQuestion.objects.all()
    JPhysics_Question = JPhysicsQuestion.objects.all()
    JChemistry_Question = JChemistryQuestion.objects.all()
    JCommerce_Question = JCommerceQuestion.objects.all()
    JIct_Question = JIctQuestion.objects.all()
    JCrk_Question = JCrkQuestion.objects.all()
    JLiterature_Question = JLiteratureQuestion.objects.all()
    JEconomics_Question= JEconomicsQuestion.objects.all()
    JGov_Question= JGovQuestion.objects.all()
    correct_ans=UserCorrectAnswer.objects.all()
    question=chain(level_one,level_two,level_three,level_four,level_five,easy,medium,hard,correct_ans,
    JAccount_Question,JBio_Question,JGeo_Question,JPhysics_Question,JChemistry_Question,JCommerce_Question,JIct_Question,
    JCrk_Question,JLiterature_Question,JEconomics_Question,JGov_Question)
    for ans in question:
        ans.delete()
    return question


def load_question(request):
    del_question()

    return HttpResponse("Questions Loading Activity Successful")




def statistics(request):
        time_day = datetime.date.today() #timezone.now() - timezone.timedelta(days=1)
        time_hour = timezone.now() - timezone.timedelta(hours=1)
        time_mon = datetime.datetime.now().month #timezone.now() - timezone.timedelta(days=30)
        now=datetime.datetime.now()
        time_year=now.year
        count_play = PlayerStatistic.objects.all().count()
        addedDate = datetime.datetime.now().replace(microsecond=0)
        high_easy_hr = HighestScoreStatistic.objects.filter(difficulty="easy",timestamp__gte=time_hour).count()
        high_easy_dy = HighestScoreStatistic.objects.filter(difficulty="easy",timestamp__startswith=time_day).count()
        high_easy_mn = HighestScoreStatistic.objects.filter(difficulty="easy",timestamp__month=time_mon).count()
        high_easy_yr = HighestScoreStatistic.objects.filter(difficulty="easy",timestamp__year=time_year).count()

        high_med_hr = HighestScoreStatistic.objects.filter(difficulty="medium",timestamp__gte=time_hour).count()
        high_med_dy = HighestScoreStatistic.objects.filter(difficulty="medium",timestamp__startswith=time_day).count()
        high_med_mn = HighestScoreStatistic.objects.filter(difficulty="medium",timestamp__month=time_mon).count()
        high_med_yr = HighestScoreStatistic.objects.filter(difficulty="medium",timestamp__year=time_year).count()

        high_hard_hr = HighestScoreStatistic.objects.filter(difficulty="hard",timestamp__gte=time_hour).count()
        high_hard_dy = HighestScoreStatistic.objects.filter(difficulty="hard",timestamp__startswith=time_day).count()
        high_hard_mn = HighestScoreStatistic.objects.filter(difficulty="hard",timestamp__month=time_mon).count()
        high_hard_yr = HighestScoreStatistic.objects.filter(difficulty="hard",timestamp__year=time_year).count()


        high_levone_hr = HighestScoreStatistic.objects.filter(difficulty="levelone",timestamp__gte=time_hour).count()
        high_levone_dy = HighestScoreStatistic.objects.filter(difficulty="levelone",timestamp__startswith=time_day).count()
        high_levone_mn = HighestScoreStatistic.objects.filter(difficulty="levelone",timestamp__month=time_mon).count()
        high_levone_yr = HighestScoreStatistic.objects.filter(difficulty="levelone",timestamp__year=time_year).count()


        high_levtwo_hr = HighestScoreStatistic.objects.filter(difficulty="leveltwo",timestamp__gte=time_hour).count()
        high_levtwo_dy = HighestScoreStatistic.objects.filter(difficulty="leveltwo",timestamp__startswith=time_day).count()
        high_levtwo_mn = HighestScoreStatistic.objects.filter(difficulty="leveltwo",timestamp__month=time_mon).count()
        high_levtwo_yr = HighestScoreStatistic.objects.filter(difficulty="leveltwo",timestamp__year=time_year).count()


        high_levthree_hr = HighestScoreStatistic.objects.filter(difficulty="levelthree",timestamp__gte=time_hour).count()
        high_levthree_dy = HighestScoreStatistic.objects.filter(difficulty="levelthree",timestamp__startswith=time_day).count()
        high_levthree_mn = HighestScoreStatistic.objects.filter(difficulty="levelthree",timestamp__month=time_mon).count()
        high_levthree_yr = HighestScoreStatistic.objects.filter(difficulty="levelthree",timestamp__year=time_year).count()



        high_levfour_hr = HighestScoreStatistic.objects.filter(difficulty="levelfour",timestamp__gte=time_hour).count()
        high_levfour_dy = HighestScoreStatistic.objects.filter(difficulty="levelfour",timestamp__startswith=time_day).count()
        high_levfour_mn = HighestScoreStatistic.objects.filter(difficulty="levelfour",timestamp__month=time_mon).count()
        high_levfour_yr = HighestScoreStatistic.objects.filter(difficulty="levelfour",timestamp__year=time_year).count()


        # Level Five
        high_levfive_hr = HighestScoreStatistic.objects.filter(difficulty="levelfive",timestamp__gte=time_hour).count()
        high_levfive_dy = HighestScoreStatistic.objects.filter(difficulty="levelfive",timestamp__startswith=time_day).count()
        high_levfive_mn = HighestScoreStatistic.objects.filter(difficulty="levelfive",timestamp__month=time_mon).count()
        high_levfive_yr = HighestScoreStatistic.objects.filter(difficulty="levelfive",timestamp__year=time_year).count()

        # Hourly Statistics
        easy_players_hr=PlayerStatistic.objects.filter(difficulty="easy",timestamp__gte=time_hour).count()
        med_players_hr = PlayerStatistic.objects.filter(difficulty="medium",timestamp__gte=time_hour).count()
        hard_players_hr = PlayerStatistic.objects.filter(difficulty="hard",timestamp__gte=time_hour).count()
        levone_players_hr = PlayerStatistic.objects.filter(difficulty="levelone",timestamp__gte=time_hour).count()
        levtwo_players_hr = PlayerStatistic.objects.filter(difficulty="leveltwo",timestamp__gte=time_hour).count()
        levthree_players_hr = PlayerStatistic.objects.filter(difficulty="levelthree",timestamp__gte=time_hour).count()
        levfour_players_hr = PlayerStatistic.objects.filter(difficulty="levelfour",timestamp__gte=time_hour).count()
        levfive_players_hr = PlayerStatistic.objects.filter(difficulty="levelfive",timestamp__gte=time_hour).count()
        

        # Daily Statistics
        easy_players_dy=PlayerStatistic.objects.filter(difficulty="easy",timestamp__startswith=time_day).count()
        med_players_dy = PlayerStatistic.objects.filter(difficulty="medium",timestamp__startswith=time_day).count()
        hard_players_dy = PlayerStatistic.objects.filter(difficulty="hard",timestamp__startswith=time_day).count()
        levone_players_dy = PlayerStatistic.objects.filter(difficulty="levelone",timestamp__startswith=time_day).count()
        levtwo_players_dy = PlayerStatistic.objects.filter(difficulty="leveltwo",timestamp__startswith=time_day).count()
        levthree_players_dy = PlayerStatistic.objects.filter(difficulty="levelthree",timestamp__startswith=time_day).count()
        levfour_players_dy = PlayerStatistic.objects.filter(difficulty="levelfour",timestamp__startswith=time_day).count()
        levfive_players_dy = PlayerStatistic.objects.filter(difficulty="levelfive",timestamp__startswith=time_day).count()
        


        # Monthly Statistics
        easy_players_mn=PlayerStatistic.objects.filter(difficulty="easy",timestamp__month=time_mon).count()
        med_players_mn = PlayerStatistic.objects.filter(difficulty="medium",timestamp__month=time_mon).count()
        hard_players_mn = PlayerStatistic.objects.filter(difficulty="hard",timestamp__month=time_mon).count()
        levone_players_mn = PlayerStatistic.objects.filter(difficulty="levelone",timestamp__month=time_mon).count()
        levtwo_players_mn = PlayerStatistic.objects.filter(difficulty="leveltwo",timestamp__month=time_mon).count()
        levthree_players_mn = PlayerStatistic.objects.filter(difficulty="levelthree",timestamp__month=time_mon).count()
        levfour_players_mn = PlayerStatistic.objects.filter(difficulty="levelfour",timestamp__month=time_mon).count()
        levfive_players_mn = PlayerStatistic.objects.filter(difficulty="levelfive",timestamp__month=time_mon).count()
        



        # Yearly Statistics
        easy_players_yr=PlayerStatistic.objects.filter(difficulty="easy",timestamp__year=time_year).count()
        med_players_yr = PlayerStatistic.objects.filter(difficulty="medium",timestamp__year=time_year).count()
        hard_players_yr = PlayerStatistic.objects.filter(difficulty="hard",timestamp__year=time_year).count()
        levone_players_yr = PlayerStatistic.objects.filter(difficulty="levelone",timestamp__year=time_year).count()
        levtwo_players_yr = PlayerStatistic.objects.filter(difficulty="leveltwo",timestamp__year=time_year).count()
        levthree_players_yr = PlayerStatistic.objects.filter(difficulty="levelthree",timestamp__year=time_year).count()
        levfour_players_yr = PlayerStatistic.objects.filter(difficulty="levelfour",timestamp__year=time_year).count()
        levfive_players_yr = PlayerStatistic.objects.filter(difficulty="levelfive",timestamp__year=time_year).count()
        



        context={'count_play':count_play,'heyr':high_easy_yr,'hedy':high_easy_dy,'hemn':high_easy_mn,'hehr':high_easy_hr,
        'hmyr':high_med_yr,'hmdy':high_med_dy,'hmmn':high_med_mn,'hmhr':high_med_hr,
        'hhyr':high_hard_yr,'hhdy':high_hard_dy,'hhmn':high_hard_mn,'hhhr':high_hard_hr,
        'hl1yr':high_levone_yr,'hl1dy':high_levone_dy,'hl1mn':high_levone_mn,'hl1hr':high_levone_hr,
        'hl2yr':high_levtwo_yr,'hl2dy':high_levtwo_dy,'hl2mn':high_levtwo_mn,'hl2hr':high_levtwo_hr,
        'hl3yr':high_levthree_yr,'hl3dy':high_levthree_dy,'hl3mn':high_levthree_mn,'hl3hr':high_levthree_hr,
        'hl4yr':high_levfour_yr,'hl4dy':high_levfour_dy,'hl4mn':high_levfour_mn,'hl4hr':high_levfour_hr,
        'hl5yr':high_levfive_yr,'hl5dy':high_levfive_dy,'hl5mn':high_levfive_mn,'hl5hr':high_levfive_hr,
        'dat':addedDate,'easy_yr':easy_players_yr,
        'med_yr':med_players_yr,'hard_yr':hard_players_yr,'levelone_yr':levone_players_yr,'leveltwo_yr':levtwo_players_yr,
        'levelthree_yr':levthree_players_yr,'levelfour_yr':levfour_players_yr,'levelfive_yr':levfive_players_yr,'easy_mn':easy_players_mn,
        'med_mn':med_players_mn,'hard_mn':hard_players_mn,'levelone_mn':levone_players_mn,'leveltwo_mn':levtwo_players_mn,
        'levelthree_mn':levthree_players_mn,'levelfour_mn':levfour_players_mn,'levelfive_mn':levfive_players_mn,'easy_dy':easy_players_dy,
        'med_dy':med_players_dy,'hard_dy':hard_players_dy,'levelone_dy':levone_players_dy,'leveltwo_dy':levtwo_players_dy,
        'levelthree_dy':levthree_players_dy,'levelfour_dy':levfour_players_dy,'levelfive_dy':levfive_players_dy,'easy_hr':easy_players_hr,
        'med_hr':med_players_hr,'hard_hr':hard_players_hr,'levelone_hr':levone_players_hr,'leveltwo_hr':levtwo_players_hr,
        'levelthree_hr':levthree_players_hr,'levelfour_hr':levfour_players_hr,'levelfive_hr':levfive_players_hr
        }
        if request.user.is_authenticated:
            return render(request,"statistics.html",context)
        else:
            return redirect("/")



def statistics_excel(request):
        time_day = timezone.now() - timezone.timedelta(days=1)
        time_hour = timezone.now() - timezone.timedelta(hours=1)
        time_mon = timezone.now() - timezone.timedelta(6*30)
        now=datetime.datetime.now()
        time_year=now.year
        # content-type of response
        response = HttpResponse(content_type='application/ms-excel')
        #decide file name
        
        response['Content-Disposition'] = 'attachment; filename="wstreams_excel_data_%s.xls"'%datetime.datetime.now()

        #creating workbook
        wb = xlwt.Workbook(encoding='utf-8')

        #adding sheet
        ws = wb.add_sheet("sheet1")

        # Sheet header, first row
        row_num = 0
        row_num1 = 0

        font_style = xlwt.XFStyle()
        # headers are bold
        font_style.font.bold = True

        #column header names, you can use your own headers here
        columns = ['Players for  The Year(Easy)', 'Players  for The Year(Medium)', 'Players for The Year(Hard)', 'Players for  The Year (LevelOne)','Players for The Year (LevelTwo)','Players for The Year (LevelThree)',
        'Players for  The Year (LevelFour)','Players for  The Year (LevelFive)'
        'Players for  The Month(Easy)', 'Players  for The Month(Medium)', 'Players for The Month(Hard)', 'Players for  The Month (LevelOne)','Players for The Month (LevelTwo)',
        'Players for The Month (LevelThree)','Players for  The Month (LevelFour)','Players for The Month(LevelFive)',
        'Players for  The Day(Easy)', 'Players  for The Day(Medium)', 'Players for The Day(Hard)', 'Players for  The Day (LevelOne)','Players for The Day (LevelTwo)',
        'Players for The Day (LevelThree)','Players for  The Day (LevelFour)','Players for the Day(LevelFive)'
        ]

        column = ['Highest Score for  The Year(Easy)', 'Highest Score  for The Year(Medium)', 'Highest Score for The Year(Hard)', 'Highest Score for  The Year (LevelOne)','Highest Score for The Year (LevelTwo)','Highest Score for The Year (LevelThree)',
        'Highest Score for  The Year (LevelFour)','Highest Score for  The Year (LevelFive)'
        'Highest Score for  The Month(Easy)', 'Highest Score  for The Month(Medium)', 'Highest Score for The Month(Hard)', 'Highest Score for  The Month (LevelOne)','Highest Score for The Month (LevelTwo)',
        'Highest Score for The Month (LevelThree)','Highest Score for  The Month (LevelFour)','Highest Score for The Month(LevelFive)',
        'Highest Score for  The Day(Easy)', 'Highest Score  for The Day(Medium)', 'Highest Score for The Day(Hard)', 'Highest Score for  The Day (LevelOne)','Highest Score for The Day (LevelTwo)',
        'Highest Score for The Day (LevelThree)','Highest Score for  The Day (LevelFour)','Highest Score for the Day(LevelFive)'
        ]

        #write column headers in sheet
        for col_num in range(len(column)):
            ws.write(row_num, col_num, column[col_num], font_style)
        # for col_num1 in range(len(column)):
        #     ws.write(row_num1,col_num1,columns[col_num1], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        addedDate = datetime.datetime.now().replace(microsecond=0)
        high_easy_hr = HighestScoreStatistic.objects.filter(difficulty="easy",timestamp__gte=time_hour).count()
        high_easy_dy = HighestScoreStatistic.objects.filter(difficulty="easy",timestamp__gte=time_day).count()
        high_easy_mn = HighestScoreStatistic.objects.filter(difficulty="easy",timestamp__gte=time_mon).count()
        high_easy_yr = HighestScoreStatistic.objects.filter(difficulty="easy",timestamp__year=time_year).count()

        high_med_hr = HighestScoreStatistic.objects.filter(difficulty="medium",timestamp__gte=time_hour).count()
        high_med_dy = HighestScoreStatistic.objects.filter(difficulty="medium",timestamp__gte=time_day).count()
        high_med_mn = HighestScoreStatistic.objects.filter(difficulty="medium",timestamp__gte=time_mon).count()
        high_med_yr = HighestScoreStatistic.objects.filter(difficulty="medium",timestamp__year=time_year).count()

        high_hard_hr = HighestScoreStatistic.objects.filter(difficulty="hard",timestamp__gte=time_hour).count()
        high_hard_dy = HighestScoreStatistic.objects.filter(difficulty="hard",timestamp__gte=time_day).count()
        high_hard_mn = HighestScoreStatistic.objects.filter(difficulty="hard",timestamp__gte=time_mon).count()
        high_hard_yr = HighestScoreStatistic.objects.filter(difficulty="hard",timestamp__year=time_year).count()


        high_levone_hr = HighestScoreStatistic.objects.filter(difficulty="levelone",timestamp__gte=time_hour).count()
        high_levone_dy = HighestScoreStatistic.objects.filter(difficulty="levelone",timestamp__gte=time_day).count()
        high_levone_mn = HighestScoreStatistic.objects.filter(difficulty="levelone",timestamp__gte=time_mon).count()
        high_levone_yr = HighestScoreStatistic.objects.filter(difficulty="levelone",timestamp__year=time_year).count()


        high_levtwo_hr = HighestScoreStatistic.objects.filter(difficulty="leveltwo",timestamp__gte=time_hour).count()
        high_levtwo_dy = HighestScoreStatistic.objects.filter(difficulty="leveltwo",timestamp__gte=time_day).count()
        high_levtwo_mn = HighestScoreStatistic.objects.filter(difficulty="leveltwo",timestamp__gte=time_mon).count()
        high_levtwo_yr = HighestScoreStatistic.objects.filter(difficulty="leveltwo",timestamp__year=time_year).count()


        high_levthree_hr = HighestScoreStatistic.objects.filter(difficulty="levelthree",timestamp__gte=time_hour).count()
        high_levthree_dy = HighestScoreStatistic.objects.filter(difficulty="levelthree",timestamp__gte=time_day).count()
        high_levthree_mn = HighestScoreStatistic.objects.filter(difficulty="levelthree",timestamp__gte=time_mon).count()
        high_levthree_yr = HighestScoreStatistic.objects.filter(difficulty="levelthree",timestamp__year=time_year).count()



        high_levfour_hr = HighestScoreStatistic.objects.filter(difficulty="levelfour",timestamp__gte=time_hour).count()
        high_levfour_dy = HighestScoreStatistic.objects.filter(difficulty="levelfour",timestamp__gte=time_day).count()
        high_levfour_mn = HighestScoreStatistic.objects.filter(difficulty="levelfour",timestamp__gte=time_mon).count()
        high_levfour_yr = HighestScoreStatistic.objects.filter(difficulty="levelfour",timestamp__year=time_year).count()


        # Level Five
        high_levfive_hr = HighestScoreStatistic.objects.filter(difficulty="levelfive",timestamp__gte=time_hour).count()
        high_levfive_dy = HighestScoreStatistic.objects.filter(difficulty="levelfive",timestamp__gte=time_day).count()
        high_levfive_mn = HighestScoreStatistic.objects.filter(difficulty="levelfive",timestamp__gte=time_mon).count()
        high_levfive_yr = HighestScoreStatistic.objects.filter(difficulty="levelfive",timestamp__year=time_year).count()

        # Hourly Statistics
        easy_players_hr=PlayerStatistic.objects.filter(difficulty="easy",timestamp__gte=time_hour).count()
        med_players_hr = PlayerStatistic.objects.filter(difficulty="medium",timestamp__gte=time_hour).count()
        hard_players_hr = PlayerStatistic.objects.filter(difficulty="hard",timestamp__gte=time_hour).count()
        levone_players_hr = PlayerStatistic.objects.filter(difficulty="levelone",timestamp__gte=time_hour).count()
        levtwo_players_hr = PlayerStatistic.objects.filter(difficulty="leveltwo",timestamp__gte=time_hour).count()
        levthree_players_hr = PlayerStatistic.objects.filter(difficulty="levelthree",timestamp__gte=time_hour).count()
        levfour_players_hr = PlayerStatistic.objects.filter(difficulty="levelfour",timestamp__gte=time_hour).count()
        levfive_players_hr = PlayerStatistic.objects.filter(difficulty="levelfive",timestamp__gte=time_hour).count()
        

        # Daily Statistics
        easy_players_dy=PlayerStatistic.objects.filter(difficulty="easy",timestamp__gte=time_day).count()
        med_players_dy = PlayerStatistic.objects.filter(difficulty="medium",timestamp__gte=time_day).count()
        hard_players_dy = PlayerStatistic.objects.filter(difficulty="hard",timestamp__gte=time_day).count()
        levone_players_dy = PlayerStatistic.objects.filter(difficulty="levelone",timestamp__gte=time_day).count()
        levtwo_players_dy = PlayerStatistic.objects.filter(difficulty="leveltwo",timestamp__gte=time_day).count()
        levthree_players_dy = PlayerStatistic.objects.filter(difficulty="levelthree",timestamp__gte=time_day).count()
        levfour_players_dy = PlayerStatistic.objects.filter(difficulty="levelfour",timestamp__gte=time_day).count()
        levfive_players_dy = PlayerStatistic.objects.filter(difficulty="levelfive",timestamp__gte=time_day).count()
        


        # Monthly Statistics
        easy_players_mn=PlayerStatistic.objects.filter(difficulty="easy",timestamp__gte=time_mon).count()
        med_players_mn = PlayerStatistic.objects.filter(difficulty="medium",timestamp__gte=time_mon).count()
        hard_players_mn = PlayerStatistic.objects.filter(difficulty="hard",timestamp__gte=time_mon).count()
        levone_players_mn = PlayerStatistic.objects.filter(difficulty="levelone",timestamp__gte=time_mon).count()
        levtwo_players_mn = PlayerStatistic.objects.filter(difficulty="leveltwo",timestamp__gte=time_mon).count()
        levthree_players_mn = PlayerStatistic.objects.filter(difficulty="levelthree",timestamp__gte=time_mon).count()
        levfour_players_mn = PlayerStatistic.objects.filter(difficulty="levelfour",timestamp__gte=time_mon).count()
        levfive_players_mn = PlayerStatistic.objects.filter(difficulty="levelfive",timestamp__gte=time_mon).count()
        



        # Yearly Statistics
        easy_players_yr=PlayerStatistic.objects.filter(difficulty="easy",timestamp__year=time_year).count()
        med_players_yr = PlayerStatistic.objects.filter(difficulty="medium",timestamp__year=time_year).count()
        hard_players_yr = PlayerStatistic.objects.filter(difficulty="hard",timestamp__year=time_year).count()
        levone_players_yr = PlayerStatistic.objects.filter(difficulty="levelone",timestamp__year=time_year).count()
        levtwo_players_yr = PlayerStatistic.objects.filter(difficulty="leveltwo",timestamp__year=time_year).count()
        levthree_players_yr = PlayerStatistic.objects.filter(difficulty="levelthree",timestamp__year=time_year).count()
        levfour_players_yr = PlayerStatistic.objects.filter(difficulty="levelfour",timestamp__year=time_year).count()
        levfive_players_yr = PlayerStatistic.objects.filter(difficulty="levelfive",timestamp__year=time_year).count()
        
        # HighScore Based
        # for my_row in data:
        row_num = row_num + 1
        ws.write(row_num, 0, easy_players_yr, font_style)
        ws.write(row_num, 1, med_players_yr, font_style)
        ws.write(row_num, 2, hard_players_yr, font_style)

        ws.write(row_num, 3, easy_players_mn, font_style)
        ws.write(row_num, 4, med_players_mn, font_style)
        ws.write(row_num, 5, hard_players_mn, font_style)


        ws.write(row_num, 6, easy_players_dy, font_style)
        ws.write(row_num, 7, med_players_dy, font_style)
        ws.write(row_num, 8, hard_players_dy, font_style)

        # Level Based
        ws.write(row_num, 9, levone_players_yr, font_style)
        ws.write(row_num, 10, levtwo_players_yr, font_style)
        ws.write(row_num, 11, levthree_players_yr, font_style)
        ws.write(row_num, 12, levfour_players_yr, font_style)
        ws.write(row_num, 13, levfive_players_yr, font_style)


        ws.write(row_num, 14, levone_players_mn, font_style)
        ws.write(row_num, 15, levtwo_players_mn, font_style)
        ws.write(row_num, 16, levthree_players_mn, font_style)
        ws.write(row_num, 17, levfour_players_mn, font_style)
        ws.write(row_num, 18, levfive_players_mn, font_style)


        ws.write(row_num, 19, levone_players_dy, font_style)
        ws.write(row_num, 20, levtwo_players_dy, font_style)
        ws.write(row_num, 21, levthree_players_dy, font_style)
        ws.write(row_num, 22, levfour_players_dy, font_style)
        ws.write(row_num, 23, levfive_players_dy, font_style)
        

        # ws.write(row_num1, 0, easy_players_yr, font_style)
        # ws.write(row_num1, 1, med_players_yr, font_style)
        # ws.write(row_num1, 2, hard_players_yr, font_style)

        # ws.write(row_num1, 3, easy_players_mn, font_style)
        # ws.write(row_num1, 4, med_players_mn, font_style)
        # ws.write(row_num1, 5, hard_players_mn, font_style)


        # ws.write(row_num1, 6, easy_players_dy, font_style)
        # ws.write(row_num1, 7, med_players_dy, font_style)
        # ws.write(row_num1, 8, hard_players_dy, font_style)

        # # Level Based
        # ws.write(row_num1, 9, levone_players_yr, font_style)
        # ws.write(row_num1, 10, levtwo_players_yr, font_style)
        # ws.write(row_num1, 11, levthree_players_yr, font_style)
        # ws.write(row_num1, 12, levfour_players_yr, font_style)
        # ws.write(row_num1, 13, levfive_players_yr, font_style)


        # ws.write(row_num1, 14, levone_players_mn, font_style)
        # ws.write(row_num1, 15, levtwo_players_mn, font_style)
        # ws.write(row_num1, 16, levthree_players_mn, font_style)
        # ws.write(row_num1, 17, levfour_players_mn, font_style)
        # ws.write(row_num1, 18, levfive_players_mn, font_style)


        # ws.write(row_num1, 19, levone_players_dy, font_style)
        # ws.write(row_num1, 20, levtwo_players_dy, font_style)
        # ws.write(row_num1, 21, levthree_players_dy, font_style)
        # ws.write(row_num1, 22, levfour_players_dy, font_style)
        # ws.write(row_num1, 23, levfive_players_dy, font_style)
	   



        if request.user.is_authenticated and request.user.is_admin:
            wb.save(response)
            return response
        else:
            return redirect("/")


 # Hours must be 24 hour clock times 
def is_weekday_and_time_in_range(date):
    return date.weekday() < 4




import xlwt
from django.http import HttpResponse


def download_excel_data(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="wstreams_excel_data_%s.xls"'%datetime.datetime.now()
    wb= xlwt.Workbook(encoding='utf-8')
    ws= wb.add_sheet("sheet1")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold =True
    columns= ['Username','Full Name', 'Password','Phone Number', 'Email', 'Registration Date']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style =xlwt.XFStyle()
    data = MyUser.objects.all()
    for my_row in data:

        row_num = row_num + 1
        ws.write(row_num,0,my_row.username, font_style)
        ws.write(row_num,1,my_row.get_full_name, font_style)
        ws.write(row_num,2,my_row.password,font_style)
        ws.write(row_num,3,my_row.phone_number, font_style)
        ws.write(row_num,4,my_row.email, font_style)
        ws.write(row_num,5,my_row.created_at.strftime("%Y-%m-%d"), font_style)
    wb.save(response)
    return response

# def download_excel_data(request):
# 	# content-type of response
# 	response = HttpResponse(content_type='application/ms-excel')
# 	#decide file name
    
# 	response['Content-Disposition'] = 'attachment; filename="wstreams_excel_data_%s.xls"'%datetime.datetime.now()

# 	#creating workbook
# 	wb = xlwt.Workbook(encoding='utf-8')

# 	#adding sheet
# 	ws = wb.add_sheet("sheet1")

# 	# Sheet header, first row
# 	row_num = 0

# 	font_style = xlwt.XFStyle()
# 	# headers are bold
# 	font_style.font.bold = True

# 	#column header names, you can use your own headers here
# 	columns = ['Full Name', 'Phone Number', 'Email',  'Registration Date',]

# 	#write column headers in sheet
# 	for col_num in range(len(columns)):
# 		ws.write(row_num, col_num, columns[col_num], font_style)

# 	# Sheet body, remaining rows
# 	font_style = xlwt.XFStyle()

# 	#get your data, from database or from a text file...
# 	data = MyUser.objects.all() #dummy method to fetch data.
# 	for my_row in data:
# 		row_num = row_num + 1
# 		ws.write(row_num, 0, my_row.get_full_name, font_style)
# 		ws.write(row_num, 1, my_row.phone_number, font_style)
# 		ws.write(row_num, 2, my_row.email, font_style)
# 		ws.write(row_num, 3, my_row.created_at.strftime("%Y-%m-%d"), font_style)
    
        
        # ws.write(row_num, 4, my_row.username, font_style)
        # ws.write(row_num, 3, my_row.created_at,font_style)

        

	# wb.save(response)
	# return response




import uuid
def gen_ran():
	return str(uuid.uuid4())




@login_required
def recharge(request):
    context={}
    template="recharge/recharge.html"
    return render(request,template,context)



# @login_required
# def level_based(request):
#     user=get_object_or_404(MyUser,username=username)
#     data =dict()
    
#     weekday = datetime.datetime.now().strftime('%A') 
#     current_day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    
#     # easy_count=EasyAnswer.objects.all().count()
#     # easy_rand=randint(0,easy_count -1)
#     score=0
#     current_site = request.META['HTTP_HOST']
#     get_easy = "%s/recharge/easy/%s"%(current_site,request.user)
#     get_medium = "%s/recharge/medium%s/"%(current_site,request.user)
#     get_hard = "%s/recharge/hard/%s"%(current_site,request.user)

#     time_diff = timezone.now() - timezone.timedelta(hours=1)
   
#     easy=EasyAnswer.objects.all().order_by('?')[:20]
#     num_score=EasyAnswer.objects.all()[:20]
#     num_played = UserCorrectAnswer.objects.filter(user=request.user,timestamp__gte=time_diff).count()
#     if num_score and num_played < 25:
#         if weekday not in current_day:
#             messages.error(request,"Sorry this game is only opened from Mondays to Saturdays")
#             return redirect("/")
#         all_score=UserCorrectAnswer.objects.all().order_by('-score','-timestamp')[:1]
#         user_score=UserCorrectAnswer.objects.filter(user=request.user).order_by('-timestamp')

#         context={"easy":easy,"user_score":user_score,"all_score":all_score}
#         template="recharge/high-score-based/easy.html"
#         return render(request,template,context)
#     else:
#         # context={"easy":easy,"user_score":user_score,"all_score":all_score}
        
#         template="recharge/high-score-based/easy.html"
#         return render(request,template)

@login_required
def easy_submit(request,username):
        user=get_object_or_404(MyUser,username=username)
        level_progress=""
        data =dict()
        start_timer=0
        time_differ=0
        time_diff_arr= range(1,55)
        time_diff_arr2=range(117,129)
        #[58,50,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,43,44,45,46,47,48,49,9,10,11,12,13,14,15,16,17,18,19,20,118,119,120,121,122,123,124,125,126,127,128,129,130]
        time_diff = timezone.now() - timezone.timedelta(hours=3)

        weekday = datetime.datetime.now().strftime('%A') 
        current_day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        current_site = request.META['HTTP_HOST']
        where_from = request.META.get('HTTP_REFERER')

    
        get_easy = "%s/recharge/easy/%s/"%(current_site,request.user)
        get_medium = "%s/recharge/medium/%s/"%(current_site,request.user)
        get_hard = "%s/recharge/hard/%s/"%(current_site,request.user)
        get_akwa = "%s/recharge/akwa/%s/"%(current_site,request.user)
        get_xmas = "%s/recharge/xmas/%s/"%(current_site,request.user)
        get_level1 = "%s/recharge/level1/%s/"%(current_site,request.user)
        get_level2 = "%s/recharge/level2/%s/"%(current_site,request.user)
        get_level3 = "%s/recharge/level3/%s/"%(current_site,request.user)
        get_level4 = "%s/recharge/level4/%s/"%(current_site,request.user)
        get_level5 = "%s/recharge/level5/%s/"%(current_site,request.user)

        ############# JAMB View Url ####################
        get_jacct = "%s/jamb/account/%s/"%(current_site,request.user)
        get_jgeo = "%s/jamb/geography/%s/"%(current_site,request.user)
        get_jbio = "%s/jamb/biology/%s/"%(current_site,request.user)
        get_jphy = "%s/jamb/physics/%s/"%(current_site,request.user)
        get_jchem = "%s/jamb/chemistry/%s/"%(current_site,request.user)
        get_jcomm = "%s/jamb/commerce/%s/"%(current_site,request.user)
        get_jeng = "%s/jamb/english/%s/"%(current_site,request.user)
        get_jmath = "%s/jamb/mathematics/%s/"%(current_site,request.user)
        get_jict = "%s/jamb/ict/%s/"%(current_site,request.user)
        get_jcrk = "%s/jamb/crk/%s/"%(current_site,request.user)
        get_jlit = "%s/jamb/literature/%s/"%(current_site,request.user)
        get_jeco = "%s/jamb/economics/%s/"%(current_site,request.user)
        get_jgov = "%s/jamb/government/%s/"%(current_site,request.user)


        num_played = UserCorrectAnswer.objects.filter(user=request.user,timestamp__gte=time_diff).count()
        print("Print Played",num_played)
        # end_timer=0
        if num_played < 20:
            if weekday not in current_day:
                data['weekday']="This Game is only opened from Mondays to Saturdays"
                # return redirect("/")
            if get_level1 in where_from:
                easy=LevelOneAnswer.objects.all().order_by('?')[:10]
                num_score=LevelOneAnswer.objects.all()[:10]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)
            elif get_level2 in where_from:
                # if "onecompleted" in request.session:
                    # level_progress = "leveltwo"
                    easy=LevelTwoAnswer.objects.all().order_by('?')[:10]
                    num_score=LevelTwoAnswer.objects.all()[:10]
                    context={"easy":easy}
                    data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)
                    # del request.session['onecompleted']
                # else:
                    # data['previous']="You need to complete the previous level to move to this level"
                    # return redirect("/")
            
            elif get_level3 in where_from:
                # if "twocompleted" in request.session:
                    # level_progress = "levelthree"
                    easy=LevelThreeAnswer.objects.all().order_by('?')[:10]
                    num_score=LevelThreeAnswer.objects.all()[:10]
                    context={"easy":easy}
                    data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)
                    # del request.session['twocompleted']
                # else:
                    # messages.error(request,"You need to complete the previous level to move to this level")
                    # return redirect("/")
            
            elif get_level4 in where_from:
                # if "threecompleted" in request.session:
                    # level_progress = "levelfour"
                    easy=LevelFourAnswer.objects.all().order_by('?')[:10]
                    num_score=LevelFourAnswer.objects.all()[:10]
                    context={"easy":easy}
                    data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)
                    # del request.session['threecompleted']
                # else:
                    # messages.error(request,"You need to complete the previous level to move to this level")
                    # return redirect("/")
            
            elif get_level5 in where_from:
                # if  "fourcompleted" in request.session:
                    # level_progress = "levelfive"
                    easy=LevelFiveAnswer.objects.all().order_by('?')[:10]
                    num_score=LevelFiveAnswer.objects.all()[:10]
                    context={"easy":easy}
                    data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)
                    # del request.session['fourcompleted']
                # else:
                    # data['previous']="You need to complete the previous level to move to this level"
                    # return redirect("/")
            
            elif get_easy in where_from:
                easy=EasyAnswer.objects.all().order_by('?')[:50]
                num_score=EasyAnswer.objects.all()[:50]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)
            elif get_medium in where_from:
                easy=MediumAnswer.objects.all().order_by('?')[:50]
                num_score=MediumAnswer.objects.all()[:50]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)
            elif get_hard in where_from:
                easy=HardAnswer.objects.all().order_by('?')[:50]
                num_score=HardAnswer.objects.all()[:50]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)

            elif get_akwa in where_from:
                akwa=AkwaIbomAnswer.objects.all().order_by('?')[:10]
                num_score=AkwaIbomAnswer.objects.all()[:10]
                context={"easy":akwa}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)

            elif get_xmas in where_from:
                easy=HardAnswer.objects.all().order_by('?')[:10]
                num_score=HardAnswer.objects.all()[:10]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)

            ######################## JAMB View Question ###########################
            elif get_jacct in where_from:
                easy=JAccountAnswer.objects.all().order_by('?')[:20]
                num_score=JAccountAnswer.objects.all()[:20]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)

            elif get_jmath in where_from:
                easy=JMathAnswer.objects.all().order_by('?')[:20]
                num_score=JMathAnswer.objects.all()[:20]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)

            elif get_jeng in where_from:
                easy=JEngAnswer.objects.all().order_by('?')[:20]
                num_score=JEngAnswer.objects.all()[:20]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)

            elif get_jgeo in where_from:
                easy=JGeoAnswer.objects.all().order_by('?')[:20]
                num_score=JGeoAnswer.objects.all()[:20]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)

            elif get_jbio in where_from:
                easy=JBioAnswer.objects.all().order_by('?')[:20]
                num_score=JBioAnswer.objects.all()[:20]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)

            elif get_jphy in where_from:
                easy=JPhysicsAnswer.objects.all().order_by('?')[:20]
                num_score=JPhysicsAnswer.objects.all()[:20]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)

            elif get_jchem in where_from:
                easy=JChemistryAnswer.objects.all().order_by('?')[:20]
                num_score=JChemistryAnswer.objects.all()[:20]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)

            elif get_jcomm in where_from:
                easy=JCommerceAnswer.objects.all().order_by('?')[:20]
                num_score=JCommerceAnswer.objects.all()[:20]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)

            elif get_jict in where_from:
                easy=JIctAnswer.objects.all().order_by('?')[:20]
                num_score=JIctAnswer.objects.all()[:20]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)

            elif get_jcrk in where_from:
                easy=JCrkAnswer.objects.all().order_by('?')[:20]
                num_score=JCrkAnswer.objects.all()[:20]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)


            elif get_jlit in where_from:
                easy=JLiteratureAnswer.objects.all().order_by('?')[:20]
                num_score=JLiteratureAnswer.objects.all()[:20]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)

            elif get_jeco in where_from:
                easy=JEconomicsAnswer.objects.all().order_by('?')[:20]
                num_score=JEconomicsAnswer.objects.all()[:20]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)

            elif get_jgov in where_from:
                easy=JGovAnswer.objects.all().order_by('?')[:20]
                num_score=JGovAnswer.objects.all()[:20]
                context={"easy":easy}
                data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', context)
        else:
            data['limit'] = "You Have Played Your Limit For The Hour"
        time_start = request.POST.get('time_start',)
        if time_start:
            import time,math
            start_timer = time.time()
            request.session["get-timer"]=start_timer
            
            
            # def mycoverter(o):
            #     if isinstance(o,datetime.datetime):
            #         return o.__str__()
            # json.dumps(request.session,default=mycoverter)
            # b=start_timer
            print(start_timer)
         
        time_end = request.POST.get("end_time",)
        if time_end:
            import time,math
            end_timer=time.time()
            time_differ = math.floor(end_timer - request.session["get-timer"])
            if time_differ in time_diff_arr or time_differ in time_diff_arr2:
                    
            # get_time_diff = int(time_end - time_start)
                score=0
                if request.method == 'POST':
                    easy_ans=EasyAnswer.objects.all()
                    medium_ans=MediumAnswer.objects.all()
                    hard_ans=HardAnswer.objects.all()
                    akwa_ans=AkwaIbomAnswer.objects.all()
                    xmas_ans=HardAnswer.objects.all()
                    levone_ans=LevelOneAnswer.objects.all()
                    levtwo_ans=LevelTwoAnswer.objects.all()
                    levthree_ans=LevelThreeAnswer.objects.all()
                    levfour_ans=LevelFourAnswer.objects.all()
                    levfive_ans=LevelFiveAnswer.objects.all()

                    ################ JAMB Post View #############
                    jacct_ans = JAccountAnswer.objects.all()
                    jgeo_ans = JGeoAnswer.objects.all()
                    jbio_ans = JBioAnswer.objects.all()
                    jphy_ans = JPhysicsAnswer.objects.all()
                    jchem_ans = JChemistryAnswer.objects.all()
                    jcomm_ans = JCommerceAnswer.objects.all()
                    jict_ans = JIctAnswer.objects.all()
                    jcrk_ans = JCrkAnswer.objects.all()
                    jlit_ans = JLiteratureAnswer.objects.all()
                    jeco_ans = JEconomicsAnswer.objects.all()
                    jgov_ans = JGovAnswer.objects.all()
                    jeng_ans = JMathAnswer.objects.all()
                    jmath_ans = JEngAnswer.objects.all()
                    
                    num_score=list(set(chain(jacct_ans,jgeo_ans,jbio_ans,jphy_ans,jchem_ans,jcomm_ans,jict_ans,jcrk_ans,jlit_ans,jeco_ans,jgov_ans,jeng_ans,jmath_ans,easy_ans,medium_ans,hard_ans,akwa_ans,xmas_ans,levone_ans,levtwo_ans,levthree_ans,levfour_ans,levfive_ans)))
                    score_count=request.POST.getlist('answer[]',None)
                    score_point=request.POST.getlist('ran_score',None)
                    if type(score_point) == "<class 'list'>" :
                        score_point=int(score_point[0])
                    elif score_point == None:
                        score_point=0
                    
                    # print("ran score",score_point)
                    correct_ans=[correct.correct_answer for correct in num_score]
                    if score_count:
                        contained=[a for a in score_count if a in correct_ans]
                        for scores in contained:
                            score+=10
                        # print(score)
                        data['user_score']=score
                        # score_count.clear()
                        # print(score_count)
                        # print(contained)
                    else:
                        data["score_status"]="Score too low" 

                    now=datetime.datetime.now()
                    time=[9,12,15,18]
                    # num_score=EasyAnswer.objects.all()
                    # correct_ans=[correct.correct_answer for correct in num_score]
                    # print(correct_ans)

                    print(get_level1)
                    # print(request.META.get('HTTP_REFERER'))
                    
                    
                    if score > 0:
                        if get_easy in where_from:
                            if score > 0:
                                # request.session['easycompleted']='easycomplete'
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="easy")
                                PlayerStatistic.objects.create(player=request.user,difficulty="easy",score=score)
                                data["thanks"]="Thanks For playing See You Next Time"
                            elif score > score_point:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="easy")
                                PlayerStatistic.objects.create(player=request.user,difficulty="easy",score=score)
                                data["thanks"]="Thanks For playing See You Next Time"
                            
                        elif get_medium in where_from:
                            if score > 0:
                                # request.session['mediumcompleted']='mediumcomplete'
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="medium")
                                PlayerStatistic.objects.create(player=request.user,difficulty="medium",score=score)
                                data["thanks"]="Thanks For playing See You Next Time"
                            elif score > score_point:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="medium")
                                PlayerStatistic.objects.create(player=request.user,difficulty="medium",score=score)
                                data["thanks"]="Thanks For playing See You Next Time" 
                        elif get_hard in where_from:
                            if score > 0:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="hard")
                                PlayerStatistic.objects.create(player=request.user,difficulty="hard",score=score)
                                data["thanks"]="Thanks For playing See You Next Time"
                            elif score > score_point:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="hard")
                                PlayerStatistic.objects.create(player=request.user,difficulty="hard",score=score)
                                data["thanks"]="Thanks For playing See You Next Time"
                        elif get_akwa in where_from:
                            if score > 0:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="akwa")
                                PlayerStatistic.objects.create(player=request.user,difficulty="akwa",score=score)
                                data["thanks"]="Thanks For playing See You Next Time"
                            elif score > score_point:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="akwa")
                                PlayerStatistic.objects.create(player=request.user,difficulty="akwa",score=score)
                                data["thanks"]="Thanks For playing See You Next Time"

                        elif get_xmas in where_from:
                            if score > 0:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="xmas")
                                PlayerStatistic.objects.create(player=request.user,difficulty="xmas",score=score)
                                data["thanks"]="Thanks For playing See You Next Time"
                            elif score == 100:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="xmas")
                                PlayerStatistic.objects.create(player=request.user,difficulty="xmas",score=score)
                                data["thanks"]="Thanks For playing See You Next Time"

                        elif get_jacct in where_from:
                            if score > 0:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="account")
                                PlayerStatistic.objects.create(player=request.user,difficulty="account",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"
                            elif score == 200:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="account")
                                PlayerStatistic.objects.create(player=request.user,difficulty="account",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"

                        elif get_jbio in where_from:
                            if score > 0:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="biology")
                                PlayerStatistic.objects.create(player=request.user,difficulty="biology",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"
                            elif score == 200:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="biology")
                                PlayerStatistic.objects.create(player=request.user,difficulty="biology",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"
                            
                        elif get_jgeo in where_from:
                            if score > 0:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="geography")
                                PlayerStatistic.objects.create(player=request.user,difficulty="geography",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"
                            elif score == 200:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="geography")
                                PlayerStatistic.objects.create(player=request.user,difficulty="geography",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"

                        elif get_jphy in where_from:
                            if score > 0:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="Physics")
                                PlayerStatistic.objects.create(player=request.user,difficulty="Physics",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"
                            elif score == 200:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="Physics")
                                PlayerStatistic.objects.create(player=request.user,difficulty="Physics",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"

                        elif get_jchem in where_from:
                            if score > 0:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="chemistry")
                                PlayerStatistic.objects.create(player=request.user,difficulty="chemistry",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"
                            elif score == 200:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="chemistry")
                                PlayerStatistic.objects.create(player=request.user,difficulty="chemistry",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"


                        elif get_jict in where_from:
                            if score > 0:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="ict")
                                PlayerStatistic.objects.create(player=request.user,difficulty="ict",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"
                            elif score == 200:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="ict")
                                PlayerStatistic.objects.create(player=request.user,difficulty="ict",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"


                        elif get_jcomm in where_from:
                            if score > 0:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="commerce")
                                PlayerStatistic.objects.create(player=request.user,difficulty="commerce",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"
                            elif score == 200:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="commerce")
                                PlayerStatistic.objects.create(player=request.user,difficulty="commerce",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"

                        elif get_jeng in where_from:
                            if score > 0:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="english")
                                PlayerStatistic.objects.create(player=request.user,difficulty="english",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"
                            elif score == 200:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="english")
                                PlayerStatistic.objects.create(player=request.user,difficulty="english",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"


                        elif get_jmath in where_from:
                            if score > 0:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="mathematics")
                                PlayerStatistic.objects.create(player=request.user,difficulty="mathematics",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"
                            elif score == 200:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="mathematics")
                                PlayerStatistic.objects.create(player=request.user,difficulty="mathematics",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"


                        elif get_jcrk in where_from:
                            if score > 0:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="crk")
                                PlayerStatistic.objects.create(player=request.user,difficulty="crk",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"
                            elif score == 200:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="crk")
                                PlayerStatistic.objects.create(player=request.user,difficulty="crk",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"


                        elif get_jlit in where_from:
                            if score > 0:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="literature")
                                PlayerStatistic.objects.create(player=request.user,difficulty="literature",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"
                            elif score == 200:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="literature")
                                PlayerStatistic.objects.create(player=request.user,difficulty="literature",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"


                        # elif get_eco in where_from:
                        #     if score > 0:
                        #         UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="economics")
                        #         PlayerStatistic.objects.create(player=request.user,difficulty="economics",score=score)
                        #         data["thanks"]="Thanks For Practicing See You Next Time"
                        #     elif score == 200:
                        #         UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="economics")
                        #         PlayerStatistic.objects.create(player=request.user,difficulty="economics",score=score)
                        #         data["thanks"]="Thanks For Practicing See You Next Time"


                        elif get_jgov in where_from:
                            if score > 0:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="government")
                                PlayerStatistic.objects.create(player=request.user,difficulty="government",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"
                            elif score == 200:
                                UserCorrectAnswer.objects.create(winner=True,phone_number=request.user.phone_number,user=request.user,score=score,difficulty="government")
                                PlayerStatistic.objects.create(player=request.user,difficulty="government",score=score)
                                data["thanks"]="Thanks For Practicing See You Next Time"

                        elif get_level1 in where_from:
                            
                            if score == 100:
                                request.session['onecompleted']="onecomplete"
                                
                                # UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="levelone")
                                PlayerStatistic.objects.create(player=request.user,difficulty="levelone",score=score)
                                HighestLevelScore.objects.create(player=request.user,difficulty="levelone",score=score,phone_number=request.user.phone_number)
                                HighestScoreStatistic.objects.create(user=request.user,difficulty="levelone",score=score)
                                data["thanks"]="Thanks For playing See You Next Time"
                            else:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="levelone")
                                PlayerStatistic.objects.create(player=request.user,difficulty="levelone",score=score)
                                data["thanks"]="Thanks For playing See You Next Time" 

                        elif get_level2 in where_from:
                            
                            if score == 100:
                                request.session['twocompleted']="twocomplete"
                                
                                # UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="leveltwo")
                                PlayerStatistic.objects.create(player=request.user,difficulty="leveltwo",score=score)
                                HighestLevelScore.objects.create(player=request.user,difficulty="leveltwo",score=score,phone_number=request.user.phone_number)
                                HighestScoreStatistic.objects.create(user=request.user,difficulty="leveltwo",score=score)
                                data["thanks"]="Thanks For playing See You Next Time"
                            else:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="leveltwo")
                                PlayerStatistic.objects.create(player=request.user,difficulty="leveltwo",score=score)
                                
                                data["thanks"]="Thanks For playing See You Next Time"

                        elif get_level3 in where_from:
                        
                            if score == 100:
                                request.session['threecompleted']="threecomplete"
                                
                                # UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="levelthree")
                                PlayerStatistic.objects.create(player=request.user,difficulty="levelthree",score=score)
                                HighestLevelScore.objects.create(player=request.user,difficulty="levelthree",score=score,phone_number=request.user.phone_number)
                                HighestScoreStatistic.objects.create(userr=request.user,difficulty="levelthree",score=score)
                                data["thanks"]="Thanks For playing See You Next Time"
                            else:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="levelthree")
                                PlayerStatistic.objects.create(player=request.user,difficulty="levelthree",score=score)
                                data["thanks"]="Thanks For playing See You Next Time"

                        elif get_level4 in where_from:
                        
                            if score == 100:
                                request.session['fourcompleted']="fourcomplete"
                                
                                # UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="levelfour")
                                PlayerStatistic.objects.create(player=request.user,difficulty="levelfour",score=score)
                                HighestLevelScore.objects.create(player=request.user,difficulty="levelfour",score=score,phone_number=request.user.phone_number)
                                HighestScoreStatistic.objects.create(user=request.user,difficulty="levelfour",score=score)
                                data["thanks"]="Thanks For playing See You Next Time"
                            else:
                                UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="levelfour")
                                PlayerStatistic.objects.create(player=request.user,difficulty="levelfour",score=score)
                                
                                data["thanks"]="Thanks For playing See You Next Time"

                        elif get_level5 in where_from:
                            UserCorrectAnswer.objects.create(phone_number=request.user.phone_number,user=request.user,score=score,difficulty="levelfive")
                            PlayerStatistic.objects.create(player=request.user,difficulty="levelfive",score=score)
                            HighestScoreStatistic.objects.create(user=request.user,difficulty="levelfive",score=score)
                            data["thanks"]="Thanks For playing See You Next Time" 


                # instance.user = request.user
                # instance.save()
            # message success
                else:
                    data["Sorry"]="You Have Exceeded Your Limit" 
                    return JsonResponse(data)
            else:
                data["busted"]="Hey! I can see You Cheating Backoff. You Spent %s Seconds On The Questions"%time_differ        
                return JsonResponse(data)
        else:
            data["busted"]="Hey! I can see You Cheating Backoff. "
    
        return JsonResponse(data)

import random
@login_required
def quiz(request,username):
    count_player=ActivePlayer.objects.all()
    bonus=None
    loyalty=None
    ran_score=None
    now=xmas_time.now()
    now_time=now.time()
    easy_ran_score=[250,260,270,280,290,300]
    med_ran_score=[200,210,220,230,240,250]
    akwa_ran_score=[200,210,220,230,240,250]
    hard_ran_score=[230,240,250,260,270,280]
    winner=ERCTransaction.objects.all()[:10]
    


    user_score=None
    if count_player:
        for count in count_player:
            count.player_num+=1
            count.save()
    else: 
         ActivePlayer.objects.create(player_num=+1)
    weekday = datetime.datetime.now().strftime('%A') 
    current_day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    user=get_object_or_404(MyUser,username=username)
    try:
        bonus=BonusPointAirtime.objects.get(player=request.user)
        loyalty=MyUser.objects.get(username=request.user.username)
    except BonusPointAirtime.DoesNotExist or MyUser.DoesNotExist:
        pass
    user_score=UserCorrectAnswer.objects.filter(user=request.user).order_by('-timestamp')
    airtime_score=UserCorrectAnswer.objects.all()
    score=0
    data={}
    time_start = request.POST.get('time_start',)
    current_site = request.META['HTTP_HOST']
    where_from = "%s%s"%(current_site,request.get_full_path())
    
    
    get_easy = "%s/recharge/easy/%s/"%(current_site,request.user)
    get_medium = "%s/recharge/medium/%s/"%(current_site,request.user)
    get_hard = "%s/recharge/hard/%s/"%(current_site,request.user)
    get_akwa = "%s/recharge/akwa/%s/"%(current_site,request.user)
    get_xmas = "%s/recharge/xmas/%s/"%(current_site,request.user)
    
    ##############Level Based Score Url Check ##########################

    get_level1 = "%s/recharge/level1/%s"%(current_site,request.user)
    get_level2 = "%s/recharge/level2/%s"%(current_site,request.user)
    get_level3 = "%s/recharge/level3/%s"%(current_site,request.user)
    get_level4 = "%s/recharge/level4/%s"%(current_site,request.user)
    get_level5 = "%s/recharge/level5/%s"%(current_site,request.user)


    ######################### JAMB View Url ##############################
    get_jacct = "%s/jamb/account/%s/"%(current_site,request.user)
    get_jgeo = "%s/jamb/geography/%s/"%(current_site,request.user)
    get_jbio = "%s/jamb/biology/%s/"%(current_site,request.user)
    get_jphy = "%s/jamb/physics/%s/"%(current_site,request.user)
    get_jchem = "%s/jamb/chemistry/%s/"%(current_site,request.user)
    get_jcomm = "%s/jamb/commerce/%s/"%(current_site,request.user)
    get_jict = "%s/jamb/ict/%s/"%(current_site,request.user)
    get_jcrk = "%s/jamb/crk/%s/"%(current_site,request.user)
    get_jlit = "%s/jamb/literature/%s/"%(current_site,request.user)
    get_jeco = "%s/jamb/economics/%s/"%(current_site,request.user)
    get_jgov = "%s/jamb/government/%s/"%(current_site,request.user)
    get_jeng = "%s/jamb/english/%s/"%(current_site,request.user)
    get_jmath = "%s/jamb/mathematics/%s/"%(current_site,request.user)
    level_progress = ""
    time_diff = timezone.now() - timezone.timedelta(hours=3)
    num_played = UserCorrectAnswer.objects.filter(user=request.user,timestamp__gte=time_diff).count()
    if get_level1 in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='levelone').order_by('-score','-timestamp')[:1]
    elif get_level2 in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='leveltwo').order_by('-score','-timestamp')[:1]
    elif get_level3 in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='levelthree').order_by('-score','-timestamp')[:1]
    elif get_level4 in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='levelfour').order_by('-score','-timestamp')[:1]
    elif get_level5 in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='levelfive').order_by('-score','-timestamp')[:1]
    elif get_easy in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='easy').order_by('-score','-timestamp')[:1]
    elif get_medium in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='medium').order_by('-score','-timestamp')[:1]
    elif get_hard in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='hard').order_by('-score','-timestamp')[:1]
    elif get_akwa in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='akwa').order_by('-score','-timestamp')[:1]
    elif get_xmas in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='xmas').order_by('-score','-timestamp')[:1]

    #################################################JAMB View ##############################################
    elif get_jacct in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='account').order_by('-score','-timestamp')[:1]
    elif get_jgeo in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='geography').order_by('-score','-timestamp')[:1]
    elif get_jbio in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='biology').order_by('-score','-timestamp')[:1]
    elif get_jphy in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='physics').order_by('-score','-timestamp')[:1]
    elif get_jchem in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='chemistry').order_by('-score','-timestamp')[:1]
    elif get_jcomm in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='commerce').order_by('-score','-timestamp')[:1]
    elif get_jict in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='ict').order_by('-score','-timestamp')[:1]
    elif get_jcrk in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='crk').order_by('-score','-timestamp')[:1]
    elif get_jlit in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='literature').order_by('-score','-timestamp')[:1]
    elif get_jeco in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='economics').order_by('-score','-timestamp')[:1]
    elif get_jgov in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='government').order_by('-score','-timestamp')[:1]
    elif get_jeng in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='english').order_by('-score','-timestamp')[:1]
    elif get_jmath in where_from:
        all_score=UserCorrectAnswer.objects.filter(difficulty='mathematics').order_by('-score','-timestamp')[:1]
    # context={"easy":easy,"user_score":user_score,"all_score":all_score,"level_progress":level_progress}
    data['questions'] = render_to_string('recharge/high-score-based/easy_partial.html', {})
    if num_played < 20:
                   ############################# JAMB Question ################################
            
            if get_jacct in where_from:
                    easy=JAccountAnswer.objects.all().order_by('?')[:20]
                    num_score=JAccountAnswer.objects.all()[:20]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="account").order_by('-timestamp')[:1]

            elif get_jgeo in where_from:
                    easy=JGeoAnswer.objects.all().order_by('?')[:20]
                    num_score=JGeoAnswer.objects.all()[:20]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="geography").order_by('-timestamp')[:1]

            elif get_jbio in where_from:
                    easy=JBioAnswer.objects.all().order_by('?')[:20]
                    num_score=JBioAnswer.objects.all()[:20]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="biology").order_by('-timestamp')[:1]

            elif get_jphy in where_from:
                    easy=JPhysicsAnswer.objects.all().order_by('?')[:20]
                    num_score=JPhysicsAnswer.objects.all()[:20]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="physics").order_by('-timestamp')[:1]

            elif get_jchem in where_from:
                    easy=JChemistryAnswer.objects.all().order_by('?')[:20]
                    num_score=JChemistryAnswer.objects.all()[:20]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="chemistry").order_by('-timestamp')[:1]

            elif get_jcomm in where_from:
                    easy=JCommerceAnswer.objects.all().order_by('?')[:20]
                    num_score=JCommerceAnswer.objects.all()[:20]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="commerce").order_by('-timestamp')[:1]

            elif get_jict in where_from:
                    easy=JIctAnswer.objects.all().order_by('?')[:20]
                    num_score=JIctAnswer.objects.all()[:20]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="ict").order_by('-timestamp')[:1]

            elif get_jcrk in where_from:
                    easy=JCrkAnswer.objects.all().order_by('?')[:20]
                    num_score=JCrkAnswer.objects.all()[:20]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="crk").order_by('-timestamp')[:1]

            elif get_jeng in where_from:
                    easy=JEngAnswer.objects.all().order_by('?')[:20]
                    num_score=JEngAnswer.objects.all()[:20]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="english").order_by('-timestamp')[:1]

            elif get_jmath in where_from:
                    easy=JMathAnswer.objects.all().order_by('?')[:20]
                    num_score=JMathAnswer.objects.all()[:20]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="mathematics").order_by('-timestamp')[:1]
           
            elif get_jlit in where_from:
                    easy=JLiteratureAnswer.objects.all().order_by('?')[:20]
                    num_score=JLiteratureAnswer.objects.all()[:20]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="literature").order_by('-timestamp')[:1]

            elif get_jeco in where_from:
                    easy=JEconomicsAnswer.objects.all().order_by('?')[:20]
                    num_score=JEconomicsAnswer.objects.all()[:20]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="economics").order_by('-timestamp')[:1]

            elif get_jgov in where_from:
                    easy=JGovAnswer.objects.all().order_by('?')[:20]
                    num_score=JGovAnswer.objects.all()[:20]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="government").order_by('-timestamp')[:1]
            if weekday not in current_day:
                messages.error(request,"This Game is only opened from Mondays to Saturdays")
                return redirect("/")
            if not time(6,00) <= now_time <= time(23,59):
                messages.error(request,"This Game is only opened from 6a.m to 12 midnight")
                return redirect("/")
            if not time(6,00) <= now_time <= time(21,50) and weekday == 'Sunday':
                messages.error(request,"This Game is only opened from 6 a.m to 9 p.m")
                return redirect("/")

            if get_level1 in where_from:
                easy=LevelOneAnswer.objects.all().order_by('?')[:10]
                num_score=LevelOneAnswer.objects.all()[:10]
                user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="levelone").order_by('-timestamp')[:1]
            
            elif get_level2 in where_from:
                if "onecompleted"  in request.session:
                    level_progress = "leveltwo"
                    easy=LevelTwoAnswer.objects.all().order_by('?')[:10]
                    num_score=LevelTwoAnswer.objects.all()[:10]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="leveltwo").order_by('-timestamp')[:1]
                    del request.session['onecompleted']
                else:
                    messages.error(request,"You need to complete the previous level to move to this level")
                    return redirect("/")
            
            elif get_level3 in where_from:
                if "twocompleted" in request.session:
                    level_progress = "levelthree"
                    easy=LevelThreeAnswer.objects.all().order_by('?')[:10]
                    num_score=LevelThreeAnswer.objects.all()[:10]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="levelthree").order_by('-timestamp')[:1]
                    del request.session['twocompleted']
                else:
                    messages.error(request,"You need to complete the previous level to move to this level")
                    return redirect("/")
            
            elif get_level4 in where_from:
                if "threecompleted" in request.session:
                    level_progress = "levelfour"
                    easy=LevelFourAnswer.objects.all().order_by('?')[:10]
                    num_score=EasyAnswer.objects.all()[:10]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="levelfour").order_by('-timestamp')[:1]
                    del request.session['threecompleted']
                else:
                    messages.error(request,"You need to complete the previous level to move to this level")
                    return redirect("/")
            
            elif get_level5 in where_from:
                if  "fourcompleted" in request.session:
                    level_progress = "levelfive"
                    easy=LevelFiveAnswer.objects.all().order_by('?')[:10]
                    num_score=LevelFiveAnswer.objects.all()[:10]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="levelfive").order_by('-timestamp')[:1]
                    del request.session['fourcompleted']
                else:
                    messages.error(request,"You need to complete the previous level to move to this level")
                    return redirect("/")
            
            elif get_easy in where_from:
                # if  "easycompleted" in request.session:
                    # level_progress = "easy"
                    pick=random.choice(easy_ran_score)
                    ran_score=pick
                    easy=EasyAnswer.objects.all().order_by('?')[:50]
                    num_score=EasyAnswer.objects.all()[:50]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="easy").order_by('-timestamp')[:1]
                    # del request.session['easycompleted']?\
                # else:
                    # messages.error(request,"You need to complete the previous level to move to this level")
                    # return redirect("/")
            
            elif get_medium in where_from:
                # if  "easycompleted" in request.session:
                    # level_progress = "medium"
                    pick=random.choice(med_ran_score)
                    ran_score=pick
                    easy=MediumAnswer.objects.all().order_by('?')[:50]
                    num_score=MediumAnswer.objects.all()[:50]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="medium").order_by('-timestamp')[:1]
                    # del request.session['easycompleted']
                # else:
                    # messages.error(request,"You need to complete the previous level to move to this level")
                    # return redirect("/")

            
            elif get_hard in where_from:
                    pick=random.choice(hard_ran_score)
                    ran_score=pick
                    easy=HardAnswer.objects.all().order_by('?')[:50]
                    num_score=HardAnswer.objects.all()[:50]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="hard").order_by('-timestamp')[:1]
            elif get_akwa in where_from:

                    pick=random.choice(akwa_ran_score)
                    ran_score=pick
                    easy=AkwaIbomAnswer.objects.all().order_by('?')[:50]
                    num_score=AkwaIbomAnswer.objects.all()[:50]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="akwa").order_by('-timestamp')[:1]


     

   



            elif get_xmas in where_from:
                    eligible_user=PlayerStatistic.objects.filter(player=request.user).count()
                    print("My Eligible User Count",eligible_user)
                    # user_arr=[]
                    # for user in eligible_user:
                        # user_arr.append(user.username)
                    # print(user_arr)
                    now=xmas_time.now()
                    now_time=now.time()
                    if eligible_user < 5:
                        messages.error(request,"You need to have attempted any of the other Earn Airtime modes to be eligible for the 10-seconds Offer")
                        return redirect("/")
                    if not time(18,00) <= now_time <= time(19,00):
                        messages.error(request,"This Game is only opened from 6 p.m to 7:00 p.m")
                        return redirect("/")
                # if  "mediumcompleted" in request.session:
                    # pick=random.choice(hard_ran_score)
                    # ran_score=pick
                    level_progress = "xmas"
                    easy=HardAnswer.objects.all().order_by('?')[:10]
                    num_score=HardAnswer.objects.all()[:10]
                    user_score=UserCorrectAnswer.objects.filter(user=request.user,difficulty="xmas").order_by('-timestamp')[:1]
                    # del request.session['mediumcompleted']
                # else:
                    # messages.error(request,"You need to complete the previous level to move to this level")
                    # return redirect("/")

            else:
                
                context={"level_progress":level_progress,"bonus_point":bonus,"loyalty":loyalty}
                return render(request,"recharge/high-score-based/easy.html",context)
                easy=EasyAnswer.objects.all().order_by('?')[:50]
                num_score=EasyAnswer.objects.all()[:50]


                if num_score:
                    all_score=UserCorrectAnswer.objects.all().order_by('-score','-timestamp')[:1]
                    # user_score=UserCorrectAnswer.objects.filter(user=request.user).order_by('-timestamp')[:1]
                else:
                    messages.error(request,"No questions available yet")
                    return redirect("/")
            context={"winner":winner,"ran_score":ran_score,"bonus_point":bonus,"loyalty":loyalty,"easy":easy,"user_score":user_score,"all_score":all_score,"level_progress":level_progress}
            template="recharge/high-score-based/easy.html"
            return render(request,template,context)
            
    else:
        messages.error(request,"You have played your limit for an hour.")
        return redirect("/")
   

def add_bonus(request):
        current_site=request.META['HTTP_HOST']
        get_easy="%s/recharge/easy/%s/"%(current_site,request.user)
        get_med="%s/recharge/medium/%s/"%(current_site,request.user)
        get_hard="%s/recharge/hard/%s/"%(current_site,request.user)
        get_akwa="%s/recharge/akwa/%s/"%(current_site,request.user)
        where_from= "%s%s"%(current_site,request.get_full_path())
        invite = request.POST.get('bonus')
        # print("Am current bonus",invite)
        data=dict()
        time_diff = timezone.now() - timezone.timedelta(hours=1)
        if request.method == 'POST':
            if invite and int(invite) > 0:
                try:
                    my_score=[]
                    invite=int(invite)
                    get_score=UserCorrectAnswer.objects.filter(user=request.user,timestamp__gte=time_diff).order_by("-score")[:1]
                    for get in get_score:
                        my_score.append(get.score)
                        sum_bonus=invite + my_score[0]
                        # return JsonResponse(data)
                    del my_score[:]
                    # print("My Score",sum_bonus)
                    airtime_score=UserCorrectAnswer.objects.filter(user=request.user,timestamp__gte=time_diff).order_by("-score")[:1]
                    for airtime in airtime_score:
                        airtime.score = sum_bonus
                        airtime.save()
                        bonus=BonusPointAirtime.objects.get(player=request.user)
                        bonus.bonus_points=0
                        bonus.save()
                        data['bonus_added']=bonus.bonus_points
                        data['tapscore_added']="Your airtime score is now {}".format(airtime.score)
                        return JsonResponse(data)
                    for airtime_score in airtime_score:
                        data['tapscore_added']="Your airtime score is now {}".format(airtime_score.score)
                        return JsonResponse(data)
                except BonusPointAirtime.DoesNotExist:
                    data['bonus_error']="Sorry You Don't Have Any Bonus or Airtime Score At The Moment"	 
                return JsonResponse(data)
            elif int(loyalty) > 0:
                try:
                    my_score=[]
                    loyalty=int(loyalty)

                    get_score=UserCorrectAnswer.objects.filter(user=request.user,timestamp__gte=time_diff).order_by("-score")[:1]
                                        
                    for get in get_score:
                        my_score.append(get.score)

                    print("Loyal Score",my_score)
                    if loyalty > 100:
                        h_bonus=loyalty - 100
                        sum_bonus=100 + my_score[0]
                        del my_score[:]
                    else:
                        h_bonus=0
                        sum_bonus = loyalty + my_score[0]
                    
                        del my_score[:]
                

                    print("My Score",sum_bonus,h_bonus,r_bonus)
                    tap_score=UserCorrectAnswer.objects.filter(user=request.user,timestamp__gte=time_diff).order_by("-score")[:1]
                    for tap in tap_score:
                        tap.score = sum_bonus
                        tap.save()
                        
                        
                        bonus=MyUser.objects.get(username=request.user.username)
                        bonus.loyalty_point=h_bonus
                        r_bonus=h_bonus
                        bonus.save()
                        
                        data['bonus_added']=bonus.loyalty_point
                        data["bonus_left"]=r_bonus
                        data['tapscore_added']="Your tap score is now{}".format(tap.score)
                        return JsonResponse(data)
                    for tap_score in tap_score:
                        data['tapscore_added']="Your tap score is now{}".format(tap_score.score)
                except MyUser.DoesNotExist:
                    data['bonus_error']="Sorry You Don't Have Any Bonus or Tap Score At The Moment"	 
                    return JsonResponse(data)
            else:
                data['bonus_error']="Sorry You Don't Have Any Bonus or Tap Score At The Moment"
                return JsonResponse(data)
            

        else:
            return JsonResponse(data)
	

def send_invite(request):
	invite = request.POST.get('number',).split(",")
	invite_arr=invite
	invite_len=len(invite_arr)
	bonus_points = 5 * invite_len
	

	
	data=dict()
	# for arr in invite:
	# 	invite_list.append(arr)
	text_message="Your Friend %s,has invited you to play Freeairtime & stand a chance to earn free airtime! Click freeairtime.wstreams.com/ to play (No data charges)"%request.user.get_full_name
	bonus_update=[]
	if request.method == 'POST':
		# print(invite)
		try: 	
				bonus= BonusPointAirtime.objects.get(player=request.user)
				print(bonus.list_numbers)
				for inv in invite:
					if not inv in bonus.list_numbers:
						bonus_update.append(inv)
						invite_len=len(bonus_update)
						bonus_ps = 5 * invite_len
						bonus.bonus_points+=bonus_ps
						bonus.list_numbers=bonus.list_numbers+str(","+inv)
						bonus.save()
						res=sms_client.send(to=invite, text=text_message)
						del bonus_update[:]
						data['sent']="You Have Successfully sent the sms"
						print("This is the lenght",len(invite_arr))
					else:
						print("It is present")
						data['onlyOnce']="You already invited this person"
		except BonusPointAirtime.DoesNotExist:
			BonusPointAirtime.objects.create(player=request.user,bonus_points=bonus_points,list_numbers=invite)

		
		# print(res)
	# data["Sorry"]="You Have Exceeded Your Limit"
		return JsonResponse(data)
	else:
		data['Post']="This is not a post request"
		return JsonResponse(data)
	
def get_winners(request):
    high_score = PlayerStatistic.objects.all()
    # play_stat=PlayerStatistic.objects.all()
    for winner in high_score.iterator():
        # if not winner.phone_number == None:
            # print("Loading Numbers")
            user_num=MyUser.objects.get(username=winner.player.username)
            PlayerStatistic.objects.filter(player__username=user_num.username).update(phone_number=user_num.phone_number)
        # else:
        #     print("Already Exist")
        #     pass
    return HttpResponse("Well directed")


def download_exce_data(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="wstreams_excel_data_%s.xls"'%datetime.datetime.now()
    wb= xlwt.Workbook(encoding='utf-8')
    ws= wb.add_sheet("sheet1")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold =True
    columns= ['Name','Phone Number','Score','Time Created','Difficulty']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style =xlwt.XFStyle()
    data = PlayerStatistic.objects.all()[9000:12000]
    for my_row in data:

        row_num = row_num + 1
        ws.write(row_num,0,my_row.player.username, font_style)
        ws.write(row_num,1,my_row.phone_number, font_style)
        ws.write(row_num,2,my_row.score, font_style)
        ws.write(row_num,3,my_row.timestamp.strftime("%Y-%m-%d"), font_style)
        ws.write(row_num,4,my_row.difficulty, font_style)
    wb.save(response)
    return response