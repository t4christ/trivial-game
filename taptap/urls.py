from django.urls import path
from django.contrib import admin

from .views import tap_score,welcome_tap,understand_tap,send_invite,add_bonus

app_name="taptap"

urlpatterns = [
    path('invite/',send_invite, name='invite'),
    path('bonus/',add_bonus, name='bonus'),
    path('play/<str:username>/',welcome_tap, name='welcome_tap'),
	path('tap_and_tap/<str:username>/',tap_score, name='tap_tap'),
    path('understand/',understand_tap, name='understand_tap'),
    
    
]
