from __future__ import absolute_import, unicode_literals
import random
from django.conf import settings
from celery.decorators import task
from datetime import datetime, time
from recharge.models import UserCorrectAnswer,HighestScoreStatistic,PlayerStatistic,HighestLevelScore
from accounts.models import MyUser
from erc.models import ERCTransaction
import json
from requests 
import logging
from django.core.mail import send_mail
from quiz.celery import app
from datetime import datetime
from django.utils import timezone
import random

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['Authorization'] = f'Bearer {self.token}'  # Python 3.6+
        return r


def recharge_session(login_payload,url,phone_number,amount):
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
                            ERCTransaction.objects.create(target='Temitayo',status=get_data['status'],
                            product_id=get_data['product_id'],reference=get_data['reference'],phone_number=phone_number,
                            code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                            paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                        else:
                            ERCTransaction.objects.create(target='Temitayo',status="Failed")
            return HttpResponse("Recharge Successful")
    except Exception as e:
        print("Recharge Error",e)
        return HttpResponse("Recharge Failed. Check your logs for reasons why.")



def test_recharge(phone_number,amount):
            username = str(settings.ERC_USER)
            password = (settings.ERC_PASS)
            url =  settings.ERC_LOGIN_URL 
            print("User and pass",username,password,url)
                        
            login_payload={
                    'action':'login',
                    'username':username,
                    'password':password
                    }
            return recharge_session(login_payload,url,phone_number)


@task(name="delete_airtime")
def remove_airtime():
    time_diff = timezone.now() - timezone.timedelta(hours=3)
    player_stat=UserCorrectAnswer.objects.all()
    now=datetime.now()
    recharge_score=UserCorrectAnswer.objects.filter(timestamp__gte=time_diff).order_by("-score")
    if time(9,10) <= now.time() <= time(9,15) or time(12,10) <= now.time() <= time(12,15) or time(15,10) <= now.time() <= time(15,15) or time(18,10) <= now.time() <= time(18,15) or time(21,10) <= now.time() <= time(21,15):
            if recharge_score:
                highest=[str(highest.user) for highest in recharge_score][:1]
                player=MyUser.objects.get(username=highest[0])
                highest_diff=[str(highest.difficulty) for highest in recharge_score][:1]
                highest_score=[int(highest.score) for highest in recharge_score][:1]
                high_create=HighestScoreStatistic.objects.create(user=player,phone_number=player.phone_number,difficulty=highest_diff[0],score=highest_score[0])
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
    winner_arr=[]
    recharge_payload=[]
    recharge=''
    current_day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',]
    weekday = datetime.now().strftime('%A') 
    time_diff = timezone.now() - timezone.timedelta(days=5)
    airtime_score_akwa=HighestLevelScore.objects.filter(difficulty='akwa').order_by("-score","-timestamp")
    airtime_score_levone=HighestLevelScore.objects.filter(difficulty='levelone').order_by("-score","-timestamp")
    airtime_score_levtwo=HighestLevelScore.objects.filter(difficulty='leveltwo').order_by("-score","-timestamp")
    airtime_score_levthree=HighestLevelScore.objects.filter(difficulty='levelthree').order_by("-score","-timestamp")
    airtime_score_levfour=HighestLevelScore.objects.filter(difficulty='levelfour').order_by("-score","-timestamp")
    level_credit_levone=[recharge.difficulty for recharge in airtime_score_levone][:1]
    level_credit_akwa=[recharge.difficulty for recharge in airtime_score_akwa][:1]
    level_credit_levtwo=[recharge.difficulty for recharge in airtime_score_levtwo][:1]
    level_credit_levthree=[recharge.difficulty for recharge in airtime_score_levthree][:1]
    level_credit_levfour=[recharge.difficulty for recharge in airtime_score_levfour][:1]
    # recharge=[recharge.score for recharge in airtime_score_easy][:1]
    recharge_player_levone=[winner_arr.append(str(air.phone_number)) for air in airtime_score_levone][:1]
    recharge_player_akwa=[winner_arr.append(str(air.phone_number)) for air in airtime_score_akwa][:1]
    recharge_player_levtwo=[winner_arr.append(str(air.phone_number)) for air in airtime_score_levtwo][:1]
    recharge_player_levthree=[winner_arr.append(str(air.phone_number)) for air in airtime_score_levthree][:1]
    recharge_player_levfour=[winner_arr.append(str(air.phone_number)) for air in airtime_score_levfour][:1]

    recharge_play_levonenum=[str(air.phone_number) for air in airtime_score_levone][:1]
    recharge_play_akwanum=[str(air.phone_number) for air in airtime_score_akwa][:1]
    recharge_play_levtwonum=[str(air.phone_number) for air in airtime_score_levtwo][:1]
    recharge_play_levthreenum=[str(air.phone_number) for air in airtime_score_levthree][:1]
    recharge_play_levfournum=[str(air.phone_number) for air in airtime_score_levfour][:1]



    recharge_levone_user=[str(air.player) for air in airtime_score_levone][:1]
    recharge_akwa_user=[str(air.player) for air in airtime_score_akwa][:1]
    recharge_levtwo_user=[str(air.player) for air in airtime_score_levtwo][:1]
    recharge_levthree_user=[str(air.player) for air in airtime_score_levthree][:1]
    recharge_levfour_user=[str(air.player) for air in airtime_score_levfour][:1]

    # print(str(recharge_play_easynum[0]),recharge_play_mednum,recharge_play_hardnum)
    # print(winner_arr)
    if winner_arr:
        # user_num=MyUser.objects.get(username=recharge_player_easy[0])
        
        now=datetime.now()
        now_time=now.time()
        if time(5,59) <= now.time() <= time(21,5)  and weekday in current_day:
            # if   time(9,00) <= now.time() <= time(9,2) or time(12,00) <= now.time() <= time(12,2) or time(15,00) <= now.time() <= time(15,9) or time(18,00) <= now.time() <= time(18,2) or time(21,00) <= now.time() <= time(21,2):
                
                    # print("My number %s"%user_num)
                    
                    username = str(settings.ERC_USER)
                    password = (settings.ERC_PASS)
                    url =  settings.ERC_LOGIN_URL #'https://clients.primeairtime.com/api/topup/status/'    #settings.ERC_LOGIN_URL
                # status = 'https://clients.primeairtime.com/api/topup/info/2347063419292/'
                    
                        
                    login_payload={
                    'action':'login',
                    'username':username,
                    'password':password
                    }

                   

                   
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
                        # print("My recharge load number is %s"%user_num)
                        if recharge_play_levonenum and str(recharge_play_levonenum[0]) in winner_arr and level_credit_levone and level_credit_levone[0] == 'levelone':
                            user_num=MyUser.objects.get(username=recharge_levone_user[0])
                            high_score=ERCTransaction.objects.filter(time__gte=time_diff,target=user_num.username,phone_number=recharge_play_levonenum[0]).count()
                            if high_score == 0:
                                recharge='https://clients.primeairtime.com/api/topup/exec/%s/'%recharge_play_levonenum[0]
                                recharge_payload={"product_id": "MFIN-5-OR",
                                "denomination" :100,
                                "send_sms" : True,
                                "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"}
                            else:
                                print("Level one winner can only win once  in 5 days")
                            if recharge:
                                    response = c.post(recharge,data=recharge_payload,headers=second_get)
                                    print(recharge)
                                    print(response.text)
                                    retrieve=response.text
                                    get_data=json.loads(retrieve)
                                    if response.text and get_data['status'] == 201:
                                        ERCTransaction.objects.create(target=user_num.username,status=get_data['status'],
                                        product_id=get_data['product_id'],reference=get_data['reference'],phone_number=recharge_play_levonenum[0],
                                        code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                                        paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                                    else:
                                        ERCTransaction.objects.create(target=user_num,status="Failed")
                            else:
                                    print("No recharge url available yet")
                        else:
                            print('No winner for leveleone')

                        if recharge_play_akwanum and str(recharge_play_akwanum[0]) in winner_arr and level_credit_akwa and level_credit_akwa[0] == 'akwa':
                            user_num=MyUser.objects.get(username=recharge_levone_user[0])
                            high_score=ERCTransaction.objects.filter(time__gte=time_diff,target=user_num.username,phone_number=recharge_play_akwanum[0]).count()
                            if high_score == 0:
                                recharge='https://clients.primeairtime.com/api/topup/exec/%s/'%recharge_play_akwanum[0]
                                recharge_payload={"product_id": "MFIN-5-OR",
                                "denomination" :100,
                                "send_sms" : True,
                                "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"}
                            else:
                                print("Level one winner can only win once  in 5 days")
                            if recharge:
                                    response = c.post(recharge,data=recharge_payload,headers=second_get)
                                    print(recharge)
                                    print(response.text)
                                    retrieve=response.text
                                    get_data=json.loads(retrieve)
                                    if response.text and get_data['status'] == 201:
                                        ERCTransaction.objects.create(target=user_num.username,status=get_data['status'],
                                        product_id=get_data['product_id'],reference=get_data['reference'],phone_number=recharge_play_akwanum[0],
                                        code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                                        paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                                    else:
                                        ERCTransaction.objects.create(target=user_num,status="Failed")
                            else:
                                    print("No recharge url available yet")
                        else:
                             print('No winner for akwa')

                        
                        if  recharge_play_levtwonum and str(recharge_play_levtwonum[0]) in winner_arr and level_credit_levtwo and level_credit_levtwo[0] == 'leveltwo':
                                user_num=MyUser.objects.get(username=recharge_levtwo_user[0])
                                high_score=ERCTransaction.objects.filter(time__gte=time_diff,target=user_num.username,phone_number=recharge_play_levtwonum[0]).count()
                                if high_score == 0:
                                    print(recharge_play_levtwonum)
                                    recharge='https://clients.primeairtime.com/api/topup/exec/%s/'%recharge_play_levtwonum[0]
                                    recharge_payload={"product_id": "MFIN-5-OR","denomination" :200,"send_sms" : True,"sms_text" : "Congratulations easy!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"}
                                else:
                                    print("Level two Winner can only win once in 5 days")
                                if recharge:
                                    response = c.post(recharge,data=recharge_payload,headers=second_get)
                                    print(recharge)
                                    print(response.text)
                                    retrieve=response.text
                                    get_data=json.loads(retrieve)
                                    if response.text and get_data['status'] == 201:
                                        ERCTransaction.objects.create(target=user_num.username,status=get_data['status'],
                                        product_id=get_data['product_id'],reference=get_data['reference'],phone_number=recharge_play_levtwonum[0],
                                        code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                                        paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                                    else:
                                        ERCTransaction.objects.create(target=user_num,status="Failed")
                                else:
                                    print("No recharge url available yet")
                        else:
                            print('level two is not yet ready')

                        if recharge_play_levthreenum and str(recharge_play_levthreenum[0]) in winner_arr and level_credit_levthree and level_credit_levthree[0] == 'levelthree':
                                user_num=MyUser.objects.get(username=recharge_levthree_user[0])
                                high_score=ERCTransaction.objects.filter(time__gte=time_diff,target=user_num.username,phone_number=recharge_play_levthreenum[0]).count()
                                if high_score == 0:
                                    print("levelthree%s"%recharge_play_levthreenum)
                                    recharge='https://clients.primeairtime.com/api/topup/exec/%s/'%recharge_play_levthreenum[0]
                                    recharge_payload={
                                # "message":"This is working"
                                    "product_id": "MFIN-5-OR",
                                    "denomination" :300,
                                    "send_sms" : True,
                                    "sms_text" : "Congratulations medium!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                                        }
                                else:
                                    print("Level three winner can only win once in 5 days")
                                if recharge:
                                    response = c.post(recharge,data=recharge_payload,headers=second_get)
                                    print(recharge)
                                    print(response.text)
                                    retrieve=response.text
                                    get_data=json.loads(retrieve)
                                    if response.text and get_data['status'] == 201:
                                        ERCTransaction.objects.create(target=user_num.username,status=get_data['status'],
                                        product_id=get_data['product_id'],reference=get_data['reference'],phone_number=recharge_play_levthreenum[0],
                                        code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                                        paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                                    else:
                                        ERCTransaction.objects.create(target=user_num,status="Failed")
                                else:
                                    print("No recharge url available yet")
                        else:
                            print('level three not yet ready')



                        if recharge_play_levfournum and str(recharge_play_levfournum[0]) in winner_arr and level_credit_levfour and level_credit_levfour[0] == 'levelfour':
                                user_num=MyUser.objects.get(username=recharge_levfour_user[0])
                                high_score=ERCTransaction.objects.filter(time__gte=time_diff,target=user_num.username,phone_number=recharge_play_levfournum[0]).count()
                                if high_score == 0:
                                    print("Hard %s"%recharge_play_levfournum)
                                    recharge='https://clients.primeairtime.com/api/topup/exec/%s/'%recharge_play_levfournum[0]
                                    recharge_payload={
                                # "message":"This is working"
                                    "product_id": "MFIN-5-OR",
                                    "denomination" :500,
                                    "send_sms" : True,
                                    "sms_text" : "Congratulations hard!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                                        }
                                else:
                                    print("Level four winner can only win once in 5 days")
                                if recharge:
                                    response = c.post(recharge,data=recharge_payload,headers=second_get)
                                    print(recharge)
                                    print(response.text)
                                    retrieve=response.text
                                    get_data=json.loads(retrieve)
                                    if response.text and get_data['status'] == 201:
                                        ERCTransaction.objects.create(target=user_num.username,status=get_data['status'],
                                        product_id=get_data['product_id'],reference=get_data['reference'],phone_number=recharge_play_levfournum[0],
                                        code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                                        paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                                    else:
                                        ERCTransaction.objects.create(target=user_num,status="Failed")
                                else:
                                    print("No recharge url available yet")
                        else:
                            print("Level four is not yet ready")
                        
            # else:
                #  print("Not Yet Time")               
        else:
            print("Not Yet time to credit this level")        #     )









@task(name="recharge_airtime")
def airtime():
    current_day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',]
    weekday = datetime.now().strftime('%A') 
    winner_arr=[]
    recharge_payload=[]
    recharge=''
    data={}
    easy_ran_num=[250,260,270,280,290,300]
    med_ran_num=[200,210,220,230,240,250]
    hard_ran_num=[230,240,250,260,270,280]
    easy_ran_choice=random.choice(easy_ran_num)
    med_ran_choice=random.choice(med_ran_num)
    hard_ran_choice=random.choice(hard_ran_num)
    time_diff = timezone.now() - timezone.timedelta(days=5)
    airtime_score_levfive=UserCorrectAnswer.objects.filter(difficulty='levelfive').order_by("-score","-timestamp")
    airtime_score_easy=UserCorrectAnswer.objects.filter(difficulty='easy').order_by("-score","-timestamp")
    airtime_score_medium=UserCorrectAnswer.objects.filter(difficulty='medium').order_by("-score","-timestamp")
    airtime_score_hard=UserCorrectAnswer.objects.filter(difficulty='hard').order_by("-score","-timestamp")
    airtime_score_xmas=UserCorrectAnswer.objects.filter(difficulty='xmas',winner=True).order_by("-score","-timestamp")
    level_credit_levfive=[recharge.difficulty for recharge in airtime_score_levfive][:1]
    level_credit_easy=[recharge.difficulty for recharge in airtime_score_easy][:1]
    level_credit_medium=[recharge.difficulty for recharge in airtime_score_medium][:1]
    level_credit_hard=[recharge.difficulty for recharge in airtime_score_hard][:1]
    level_credit_xmas=[recharge.difficulty for recharge in airtime_score_xmas][:1]
    # recharge=[recharge.score for recharge in airtime_score_easy][:1]
    recharge_player_easy=[winner_arr.append(str(air.phone_number)) for air in airtime_score_easy][:1]
    recharge_player_medium=[winner_arr.append(str(air.phone_number)) for air in airtime_score_medium][:1]
    recharge_player_hard=[winner_arr.append(str(air.phone_number)) for air in airtime_score_hard][:1]
    recharge_player_xmas=[winner_arr.append(str(air.phone_number)) for air in airtime_score_xmas][:1]
    recharge_player_levfive=[winner_arr.append(str(air.phone_number)) for air in airtime_score_levfive][:1]

    recharge_play_easynum=[str(air.phone_number) for air in airtime_score_easy][:1]
    recharge_play_mednum=[str(air.phone_number) for air in airtime_score_medium][:1]
    recharge_play_hardnum=[str(air.phone_number) for air in airtime_score_hard][:1]
    recharge_play_xmasnum=[str(air.phone_number) for air in airtime_score_xmas][:1]
    recharge_play_levfivenum=[str(air.phone_number) for air in airtime_score_levfive][:1]


    easy_score_guage=[bool(air.winner) for air in airtime_score_easy][:1]
    med_score_guage=[bool(air.winner)  for air in airtime_score_medium][:1]
    hard_score_guage=[ bool(air.winner) for air in airtime_score_hard][:1]
    xmas_score_guage=[ bool(air.winner) for air in airtime_score_xmas][:1]


    recharge_easy_user=[str(air.user) for air in airtime_score_easy][:1]
    recharge_med_user=[str(air.user) for air in airtime_score_medium][:1]
    recharge_hard_user=[str(air.user) for air in airtime_score_hard][:1]
    recharge_xmas_user=[str(air.user) for air in airtime_score_xmas][:1]
    recharge_levfive_user=[str(air.user) for air in airtime_score_levfive][:1]

    # print(str(recharge_play_easynum[0]),recharge_play_mednum,recharge_play_hardnum)
    # print(winner_arr)
    if winner_arr:
        # user_num=MyUser.objects.get(username=recharge_player_easy[0])
        
        now=datetime.now()
        now_time=now.time()
        if time(5,59) <= now.time() <= time(21,5) and weekday in current_day and easy_score_guage == True:
            username = str(settings.ERC_USER)
            password = (settings.ERC_PASS)
            url =  settings.ERC_LOGIN_URL #'https://clients.primeairtime.com/api/topup/status/'    #settings.ERC_LOGIN_URL
                # status = 'https://clients.primeairtime.com/api/topup/info/2347063419292/'
                    
                        
            login_payload={
            'action':'login',
            'username':username,
            'password':password
            }

            

            
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
            if recharge_play_xmasnum and str(recharge_play_xmasnum[0]) in winner_arr and level_credit_xmas and time(18,00) <= now.time() <= time(19,00) and level_credit_xmas[0] == 'xmas':
                            user_num=MyUser.objects.get(username=recharge_xmas_user[0])
                            high_score=ERCTransaction.objects.filter(time__gte=time_diff,phone_number=recharge_play_xmasnum[0]).count()
                            if high_score == 0:
                                recharge='https://clients.primeairtime.com/api/topup/exec/%s/'%recharge_play_xmasnum[0]
                                recharge_payload={"product_id": "MFIN-5-OR",
                                "denomination" :1000,
                                "send_sms" : True,
                                "sms_text" : "Congratulations!!! Your high score on FreeAirtime just earned you N1000! Keep on Tapping,spread the word!!!"}
                            elif high_score > 0:
                                    print("Xmas winner can only win once in 5 days")
                            else:
                                print("Xmas winner can only win once in 5 days")
                            if recharge:
                                    response = c.post(recharge,data=recharge_payload,headers=second_get)
                                    print(recharge)
                                    print(response.text)
                                    retrieve=response.text
                                    get_data=json.loads(retrieve)
                                    if response.text and get_data['status'] == 201:
                                        ERCTransaction.objects.create(target=user_num.username,status=get_data['status'],
                                        product_id=get_data['product_id'],reference=get_data['reference'],phone_number=recharge_play_levfivenum[0],
                                        code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                                        paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                                    else:
                                        ERCTransaction.objects.create(target=user_num,status="Failed")
                            else:
                                    print("No recharge url available yet")
            else:
                            print('No winner for xmas')
            # print("Its a boolean",type(easy_score_guage[0]))
            if time(9,00) <= now.time() <= time(9,2) or time(12,00) <= now.time() <= time(12,2) or time(15,00) <= now.time() <= time(15,9) or time(18,00) <= now.time() <= time(18,2) or time(21,00) <= now.time() <= time(21,2):
                
                    # print("My number %s"%user_num)
                    
                    username = str(settings.ERC_USER)
                    password = (settings.ERC_PASS)
                    url =  settings.ERC_LOGIN_URL #'https://clients.primeairtime.com/api/topup/status/'    #settings.ERC_LOGIN_URL
                # status = 'https://clients.primeairtime.com/api/topup/info/2347063419292/'
                    
                        
                    login_payload={
                    'action':'login',
                    'username':username,
                    'password':password
                    }

                   

                   
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
                        # print("My recharge load number is %s"%user_num)
                        if recharge_play_levfivenum and str(recharge_play_levfivenum[0]) in winner_arr and level_credit_levfive and level_credit_levfive[0] == 'levelfive':
                            user_num=MyUser.objects.get(username=recharge_levfive_user[0])
                            high_score=ERCTransaction.objects.filter(time__gte=time_diff,phone_number=recharge_play_levfivenum[0]).count()
                            if high_score == 0:
                                recharge='https://clients.primeairtime.com/api/topup/exec/%s/'%recharge_play_levfivenum[0]
                                recharge_payload={"product_id": "MFIN-5-OR",
                                "denomination" :1000,
                                "send_sms" : True,
                                "sms_text" : "Congratulations!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"}
                            elif high_score > 0:
                                    print("Levelfive winner can only win once in 5 days")
                            else:
                                print("Levelfive winner can only win twice a day")
                            if recharge:
                                    response = c.post(recharge,data=recharge_payload,headers=second_get)
                                    print(recharge)
                                    print(response.text)
                                    retrieve=response.text
                                    get_data=json.loads(retrieve)
                                    if response.text and get_data['status'] == 201:
                                        ERCTransaction.objects.create(target=user_num.username,status=get_data['status'],
                                        product_id=get_data['product_id'],reference=get_data['reference'],phone_number=recharge_play_levfivenum[0],
                                        code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                                        paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                                    else:
                                        ERCTransaction.objects.create(target=user_num,status="Failed")
                            else:
                                    print("No recharge url available yet")
                        else:
                            print('No winner for levelfive')



                        
                        if  recharge_play_easynum and easy_score_guage[0] == True and  str(recharge_play_easynum[0]) in winner_arr and level_credit_easy and level_credit_easy[0] == 'easy':
                                user_num=MyUser.objects.get(username=recharge_easy_user[0])
                                high_score=ERCTransaction.objects.filter(time__gte=time_diff,phone_number=recharge_play_easynum[0]).count()
                                if high_score == 0:
                                    data={'easy':recharge_play_easynum[0]}
                                    print(recharge_play_easynum)
                                    recharge='https://clients.primeairtime.com/api/topup/exec/%s/'%data['easy']   #recharge_play_easynum[0]
                                    recharge_payload={
                                    "product_id": "MFIN-5-OR",
                                    "denomination" :200,
                                    "send_sms" : True,
                                    "sms_text" : "Congratulations easy!!! Your high score on TapTap just earned you! Keep on Tapping,spread the word!!!"
                                    }
                                    del data['easy']
                                elif high_score > 0:
                                    print("Easy Winner can only win once in 5 days")
                                else:
                                    print('Easy Winner can only win once in 5 days')
                                
                                if recharge:
                                    recharge_times=0
                                    response = c.post(recharge,data=recharge_payload,headers=second_get)
                                    print(recharge)
                                    print(response.text)
                                    retrieve=response.text
                                    get_data=json.loads(retrieve)
                                    if response.text and get_data['status'] == 201 and recharge_times == 0:
                                        ERCTransaction.objects.create(target=user_num.username,status=get_data['status'],
                                        product_id=get_data['product_id'],reference=get_data['reference'],phone_number=recharge_play_easynum[0],
                                        code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                                        paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                                        recharge_times=1
                                    else:
                                        ERCTransaction.objects.create(target=user_num,status="Failed",phone_number=recharge_play_easynum[0])
                                else:
                                    print("No recharge url available yet")
                        else:
                            print('easy is not yet ready')

                        if recharge_play_mednum and med_score_guage == True and str(recharge_play_mednum[0]) in winner_arr and level_credit_medium and level_credit_medium[0] == 'medium':
                                user_num=MyUser.objects.get(username=recharge_med_user[0])
                                high_score=ERCTransaction.objects.filter(time__gte=time_diff,phone_number=recharge_play_mednum[0]).count()
                                print("medium%s"%high_score)
                                if high_score == 0:
                                    data={'medium':recharge_play_mednum[0]}
                                    print("medium%s"%recharge_play_mednum)
                                    recharge='https://clients.primeairtime.com/api/topup/exec/%s/'%data['medium']
                                    recharge_payload={
                                    # "message":"This is working"
                                    "product_id": "MFIN-5-OR",
                                    "denomination" :500,
                                    "send_sms" : True,
                                    "sms_text" : "Congratulations medium!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                                    }
                                    del data['medium']
                                elif high_score > 0:
                                    print("Medium winner can only win once in 5 days")
                                else:
                                    print("Medium winner can only win once in 5 days")
                                
                               
                                if recharge:
                                    recharge_times=0
                                    response = c.post(recharge,data=recharge_payload,headers=second_get)
                                    print(recharge)
                                    print(response.text)
                                    retrieve=response.text
                                    get_data=json.loads(retrieve)
                                    if response.text and get_data['status'] == 201 and recharge_times == 0:
                                        ERCTransaction.objects.create(target=user_num.username,status=get_data['status'],
                                        product_id=get_data['product_id'],reference=get_data['reference'],phone_number=recharge_play_mednum[0],
                                        code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                                        paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                                        recharge_times=1
                                    else:
                                        ERCTransaction.objects.create(target=user_num,status="Failed",phone_number=recharge_play_mednum[0])
                                else:
                                    print("No recharge url available yet")
                        else:
                            print('medium not yet ready')



                        if recharge_play_hardnum and hard_score_guage[0] == True and str(recharge_play_hardnum[0]) in winner_arr and level_credit_hard and level_credit_hard[0] == 'hard':
                                user_num=MyUser.objects.get(username=recharge_hard_user[0])
                                high_score=ERCTransaction.objects.filter(time__gte=time_diff,phone_number=recharge_play_hardnum[0]).count()
                                if high_score == 0:
                                    data={'hard':recharge_play_hardnum[0]}
                                    print("Hard %s"%recharge_play_hardnum)
                                    recharge='https://clients.primeairtime.com/api/topup/exec/%s/'%data['hard']
                                    recharge_payload={
                                # "message":"This is working"
                                    "product_id": "MFIN-5-OR",
                                    "denomination" :1000,
                                    "send_sms" : True,
                                    "sms_text" : "Congratulations hard!!! Your high score on TapTap just earned you N100! Keep on Tapping,spread the word!!!"
                                        }
                                    del data['hard']
                                elif high_score > 0:
                                    print("Hard winner can only win once in 5 days")
                                else:
                                    print("Hard winner can only win twice a day")
                                
                            
                                if recharge:
                                    recharge_times=0
                                    response = c.post(recharge,data=recharge_payload,headers=second_get)
                                    print(recharge)
                                    print(response.text)
                                    retrieve=response.text
                                    get_data=json.loads(retrieve)
                                    if response.text and get_data['status'] == 201 and recharge_times == 0:
                                        ERCTransaction.objects.create(target=user_num.username,status=get_data['status'],
                                        product_id=get_data['product_id'],reference=get_data['reference'],phone_number=recharge_play_hardnum[0],
                                        code=get_data['code'],time=['time'],paid_amount=get_data['paid_amount'],
                                        paid_currency=get_data['paid_currency'],topup_amount=get_data['topup_amount'],topup_currency=get_data['topup_currency'],country=get_data['country'],operator_name=get_data['operator_name'])
                                        recharge_times=1
                                    else:
                                        ERCTransaction.objects.create(target=user_num,status="Failed",phone_number=recharge_play_hardnum[0])
                                else:
                                    print("No recharge url available yet")
                        else:
                            print("Hard is not yet ready")
                        
            else:
                 print("Not Yet Time")  
                              
        else:
            print("You can only be credited Once")        #     )
        print(data)
    # target,status,product_id,reference,code,paid_amount,paid_currency,topup_amount,topup_currency,time,country,operator_name
        # if tap[0]:
        #     print("{} Your Phone Number {} Has Just Been Credited With The Highest Score of {}".format(user_num,user_num.phone_number,tap[0]))
