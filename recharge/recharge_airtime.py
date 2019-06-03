from __future__ import absolute_import, unicode_literals
# import random
from django.conf import settings
# from celery.decorators import task
from datetime import datetime, time
# from recharge.models import UserCorrectAnswer,HighestScoreStatistic,PlayerStatistic,HighestLevelScore
from accounts.models import MyUser
from erc.models import ERCTransaction
import json
import urllib
from requests import session
import logging
from django.core.mail import send_mail
# from quiz.celery import app
from datetime import datetime
from django.utils import timezone
 
def levelone(level_credit,high_score,user_num):
        recharge_payload=None
        username = str(settings.ERC_USER)
        password = (settings.ERC_PASS)
        url =  settings.ERC_LOGIN_URL #'https://mobifinng.primeairtime.com/api/topup/status/'    #settings.ERC_LOGIN_URL
                # status = 'https://mobifinng.primeairtime.com/api/topup/info/2347063419292/'
        recharge='https://mobifinng.primeairtime.com/api/topup/exec/%s/'%user_num.phone_number    
        login_payload={
        'action':'login',
        'username':username,
        'password':password
        }
        if level_credit[0] == 'levelone' and high_score < 2:
                recharge_payload={
            # "message":"This is working"
                "product_id": "MFIN-5-OR",
                "denomination" :5,
                "send_sms" : True,
                "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                    }
        else:
            print("levelone not yet ready")

        with session() as c:

                        null = " "
                        false = " "
                        c.post(url,data=login_payload)
                        values = { 'username': username,'password': password }
                        data = urllib.parse.urlencode(values)
                        data = data.encode('utf-8') # data should be bytes
                        req = urllib.request.Request(url, data)	
                        resp = urllib.request.urlopen(req)
                        respData = resp.read()
                        get_token=json.loads(respData)
                        use_token=get_token['token']
                        print(use_token)
                        second_get={'Authorization':'Bearer {}'.format(use_token)}
                        print(second_get)
                        response = c.post(recharge,data=recharge_payload,headers=second_get)
                        print(response.text)
                        retrieve=response.text
                        get_data=json.loads(retrieve)
                        if response.text and get_data['status'] == 201:
                            ERCTransaction.objects.create(target=get_data['target'],status=get_data['status'],
                            product_id=get_data['product_id'],reference=get_data['reference'],
                            code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                            paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                        else:
                            ERCTransaction.objects.create(target=user_num.phone_number,status="Failed")



def leveltwo(level_credit,high_score,user_num):
            recharge_payload=None
            username = str(settings.ERC_USER)
            password = (settings.ERC_PASS)
            url =  settings.ERC_LOGIN_URL #'https://mobifinng.primeairtime.com/api/topup/status/'    #settings.ERC_LOGIN_URL
        # status = 'https://mobifinng.primeairtime.com/api/topup/info/2347063419292/'
            recharge='https://mobifinng.primeairtime.com/api/topup/exec/%s/'%user_num.phone_number    
            login_payload={
            'action':'login',
            'username':username,
            'password':password
            }
            if level_credit[0] == 'leveltwo' and high_score < 2:
                    recharge_payload={
                # "message":"This is working"
                    "product_id": "MFIN-5-OR",
                    "denomination" :200,
                    "send_sms" : True,
                    "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                        }
            else:
                print("leveltwo not yet ready")
            with session() as c:

                        null = " "
                        false = " "
                        c.post(url,data=login_payload)
                        values = { 'username': username,'password': password }
                        data = urllib.parse.urlencode(values)
                        data = data.encode('utf-8') # data should be bytes
                        req = urllib.request.Request(url, data)	
                        resp = urllib.request.urlopen(req)
                        respData = resp.read()
                        get_token=json.loads(respData)
                        use_token=get_token['token']
                        print(use_token)
                        second_get={'Authorization':'Bearer {}'.format(use_token)}
                        print(second_get)
                        response = c.post(recharge,data=recharge_payload,headers=second_get)
                        print(response.text)
                        retrieve=response.text
                        get_data=json.loads(retrieve)
                        if response.text and get_data['status'] == 201:
                            ERCTransaction.objects.create(target=get_data['target'],status=get_data['status'],
                            product_id=get_data['product_id'],reference=get_data['reference'],
                            code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                            paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                        else:
                            ERCTransaction.objects.create(target=user_num.phone_number,status="Failed")



def levelthree(level_credit,high_score,user_num):
            recharge_payload=None
            username = str(settings.ERC_USER)
            password = (settings.ERC_PASS)
            url =  settings.ERC_LOGIN_URL #'https://mobifinng.primeairtime.com/api/topup/status/'    #settings.ERC_LOGIN_URL
        # status = 'https://mobifinng.primeairtime.com/api/topup/info/2347063419292/'
            recharge='https://mobifinng.primeairtime.com/api/topup/exec/%s/'%user_num.phone_number    
            login_payload={
            'action':'login',
            'username':username,
            'password':password
            }
            if level_credit[0] == 'levelthree' and high_score < 2:
                    recharge_payload={
                # "message":"This is working"
                    "product_id": "MFIN-5-OR",
                    "denomination" :5,
                    "send_sms" : True,
                    "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                        }
            else:
                print("levelthree not yet ready")
            with session() as c:

                        null = " "
                        false = " "
                        c.post(url,data=login_payload)
                        values = { 'username': username,'password': password }
                        data = urllib.parse.urlencode(values)
                        data = data.encode('utf-8') # data should be bytes
                        req = urllib.request.Request(url, data)	
                        resp = urllib.request.urlopen(req)
                        respData = resp.read()
                        get_token=json.loads(respData)
                        use_token=get_token['token']
                        print(use_token)
                        second_get={'Authorization':'Bearer {}'.format(use_token)}
                        print(second_get)
                        response = c.post(recharge,data=recharge_payload,headers=second_get)
                        print(response.text)
                        retrieve=response.text
                        get_data=json.loads(retrieve)
                        if response.text and get_data['status'] == 201:
                            ERCTransaction.objects.create(target=get_data['target'],status=get_data['status'],
                            product_id=get_data['product_id'],reference=get_data['reference'],
                            code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                            paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                        else:
                            ERCTransaction.objects.create(target=user_num.phone_number,status="Failed")



def levelfour(level_credit,high_score,user_num):
            recharge_payload=None
            username = str(settings.ERC_USER)
            password = (settings.ERC_PASS)
            url =  settings.ERC_LOGIN_URL #'https://mobifinng.primeairtime.com/api/topup/status/'    #settings.ERC_LOGIN_URL
        # status = 'https://mobifinng.primeairtime.com/api/topup/info/2347063419292/'
            recharge='https://mobifinng.primeairtime.com/api/topup/exec/%s/'%user_num.phone_number    
            login_payload={
            'action':'login',
            'username':username,
            'password':password
            }
            if level_credit[0] == 'levelfour' and high_score < 2:
                    recharge_payload={
                # "message":"This is working"
                    "product_id": "MFIN-5-OR",
                    "denomination" :5,
                    "send_sms" : True,
                    "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                        }
            else:
                print("levelthree not yet ready")
            with session() as c:

                        null = " "
                        false = " "
                        c.post(url,data=login_payload)
                        values = { 'username': username,'password': password }
                        data = urllib.parse.urlencode(values)
                        data = data.encode('utf-8') # data should be bytes
                        req = urllib.request.Request(url, data)	
                        resp = urllib.request.urlopen(req)
                        respData = resp.read()
                        get_token=json.loads(respData)
                        use_token=get_token['token']
                        print(use_token)
                        second_get={'Authorization':'Bearer {}'.format(use_token)}
                        print(second_get)
                        response = c.post(recharge,data=recharge_payload,headers=second_get)
                        print(response.text)
                        retrieve=response.text
                        get_data=json.loads(retrieve)
                        if response.text and get_data['status'] == 201:
                            ERCTransaction.objects.create(target=get_data['target'],status=get_data['status'],
                            product_id=get_data['product_id'],reference=get_data['reference'],
                            code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                            paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                        else:
                            ERCTransaction.objects.create(target=user_num.phone_number,status="Failed")



def levelfive(level_credit,high_score,user_num):
            recharge_payload=None
            username = str(settings.ERC_USER)
            password = (settings.ERC_PASS)
            url =  settings.ERC_LOGIN_URL #'https://mobifinng.primeairtime.com/api/topup/status/'    #settings.ERC_LOGIN_URL
        # status = 'https://mobifinng.primeairtime.com/api/topup/info/2347063419292/'
            recharge='https://mobifinng.primeairtime.com/api/topup/exec/%s/'%user_num.phone_number    
            login_payload={
            'action':'login',
            'username':username,
            'password':password
            }
            if level_credit[0] == 'levelfive' and high_score < 2:
                    recharge_payload={
                # "message":"This is working"
                    "product_id": "MFIN-5-OR",
                    "denomination" :5,
                    "send_sms" : True,
                    "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                        }
            else:
                print("levelfive not yet ready")
            with session() as c:

                        null = " "
                        false = " "
                        c.post(url,data=login_payload)
                        values = { 'username': username,'password': password }
                        data = urllib.parse.urlencode(values)
                        data = data.encode('utf-8') # data should be bytes
                        req = urllib.request.Request(url, data)	
                        resp = urllib.request.urlopen(req)
                        respData = resp.read()
                        get_token=json.loads(respData)
                        use_token=get_token['token']
                        print(use_token)
                        second_get={'Authorization':'Bearer {}'.format(use_token)}
                        print(second_get)
                        response = c.post(recharge,data=recharge_payload,headers=second_get)
                        print(response.text)
                        retrieve=response.text
                        get_data=json.loads(retrieve)
                        if response.text and get_data['status'] == 201:
                            ERCTransaction.objects.create(target=get_data['target'],status=get_data['status'],
                            product_id=get_data['product_id'],reference=get_data['reference'],
                            code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                            paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                        else:
                            ERCTransaction.objects.create(target=user_num.phone_number,status="Failed")




def easy(level_credit,high_score,user_num):
            recharge_payload=None
            username = str(settings.ERC_USER)
            password = (settings.ERC_PASS)
            url =  settings.ERC_LOGIN_URL #'https://mobifinng.primeairtime.com/api/topup/status/'    #settings.ERC_LOGIN_URL
        # status = 'https://mobifinng.primeairtime.com/api/topup/info/2347063419292/'
            recharge='https://mobifinng.primeairtime.com/api/topup/exec/%s/'%user_num.phone_number    
            login_payload={
            'action':'login',
            'username':username,
            'password':password
            }
            if level_credit[0] == 'easy' and high_score < 2:
                    recharge_payload={
                # "message":"This is working"
                    "product_id": "MFIN-5-OR",
                    "denomination" :0,
                    "send_sms" : True,
                    "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                        }
            else:
                print("easy not yet ready")
            with session() as c:

                        null = " "
                        false = " "
                        c.post(url,data=login_payload)
                        values = { 'username': username,'password': password }
                        data = urllib.parse.urlencode(values)
                        data = data.encode('utf-8') # data should be bytes
                        req = urllib.request.Request(url, data)	
                        resp = urllib.request.urlopen(req)
                        respData = resp.read()
                        get_token=json.loads(respData)
                        use_token=get_token['token']
                        print(use_token)
                        second_get={'Authorization':'Bearer {}'.format(use_token)}
                        print(second_get)
                        response = c.post(recharge,data=recharge_payload,headers=second_get)
                        print(response.text)
                        retrieve=response.text
                        get_data=json.loads(retrieve)
                        if response.text and get_data['status'] == 201:
                            ERCTransaction.objects.create(target=get_data['target'],status=get_data['status'],
                            product_id=get_data['product_id'],reference=get_data['reference'],
                            code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                            paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                        else:
                            ERCTransaction.objects.create(target=user_num.phone_number,status="Failed")




def medium(level_credit,high_score,user_num):
            recharge_payload=None
            username = str(settings.ERC_USER)
            password = (settings.ERC_PASS)
            url =  settings.ERC_LOGIN_URL #'https://mobifinng.primeairtime.com/api/topup/status/'    #settings.ERC_LOGIN_URL
        # status = 'https://mobifinng.primeairtime.com/api/topup/info/2347063419292/'
            recharge='https://mobifinng.primeairtime.com/api/topup/exec/%s/'%user_num.phone_number    
            login_payload={
            'action':'login',
            'username':username,
            'password':password
            }
            if level_credit[0] == 'medium' and high_score < 2:
                    recharge_payload={
                # "message":"This is working"
                    "product_id": "MFIN-5-OR",
                    "denomination" :0,
                    "send_sms" : True,
                    "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                        }
            else:
                print("medium not yet ready")
            with session() as c:

                        null = " "
                        false = " "
                        c.post(url,data=login_payload)
                        values = { 'username': username,'password': password }
                        data = urllib.parse.urlencode(values)
                        data = data.encode('utf-8') # data should be bytes
                        req = urllib.request.Request(url, data)	
                        resp = urllib.request.urlopen(req)
                        respData = resp.read()
                        get_token=json.loads(respData)
                        use_token=get_token['token']
                        print(use_token)
                        second_get={'Authorization':'Bearer {}'.format(use_token)}
                        print(second_get)
                        response = c.post(recharge,data=recharge_payload,headers=second_get)
                        print(response.text)
                        retrieve=response.text
                        get_data=json.loads(retrieve)
                        if response.text and get_data['status'] == 201:
                            ERCTransaction.objects.create(target=get_data['target'],status=get_data['status'],
                            product_id=get_data['product_id'],reference=get_data['reference'],
                            code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                            paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                        else:
                            ERCTransaction.objects.create(target=user_num.phone_number,status="Failed")



def hard(level_credit,high_score,user_num):
            recharge_payload=None
            username = str(settings.ERC_USER)
            password = (settings.ERC_PASS)
            url =  settings.ERC_LOGIN_URL #'https://mobifinng.primeairtime.com/api/topup/status/'    #settings.ERC_LOGIN_URL
        # status = 'https://mobifinng.primeairtime.com/api/topup/info/2347063419292/'
            recharge='https://mobifinng.primeairtime.com/api/topup/exec/%s/'%user_num.phone_number    
            login_payload={
            'action':'login',
            'username':username,
            'password':password
            }
            if level_credit[0] == 'hard' and high_score < 2:
                    recharge_payload={
                # "message":"This is working"
                    "product_id": "MFIN-5-OR",
                    "denomination" :0,
                    "send_sms" : True,
                    "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                        }
            else:
                print("Hard not yet ready")
            with session() as c:

                        null = " "
                        false = " "
                        c.post(url,data=login_payload)
                        values = { 'username': username,'password': password }
                        data = urllib.parse.urlencode(values)
                        data = data.encode('utf-8') # data should be bytes
                        req = urllib.request.Request(url, data)	
                        resp = urllib.request.urlopen(req)
                        respData = resp.read()
                        get_token=json.loads(respData)
                        use_token=get_token['token']
                        print(use_token)
                        second_get={'Authorization':'Bearer {}'.format(use_token)}
                        print(second_get)
                        response = c.post(recharge,data=recharge_payload,headers=second_get)
                        print(response.text)
                        retrieve=response.text
                        get_data=json.loads(retrieve)
                        if response.text and get_data['status'] == 201:
                            ERCTransaction.objects.create(target=get_data['target'],status=get_data['status'],
                            product_id=get_data['product_id'],reference=get_data['reference'],
                            code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                            paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                        else:
                            ERCTransaction.objects.create(target=user_num.phone_number,status="Failed")





# Other Code Sample For Recharges
#############################################################
from __future__ import absolute_import, unicode_literals
import random
from django.conf import settings
from celery.decorators import task
from datetime import datetime, time
from recharge.models import UserCorrectAnswer,HighestScoreStatistic,PlayerStatistic,HighestLevelScore
from accounts.models import MyUser
from erc.models import ERCTransaction
import json
import urllib
from requests import session
import logging
from django.core.mail import send_mail
from quiz.celery import app
from datetime import datetime
from django.utils import timezone
 



@task(name="delete_airtime")
def remove_airtime():
    time_diff = timezone.now() + timezone.timedelta(hours=3)
    player_stat=UserCorrectAnswer.objects.all()
    now=datetime.now()
    recharge_score=UserCorrectAnswer.objects.filter(timestamp__lte=time_diff).order_by("-score")
    if time(9,10) <= now.time() <= time(9,15) or time(12,10) <= now.time() <= time(12,15) or time(15,10) <= now.time() <= time(15,15) or time(18,10) <= now.time() <= time(18,15) or time(21,10) <= now.time() <= time(21,15):
            if recharge_score:
                highest=[str(highest.user) for highest in recharge_score][:1]
                player=MyUser.objects.get(username=highest[0])
                highest_diff=[str(highest.difficulty) for highest in recharge_score][:1]
                highest_score=[int(highest.score) for highest in recharge_score][:1]
                high_create=HighestScoreStatistic.objects.create(user=player,difficulty=highest_diff[0],score=highest_score[0])
            else:
                print("Not Data Available For This Hour")
            for recharge in recharge_score: 
                UserCorrectAnswer.objects.all().order_by("-score").delete()
    else:
        print("Not yet time to delete")
            


@task(name="delete_airtime_level")
def remove_airtime_level():
    now=datetime.now()
    recharge_score=HighestLevelScore.objects.all()
    if time(6,5) <= now.time() <= time(21,2):
            if recharge_score:
                for recharge in recharge_score: 
                    HighestLevelScore.objects.all().delete()[:1]
            else:
                print("No Level Data Available For This Hour")
            
    else:
        print("Not yet time to delete")




@task(name="recharge_airtime_level")
def airtime_level():
    time_diff = timezone.now() + timezone.timedelta(hours=15)
    airtime_score=HighestLevelScore.objects.all().order_by("-score","-timestamp")[:1]
    level_credit=[score.difficulty for score in airtime_score][:1]
    level_player=[score.player for score in airtime_score][:1]
    user_num=None
    if level_player:
        user_num=MyUser.objects.get(username=level_player[0])
        high_score=HighestScoreStatistic.objects.filter(timestamp__lte=time_diff,user=user_num).count()
    else:
        print("No Player Has Completed This Level Yet")
    
    if level_player:
        user_num=MyUser.objects.get(username=level_player[0])
    else:
        print("No Levels Completed Yet")
    if airtime_score:
        now=datetime.now()
        now_time=now.time()
        if time(5,59) <= now.time() <= time(20,59):
            # if time(9,00) <= now.time() <= time(9,2) or time(12,00) <= now.time() <= time(12,2) or time(15,00) <= now.time() <= time(15,2) or time(18,00) <= now.time() <= time(18,2) or time(21,00) <= now.time() <= time(21,2):
                    username = str(settings.ERC_USER)
                    password = (settings.ERC_PASS)
                    url =  settings.ERC_LOGIN_URL #'https://mobifinng.primeairtime.com/api/topup/status/'    #settings.ERC_LOGIN_URL
                # status = 'https://mobifinng.primeairtime.com/api/topup/info/2347063419292/'
                    recharge='https://mobifinng.primeairtime.com/api/topup/exec/%s/'%user_num.phone_number    
                    login_payload={
                    'action':'login',
                    'username':username,
                    'password':password
                    }

                    if level_credit[0] == 'levelone' and high_score < 2:
                            recharge_payload={
                        # "message":"This is working"
                            "product_id": "MFIN-5-OR",
                            "denomination" :5,
                            "send_sms" : True,
                            "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                                }
                    else:
                        print("levelone not yet ready")
                    if level_credit[0] == 'leveltwo' and high_score < 2:
                            recharge_payload={
                        # "message":"This is working"
                            "product_id": "MFIN-5-OR",
                            "denomination" :200,
                            "send_sms" : True,
                            "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                                }
                    else:
                        print("leveltwo not yet ready")
                    if level_credit[0] == 'levelthree' and high_score < 2:
                            recharge_payload={
                        # "message":"This is working"
                            "product_id": "MFIN-5-OR",
                            "denomination" :300,
                            "send_sms" : True,
                            "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                                }
                    else:
                        print('levelthree not yet ready')


                    if level_credit[0] == 'levelfour' and high_score < 2:
                            recharge_payload={
                        # "message":"This is working"
                            "product_id": "MFIN-5-OR",
                            "denomination" :500,
                            "send_sms" : True,
                            "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                                }
                    else:
                        print('levelfour not yet ready')

                    # if level_credit[0] == 'levelfive' and high_score < 2:
                    #         recharge_payload={
                    #     # "message":"This is working"
                    #         "product_id": "MFIN-5-OR",
                    #         "denomination" :1000,
                    #         "send_sms" : True,
                    #         "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                    #             }
                    # else:
                    #     print('levelfive')

                    # if level_credit[0] == 'easy' and high_score < 2:
                    #         recharge_payload={
                    #     # "message":"This is working"
                    #         "product_id": "MFIN-5-OR",
                    #         "denomination" :200,
                    #         "send_sms" : True,
                    #         "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                    #             }
                    # else:
                    #     print('easy is not yet ready')

                    # if level_credit[0] == 'medium' and high_score < 2:
                    #         recharge_payload={
                    #     # "message":"This is working"
                    #         "product_id": "MFIN-5-OR",
                    #         "denomination" :500,
                    #         "send_sms" : True,
                    #         "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                    #             }
                    # else:
                    #     print('medium not yet ready')



                    # if level_credit[0] == 'hard' and high_score < 2:
                    #         recharge_payload={
                    #     # "message":"This is working"
                    #         "product_id": "MFIN-5-OR",
                    #         "denomination" :1000,
                    #         "send_sms" : True,
                    #         "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                    #             }
                    # else:
                    #     pass

                    with session() as c:

                        null = " "
                        false = " "
                        c.post(url,data=login_payload)
                        values = { 'username': username,'password': password }
                        data = urllib.parse.urlencode(values)
                        data = data.encode('utf-8') # data should be bytes
                        req = urllib.request.Request(url, data)	
                        resp = urllib.request.urlopen(req)
                        respData = resp.read()
                        get_token=json.loads(respData)
                        use_token=get_token['token']
                        print(use_token)
                        second_get={'Authorization':'Bearer {}'.format(use_token)}
                        print(second_get)
                        response = c.post(recharge,data=recharge_payload,headers=second_get)
                        print(response.text)
                        retrieve=response.text
                        get_data=json.loads(retrieve)
                        if response.text and get_data['status'] == 201:
                            ERCTransaction.objects.create(target=get_data['target'],status=get_data['status'],
                            product_id=get_data['product_id'],reference=get_data['reference'],
                            code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                            paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                        else:
                            ERCTransaction.objects.create(target=user_num.phone_number,status="Failed")
            # else:
            #      print("Not Yet Time")               
        else:
            print("You can only be credited Once")        #     )
    else:
        print("No High Score Completed Yet")










@task(name="recharge_airtime")
def airtime():
    winner_arr=[]
    recharge_payload=[]
    time_diff = timezone.now() + timezone.timedelta(hours=15)
    airtime_score_levfive=UserCorrectAnswer.objects.filter(difficulty='levelfive').order_by("-score","-timestamp")
    airtime_score_easy=UserCorrectAnswer.objects.filter(difficulty='easy').order_by("-score","-timestamp")
    airtime_score_medium=UserCorrectAnswer.objects.filter(difficulty='medium').order_by("-score","-timestamp")
    airtime_score_hard=UserCorrectAnswer.objects.filter(difficulty='hard').order_by("-score","-timestamp")
    level_credit_levfive=[recharge.difficulty for recharge in airtime_score_levfive][:1]
    level_credit_easy=[recharge.difficulty for recharge in airtime_score_easy][:1]
    level_credit_medium=[recharge.difficulty for recharge in airtime_score_medium][:1]
    level_credit_hard=[recharge.difficulty for recharge in airtime_score_hard][:1]
    # recharge=[recharge.score for recharge in airtime_score_easy][:1]
    recharge_player_easy=[winner_arr.append(str(air.phone_number)) for air in airtime_score_easy][:1]
    recharge_player_medium=[winner_arr.append(str(air.phone_number)) for air in airtime_score_medium][:1]
    recharge_player_hard=[winner_arr.append(str(air.phone_number)) for air in airtime_score_hard][:1]
    recharge_player_levfive=[winner_arr.append(str(air.phone_number)) for air in airtime_score_levfive][:1]

    recharge_play_easynum=[str(air.phone_number) for air in airtime_score_easy][:1]
    recharge_play_mednum=[str(air.phone_number) for air in airtime_score_medium][:1]
    recharge_play_hardnum=[str(air.phone_number) for air in airtime_score_hard][:1]
    recharge_play_levfivenum=[str(air.phone_number) for air in airtime_score_levfive][:1]

    print(recharge_play_easynum,recharge_play_mednum,recharge_play_hardnum)
    print(winner_arr)
    if winner_arr:
        # user_num=MyUser.objects.get(username=recharge_player_easy[0])
        
        now=datetime.now()
        now_time=now.time()
        if time(5,59) <= now.time() <= time(21,5):
            if  not time(9,00) <= now.time() <= time(9,2) or time(12,00) <= now.time() <= time(12,2) or time(15,00) <= now.time() <= time(15,9) or time(18,00) <= now.time() <= time(18,2) or time(21,00) <= now.time() <= time(21,2):
                if recharge_play_easynum in winner_arr:
                    print("My number %s"%user_num)
                    high_score=HighestScoreStatistic.objects.filter(timestamp__lte=time_diff,user=user_num).count()
                    username = str(settings.ERC_USER)
                    password = (settings.ERC_PASS)
                    url =  settings.ERC_LOGIN_URL #'https://mobifinng.primeairtime.com/api/topup/status/'    #settings.ERC_LOGIN_URL
                # status = 'https://mobifinng.primeairtime.com/api/topup/info/2347063419292/'
                    
                    recharge='https://mobifinng.primeairtime.com/api/topup/exec/%s/'%recharge_play_easynum    
                    login_payload={
                    'action':'login',
                    'username':username,
                    'password':password
                    }

                    # if level_credit[0] == 'levelone' and high_score < 2:
                    #         recharge_payload={
                    #     # "message":"This is working"
                    #         "product_id": "MFIN-5-OR",
                    #         "denomination" :100,
                    #         "send_sms" : True,
                    #         "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                    #             }
                    # else:
                    #     print("levelone not yet ready")
                    # if level_credit[0] == 'leveltwo' and high_score < 2:
                    #         recharge_payload={
                    #     # "message":"This is working"
                    #         "product_id": "MFIN-5-OR",
                    #         "denomination" :200,
                    #         "send_sms" : True,
                    #         "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                    #             }
                    # else:
                    #     print("leveltwo not yet ready")
                    # if level_credit[0] == 'levelthree' and high_score < 2:
                    #         recharge_payload={
                    #     # "message":"This is working"
                    #         "product_id": "MFIN-5-OR",
                    #         "denomination" :300,
                    #         "send_sms" : True,
                    #         "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                    #             }
                    # else:
                    #     print('levelthree not yet ready')


                    # if level_credit[0] == 'levelfour' and high_score < 2:
                    #         recharge_payload={
                    #     # "message":"This is working"
                    #         "product_id": "MFIN-5-OR",
                    #         "denomination" :500,
                    #         "send_sms" : True,
                    #         "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                    #             }
                    # else:
                    #     print('levelfour not yet ready')

                    if level_credit_levfive and level_credit_levfive[0] == 'levelfive' and high_score < 2:
                            recharge_payload.append({"product_id": "MFIN-5-OR","denomination" :0,"send_sms" : True,"sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"})
                    else:
                        print('No winner for levelfive')

                    if level_credit_easy and level_credit_easy[0] == 'easy' and high_score < 2:
                            recharge_payload.append({"product_id": "MFIN-5-OR","denomination" :0,"send_sms" : True,"sms_text" : "Congratulations easy!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"})
                    else:
                        print('easy is not yet ready')

                    if level_credit_medium and level_credit_medium[0] == 'medium' and high_score < 2:
                            recharge_payload.append({
                        # "message":"This is working"
                            "product_id": "MFIN-5-OR",
                            "denomination" :0,
                            "send_sms" : True,
                            "sms_text" : "Congratulations medium!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                                })
                    else:
                        print('medium not yet ready')



                    if level_credit_hard and level_credit_hard[0] == 'hard' and high_score < 2:
                            recharge_payload.append({
                        # "message":"This is working"
                            "product_id": "MFIN-5-OR",
                            "denomination" :0,
                            "send_sms" : True,
                            "sms_text" : "Congratulations hard!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                                })
                    else:
                        pass
                    # print('My Recharge%s'%recharge_payload)
                    with session() as c:

                        null = " "
                        false = " "
                        c.post(url,data=login_payload)
                        values = { 'username': username,'password': password }
                        data = urllib.parse.urlencode(values)
                        data = data.encode('utf-8') # data should be bytes
                        req = urllib.request.Request(url, data)	
                        resp = urllib.request.urlopen(req)
                        respData = resp.read()
                        get_token=json.loads(respData)
                        use_token=get_token['token']
                        print(use_token)
                        second_get={'Authorization':'Bearer {}'.format(use_token)}
                        print(second_get)
                        # for recharge_payload in recharge_payload:
                        print("My recharge load number is %s"%user_num)
                        response = c.post(recharge,data=recharge_payload,headers=second_get)
                        print(response.text)
                        retrieve=response.text
                        get_data=json.loads(retrieve)
                        if response.text and get_data['status'] == 201:
                            ERCTransaction.objects.create(target=get_data['target'],status=get_data['status'],
                            product_id=get_data['product_id'],reference=get_data['reference'],
                            code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                            paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                        else:
                            ERCTransaction.objects.create(target=user_num,status="Failed")
            else:
                 print("Not Yet Time")               
        else:
            print("You can only be credited Once")        #     )

    # target,status,product_id,reference,code,paid_amount,paid_currency,topup_amount,topup_currency,time,country,operator_name
        # if tap[0]:
        #     print("{} Your Phone Number {} Has Just Been Credited With The Highest Score of {}".format(user_num,user_num.phone_number,tap[0]))
