# from django.db.models import Count
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime,time
import random
from erc.models import ERCTransaction
from django.conf import settings
from accounts.models import MyUser
from django.http import JsonResponse
from django.contrib import messages
from django.db.models.aggregates import Max
from django.core import serializers
from django.utils import timezone
from utils.smsclient import SmsClient
# from posts.models import Messaging
sms_client = SmsClient()

# from django.views.decorators.csrf import csrf_exempt



 # Hours must be 24 hour clock times 
def is_weekday_and_time_in_range(date):
    return date.weekday() < 6 






import uuid
def gen_ran():
	return str(uuid.uuid4())

def add_bonus(request):
		invite = request.POST.get('bonus')
		loyalty = request.POST.get('loyalty')
		r_bonus=None
		h_bonus=None
		sum_bonus=None
		print("Am current bonus",invite)
		data=dict()
		time_diff = timezone.now() - timezone.timedelta(hours=1)
		if request.method == 'POST':
			if invite and int(invite) > 0:

				try:
					my_score=[]
					invite=int(invite)

					get_score=Taptap.objects.filter(player=request.user,timestamp__gte=time_diff).order_by("-score")[:1]
										
					for get in get_score:
						my_score.append(get.score)
					
					if invite > 100:
						h_bonus=invite - 100
						sum_bonus=100 + my_score[0]
						del my_score[:]
					else:
						h_bonus=0
						sum_bonus = invite + my_score[0]
					
						del my_score[:]
				

					print("My Score",sum_bonus,h_bonus,r_bonus)
					tap_score=Taptap.objects.filter(player=request.user,timestamp__gte=time_diff).order_by("-score")[:1]
					for tap in tap_score:
						tap.score = sum_bonus
						tap.save()
						
						
						bonus=BonusPoint.objects.get(player=request.user)
						bonus.bonus_points=h_bonus
						r_bonus=h_bonus
						bonus.save()
						
						data['bonus_added']=bonus.bonus_points
						data["bonus_left"]=r_bonus
						data['tapscore_added']="Your tap score is now{}".format(tap.score)
						return JsonResponse(data)
					for tap_score in tap_score:
						data['tapscore_added']="Your tap score is now{}".format(tap_score.score)
				except BonusPoint.DoesNotExist:
					data['bonus_error']="Sorry You Don't Have Any Bonus or Tap Score At The Moment"	 
					return JsonResponse(data)


			elif int(loyalty) > 0:

					try:
						my_score=[]
						loyalty=int(loyalty)

						get_score=Taptap.objects.filter(player=request.user,timestamp__gte=time_diff).order_by("-score")[:1]
											
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
						tap_score=Taptap.objects.filter(player=request.user,timestamp__gte=time_diff).order_by("-score")[:1]
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
	text_message="Your Friend %s,has invited you to play TapTAP & stand a chance to earn free airtime! Click gist.wstreams.com/ to play (No data charges)"%request.user.get_full_name
	bonus_update=[]
	if request.method == 'POST':
		# print(invite)
		try: 	
				bonus= BonusPoint.objects.get(player=request.user)
				print(bonus.list_numbers)
				for inv in invite:
					if not inv in bonus.list_numbers:
						res=sms_client.send(to=invite, text=text_message)
						bonus_update.append(inv)
						invite_len=len(bonus_update)
						bonus_ps = 5 * invite_len
						bonus.bonus_points+=bonus_ps
						bonus.list_numbers=bonus.list_numbers+str(","+inv)
						bonus.save()
						
						del bonus_update[:]
						data['sent']="You Have Successfully sent the sms"
						print("This is the lenght",len(invite_arr))
					else:
						print("It is present")
						data['onlyOnce']="You already invited this person"
		except BonusPoint.DoesNotExist:
			BonusPoint.objects.create(player=request.user,bonus_points=bonus_points,list_numbers=invite)

		
		# print(res)
	# data["Sorry"]="You Have Exceeded Your Limit"
		return JsonResponse(data)
	else:
		data['Post']="This is not a post request"
		return JsonResponse(data)
	


@login_required
def welcome_tap(request,username):
	# message=Messaging.objects.filter(receiver=request.user.username,deleted=False)
	# inbox=message.count()
	now=datetime.now()
	now_time=now.time()
	winner=ERCTransaction.objects.all()[:10]
	bonus=None
	loyalty=None
	# if time(10,59)<=now.time() <= time(11,3):
	# 	print("This is the time")
	# else:
	# 	print("This time %s"%now.time())
	if not request.user.is_authenticated:
		return redirect("/register")
	user=get_object_or_404(MyUser,username=username)
	tap_score=Taptap.objects.all().order_by("-score")[:1]
	try:
		bonus=BonusPoint.objects.get(player=request.user)
		loyalty=MyUser.objects.get(username=request.user.username)
	except BonusPoint.DoesNotExist or MyUser.DoesNotExist:
		pass
	time_diff = timezone.now() - timezone.timedelta(hours=1)
	weekday = datetime.now().strftime('%A') 
	current_day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
	tap_user = Taptap.objects.filter(player=request.user,timestamp__gte=time_diff).order_by("-score")[:1]
	num_played=Taptap.objects.filter(player=request.user,timestamp__gte=time_diff).count()
	count_player=TapActivePlayer.objects.filter(player_tap=request.user).count()
	if count_player < 5:
		TapActivePlayer.objects.create(player_tap=request.user,player_num=+1)
	# 	hr = datetime.now()
	# 	hr_time=hr.second
	# 	for count in count_player:
	# 		count.player_num+=1
	# 		count.save()
			
	elif not count_player: 
	# 	created=datetime.now()
	# 	create=created.second
	 	TapActivePlayer.objects.create(player_tap=request.user,player_num=+1)
	# 	print(hr_time - create)
	try:
		if  request.session and request.user.is_authenticated:
			# tap_time=now.hour
			# tap_time=now.strftime("%Y-%m-%d %H:%M")
			tap_time=now.strftime("%H:%M:%S")
			# time=['9:00:00','12:00:00','15:00:00','18:00:00','00:00:00']
			
			
			if num_played < 20:
				play_left=20 - num_played
				if weekday not in current_day:
					messages.error(request,"This Game is only opened from Mondays to Saturdays")
					return redirect("/")
				if not time(1,00) <= now_time <= time(23,59):
					messages.error(request,"This Game is only opened from 6 a.m to 12 midnight")
					return redirect("/")
				tap_score=Taptap.objects.all().order_by("-score")[:1]
				context={"winner":winner,"tap_score":tap_score,"bonus_point":bonus,"loyalty":loyalty}
				messages.success(request,"Welcome Let the Game Begin. You have %s times left to play"%play_left)
				return render(request,"taptap/welcome.html",context)
			else:
				messages.error(request,"You Have Played Your Limit For The 3 Hour Slot.")
				return redirect("/")
		else:
			return redirect('taptap:understand_tap')
	except Exception as e:
		print("Error message",e)
		return HttpResponse("Error message",e)


def understand_tap(request):
	user=Taptap.objects.filter(understand=True)
	# message=Messaging.objects.filter(receiver=request.user.username,deleted=False)
	# inbox=message.count()
	context={}
	request.session['understand']=True
	if request.user.is_authenticated:
		# del request.session['understand']
		return redirect("taptap:welcome_tap",username=request.user)
	else:
		return render(request,"taptap/understand.html")	
	

import json
@login_required
def tap_score(request,username):
	user=get_object_or_404(MyUser,username=username)
	score = request.POST.get('total_sc',None)
	print("My body",request.body)
	
	tap_score=Taptap.objects.all()
	data=dict()
	time_start = request.POST.get('time_start',)
	print("My time started{}".format(time_start))
	if time_start:
            import time,math
            start_timer = time.time()
            request.session["get-timer"]=start_timer
            # print(start_timer)
	start_timer=0
	time_differ=0
	time_diff_arr=[60,61,62,63,64,65]
	time_start = request.POST.get('time_start',)
	if time_start:
            import time,math
            start_timer = time.time()
            request.session["get-timer"]=start_timer
	time_end = request.POST.get("end_time",)
	if time_end:
		import time,math
		end_timer=time.time()
		time_differ = math.floor(end_timer - request.session["get-timer"])
		# print("Here is the time ",time_differ)
		if time_differ not in time_diff_arr:
			data['busted']= "Hey! I can see You Cheating Backoff. You Spent %s Seconds On The Questions"%time_differ
	high_score=Taptap.objects.filter(understand=True)\
                                .annotate(max_value=Max('score')) \
                                .order_by('-max_value')
	
	score_count=[high_score for high_score in tap_score][:1]
	tap_score_count=[tap_score.score for tap_score in tap_score]
	data=dict()
	# now=datetime.datetime.now()
	# data['time_for']=now
	number=random.randint(-101,101)
	if request.method == "GET":
		# data["high_score"]=tap_score_count
		now=datetime.datetime.now()
		
		# tap_time=now.hour
		# tap_time=now.strftime("%Y-%m-%d %H:%M")
		tap_time=now.strftime("%H:%M:%S")
		time=['9:00:00','12:00:00','15:00:00','18:00:00','00:00:00']
		for time in time:
			data['time']=time
			print(data)
		print (tap_time)
		if tap_time in time:
			print(now)
		else:
			print("Not Yet Time")
		# for x in range(10):
		number=random.randint(-101,101)
		print(number)
		return JsonResponse(data)

	elif request.method == 'POST' and score is not None:
		
		print("Where my score at {}".format(score))
		# print(score)
		now=datetime.now()
		time=[9,12,15,18]
		num_played=Taptap.objects.filter(player=request.user).count()
		if int(score) > 0:
			print("Where my score at {}".format(score))
			Taptap.objects.get_or_create(player=request.user,score=score,understand=True)
			data["thanks"]="Thanks For playing See You Next Time" 
			
			# instance.user = request.user
			# instance.save()
		# message success
	else:
		data["Sorry"]="You Have Exceeded Your Limit" 
		return JsonResponse(data)

	return JsonResponse(data)



def get_winners(request):
    high_score = TapHighestScore.objects.all()
    # play_stat=PlayerStatistic.objects.all()
    for winner in high_score:
        user_num=MyUser.objects.get(username=winner.player)
        TapHighestScore.objects.filter(player__username=user_num.username).update(phone_number=user_num.phone_number)