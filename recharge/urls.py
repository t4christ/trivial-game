from django.conf.urls import url
from django.contrib import admin

from .views import (
	recharge,
    statistics,
    # level_based,
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
	# post_create,
	# post_detail,
	# post_update,
	# post_delete,
	)

app_name="recharge"

urlpatterns = [
	url(r'^$', recharge,name='recharge'),
###### High Score Based ##########
     url(r'^invite/$',send_invite, name='invite'),
     url(r'^bonus/$',add_bonus, name='bonus'),
	# url(r'^hard/(?P<username>[-\w]+)/$', hard, name='hard'),
    # url(r'^medium/(?P<username>[-\w]+)/$', medium, name='medium'),\
    url(r'^generate_excel/$', download_excel_data, name='get_excel'),
     url(r'^generate_winners/$', download_exce_data, name='get_winners'),
    url(r'^stats_excel/$', statistics_excel, name='get_stats_excel'),
    url(r'^recharge/easy_submit/(?P<username>[-\w]+)/$', easy_submit, name='easy_submit'),
    url(r'^recharge/easy/(?P<username>[-\w]+)/$', quiz, name='easy'),
    url(r'^recharge/medium/(?P<username>[-\w]+)/$', quiz, name='medium'),
    url(r'^recharge/hard/(?P<username>[-\w]+)/$', quiz, name='hard'),
    url(r'^recharge/xmas/(?P<username>[-\w]+)/$', quiz, name='xmas'),
   
    url(r'^qloads/$',load_question, name='load_question'),
    # url(r'^dload/$', del_question, name='del_question'),
    url(r'^qload/$', get_winners, name='load_question'),
    url(r'^statistics/$', statistics, name='statistics'),




###### Level Based ##########
    url(r'^recharge/level1/(?P<username>[-\w]+)/$', quiz, name='level1'),
    url(r'^recharge/level2/(?P<username>[-\w]+)/$', quiz, name='level2'),
    url(r'^recharge/level3/(?P<username>[-\w]+)/$', quiz, name='level3'),
    url(r'^recharge/level4/(?P<username>[-\w]+)/$', quiz, name='level4'),
    url(r'^recharge/level5/(?P<username>[-\w]+)/$', quiz, name='level5'),
    

############################ JAMB URL ################################
    url(r'^jamb/account/(?P<username>[-\w]+)/$', quiz, name='jacct'),
    url(r'^jamb/geography/(?P<username>[-\w]+)/$', quiz, name='jgeo'),
    url(r'^jamb/biology/(?P<username>[-\w]+)/$', quiz, name='jbio'),
    url(r'^jamb/physics/(?P<username>[-\w]+)/$', quiz, name='jphy'),
    url(r'^jamb/chemistry/(?P<username>[-\w]+)/$', quiz, name='jchem'),
    url(r'^jamb/commerce/(?P<username>[-\w]+)/$', quiz, name='jcomm'),
    url(r'^jamb/ict/(?P<username>[-\w]+)/$', quiz, name='jict'),
    url(r'^jamb/crk/(?P<username>[-\w]+)/$', quiz, name='jcrk'),
    url(r'^jamb/literature/(?P<username>[-\w]+)/$', quiz, name='jlit'),
    url(r'^jamb/economics/(?P<username>[-\w]+)/$', quiz, name='jeco'),
    url(r'^jamb/government/(?P<username>[-\w]+)/$', quiz, name='jgov'),
    url(r'^jamb/english/(?P<username>[-\w]+)/$', quiz, name='jeng'),
    url(r'^jamb/mathematics/(?P<username>[-\w]+)/$', quiz, name='jmath'),

	
]
