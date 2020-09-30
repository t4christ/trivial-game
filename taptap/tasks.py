from __future__ import absolute_import, unicode_literals
import random
from django.conf import settings
from celery.decorators import task
from datetime import datetime, time
from taptap.models import *
# from recharge.models import UserCorrectAnswer
from accounts.models import MyUser
from erc.models import ERCTransaction
import json
import urllib
import requests 
from requests.auth import AuthBase
import logging
import os
os.environ['http_proxy']=''

import logging
from django.core.mail import send_mail
from quiz.celery import app
# from posts.models import Post
from datetime import datetime
from django.utils import timezone
from utils.smsclient import SmsClient

sms_client=SmsClient()



class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['Authorization'] = f'Bearer {self.token}'  # Python 3.6+
        return r


def recharge_session(username,difficulty,login_payload,url,phone_number,amount):
    try:
        with requests.Session() as session:

            response = session.post("https://clients.primeairtime.com/api/auth",json=login_payload)
            use_token = response.json().get('token',None)

            recharge='https://clients.primeairtime.com/api/topup/exec/%s/'%phone_number
            recharge_payload={"product_id": "MFIN-5-OR",
            "denomination" :amount,
            "send_sms" : True,
            "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N50! Keep on Tapping,spread the word!!!"}
            
            if recharge:
                        recharge_response = session.post(recharge,data=recharge_payload,auth=TokenAuth(use_token))
                        print(recharge_response.json())
                        get_data = recharge_response.json()
                        if get_data['status'] == 201:
                            ERCTransaction.objects.create(target=username,difficulty=difficulty,status=get_data['status'],
                            product_id=get_data['product_id'],reference=get_data['reference'],phone_number=phone_number,
                            code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                            paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                        else:
                            ERCTransaction.objects.create(target=username,status="Failed")
            return ("Recharge Successful")
    except Exception as e:
        print("Recharge Error",e)
        return ("Recharge Failed. Check your logs for reasons why.")



def test_recharge(username,difficulty,phone_number,amount):
            username = str(settings.ERC_USER)
            password = (settings.ERC_PASS)
            url =  settings.ERC_LOGIN_URL 
            print("User and pass",username,password,url)
                        
            login_payload={
                    'action':'login',
                    'username':username,
                    'password':password
                    }
            return recharge_session(username,difficulty,login_payload,url,phone_number,amount)


# @task(name="Schedule Mail")
# def send_post_email():
#         time_diff = timezone.now() - timezone.timedelta(minutes=2)
#         post= Post.objects.filter(timestamp__gte=time_diff)
#         if post:
            
#             for post in post:
#                 send_mail('New Post on Gist','%s by %s was posted.'%(post.title,post.user),'postmaster@mg.wstreams.com',['amapelete@gmail.com'],fail_silently=False,)
#         else:
#             return("No new Posts Yet")

# @task(name="taptap_sms")
# def tap_sms():
#     now=datetime.now()
#     player=MyUser.objects.all()
#     # play_num=[play.phone_number for play in player]
#     text_message="Taptap has begun join the game to also be part of the winners"
#     text_during="The taptap game is going on join the lucky winners for the 3 hour slot"
#     text_end="The taptap game is about to end join the lucky winners to win airtime"
#     if  not time(9,10)  == now.time() or time(12,10)  == now.time() or time(15,10)  == now.time() or time(18,10) == now.time():
#         # play_num=[play.phone_number for play in player]
#         for play in player:
#             res = sms_client.send(to=play.phone_number, text=text_message)
#             print(res)
#     else:
#         print("No text message yet")
#     if  time(6,10) == now.time() or time(10,10) == now.time() or time(13,10) == now.time() or time(16,10) == now.time() or time(19,10) == now.time():
#         # play_num=[play.phone_number for play in player]
#         for play in player:
#             res = sms_client.send(to=play.phone_number, text=text_during)
#             print(res)

#     else:
#         print("No text during yet")
#     if   time(8,30) == now.time()  or   time(11,30) == now.time() or time(14,30)  == now.time() or time(17,30)  == now.time() or time(20,30)  == now.time():
#         # play_num=[play.phone_number for play in player]
#         for play in player:
#             res = sms_client.send(to=play.phone_number, text=text_end)
        
#     else:
#         print("No text end")







@task(name="taptap_sms")
def tap_sms():
    now=datetime.now()
    num_list=[]
    player=MyUser.objects.all()
    # play_num=[play.phone_number for play in player]
    text_message="The TapTAP 3hour session jut began! Earn some airtime today, click gist.wstreams.com"
    text_during="Have you attempted the TapTAP today? Hurry now, earn some airtime, click gist.wstreams.com"
    text_end="The highest score now is 123, get on TapTAP to beat this score NOW. Click gist.wstreams.com"
    if time(9,10)  == now.time() or time(12,10)  == now.time() or time(15,10)  == now.time() or time(18,10) == now.time():
        # play_num=[play.phone_number for play in player]
        for play in player:
            num_list.append(play.phone_number)
            
        res = sms_client.send(to=num_list, text=text_message)
        print(res)
    else:
        print("No text message yet")
    if  time(6,10) == now.time() or time(10,10) == now.time() or time(13,10) == now.time() or time(16,10) == now.time() or time(19,10) == now.time():
        # play_num=[play.phone_number for play in player]
        for play in player:
            num_list.append(play.phone_number)
            
        res = sms_client.send(to=[num_list], text=text_message)
        print(res)
    else:
        print("No text during yet")
    if   time(8,30) == now.time()  or   time(11,30) == now.time() or time(14,30)  == now.time() or time(17,30)  == now.time() or time(20,30)  == now.time():
        # play_num=[play.phone_number for play in player]
        for play in player:
            num_list.append(play.phone_number)
        res = sms_client.send(to=[num_list], text=text_message)
        print(res)
    else:
        print("No text end")



# @task(name="taptap_sms_reminder")
# def tap_sms_reminder():
#     time_diff = timezone.now() + timezone.timedelta(days=3)
#     now=datetime.now()
#     player=MyUser.objects.all()
#     reminder_three=[]
#     play_num=[play.phone_number for play in player]
#     tap_active_player=TapActivePlayer.objects.filter(timestamp__lte=time_diff)
#     for tap in tap_active_player:
#         reminder_three.append(tap.phone_number)
#         print(reminder_three)
#     text_message="Hope you are fine. We noticed you have not been playing for the past 3 days. Join the taptap game to become a lucky winner. Regards wstreams."
#     if play_num not in reminder_three:
#             res = sms_client.send(to=play_num, text=text_message)
#     else:
#         print("All numbers have played in the past three days")

@task(name="delete_game")
def remove():
        time_diff = timezone.now() + timezone.timedelta(hours=1)
        now=datetime.now()
        tap_score=Taptap.objects.filter(timestamp__lte=time_diff).order_by("-score")
        if time(9,10) <= now.time() <= time(9,15) or time(12,10) <= now.time() <= time(12,15) or time(15,10) <= now.time() <= time(15,15) or time(18,10) <= now.time() <= time(18,15) or time(21,10) <= now.time() <= time(21,15) or time(23,58) <= now.time() <= time(23,59):
            if tap_score:
                highest=[str(highest.player) for highest in tap_score][:1]
                player=MyUser.objects.get(username=highest[0])
                highest_score=[int(highest.score) for highest in tap_score][:1]
                high_create=TapHighestScore.objects.create(player=player,score=highest_score[0])
            else:
                print("No Data Available For This Hour")
            for tap in tap_score: 
                    tap_score=Taptap.objects.all().order_by("-score").delete()
        else:
            print("Not Yet time to deleter")


import ast
import json
@task(name="recharge_time")
def recharge():
    time_diff = timezone.now() - timezone.timedelta(days=5)
    tap_score=Taptap.objects.all().order_by("-score")
    tap_count=TapActivePlayer.objects.all().count()
    tap=[tap.score for tap in tap_score][:1]
    tap_player=[str(tapy.player) for tapy in tap_score][:1]
    if tap_player and tap_count > 9:
        user_num=MyUser.objects.get(username=tap_player[0])
        high_score=ERCTransaction.objects.filter(time__gte=time_diff,target=user_num.username,phone_number=user_num.phone_number).count()
        now=datetime.now()
        now_time=now.time()
        if time(5,59) <= now.time() <= time(21,10) and high_score == 0:
            if time(9,00) <= now.time() <= time(9,2) or time(12,00) <= now.time() <= time(12,2) or time(15,00) <= now.time() <= time(15,2) or time(18,00) <= now.time() <= time(18,2) or time(21,00) <= now.time() <= time(21,2) or time(23,55) <= now.time() <= time(23,57):
                test_recharge(user_num.username,'taptap',user_num.phone_number,500)
            else:
                    print("Not yet time")
        else:
            return("You can only win once in a day")        #     )
    else:
        print("Not up to twenty players yet")

    # target,status,product_id,reference,code,paid_amount,paid_currency,topup_amount,topup_currency,time,country,operator_name
        # if tap[0]:
        #     print("{} Your Phone Number {} Has Just Been Credited With The Highest Score of {}".format(user_num,user_num.phone_number,tap[0]))
    


