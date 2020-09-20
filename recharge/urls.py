from django.urls import path
from django.contrib import admin

from .views import (
	recharge,
    statistics,
    UploadQuestion,
    quiz,
    easy_submit,
    download_excel_data,
    download_exce_data,
    statistics_excel,
    send_invite,
    add_bonus,
    get_winners,
    del_question,
    load_question,
    time_lapse
	# post_create,
	# post_detail,
	# post_update,
	# post_delete,
	)

app_name="recharge"

urlpatterns = [
	path('', recharge,name='recharge'),
###### High Score Based ##########
     path('invite/',send_invite, name='invite'),
     path('bonus/',add_bonus, name='bonus'),
	path('upload_question/', UploadQuestion, name='upload_question'),
    # path('medium/<str:username>/', medium, name='medium'),\
    path('generate_excel/', download_excel_data, name='get_excel'),
     path('generate_winners/', download_exce_data, name='get_winners'),
    path('stats_excel/', statistics_excel, name='get_stats_excel'),
    path('recharge/easy_submit/<str:username>/', easy_submit, name='easy_submit'),
    path('recharge/time_lapse/<str:username>/', time_lapse, name='time_lapse'),
    path('recharge/easy/<str:username>/', quiz, name='easy'),
    path('recharge/medium/<str:username>/', quiz, name='medium'),
    path('recharge/hard/<str:username>/', quiz, name='hard'),
    path('recharge/akwa/<str:username>/', quiz, name='akwa'),
    path('recharge/xmas/<str:username>/', quiz, name='xmas'),
   
    path('qloads/',load_question, name='load_question'),
    # path('dload/', del_question, name='del_question'),
    path('qload/', get_winners, name='load_question'),
    path('statistics/', statistics, name='statistics'),




###### Level Based ##########
    path('recharge/level1/<str:username>/', quiz, name='level1'),
    path('recharge/level2/<str:username>/', quiz, name='level2'),
    path('recharge/level3/<str:username>/', quiz, name='level3'),
    path('recharge/level4/<str:username>/', quiz, name='level4'),
    path('recharge/level5/<str:username>/', quiz, name='level5'),
    

############################ JAMB path ################################
    path('jamb/account/<str:username>/', quiz, name='jacct'),
    path('jamb/geography/<str:username>/', quiz, name='jgeo'),
    path('jamb/biology/<str:username>/', quiz, name='jbio'),
    path('jamb/physics/<str:username>/', quiz, name='jphy'),
    path('jamb/chemistry/<str:username>/', quiz, name='jchem'),
    path('jamb/commerce/<str:username>/', quiz, name='jcomm'),
    path('jamb/ict/<str:username>/', quiz, name='jict'),
    path('jamb/crk/<str:username>/', quiz, name='jcrk'),
    path('jamb/literature/<str:username>/', quiz, name='jlit'),
    path('jamb/economics/<str:username>/', quiz, name='jeco'),
    path('jamb/government/<str:username>/', quiz, name='jgov'),
    path('jamb/english/<str:username>/', quiz, name='jeng'),
    path('jamb/mathematics/<str:username>/', quiz, name='jmath'),

	
]
