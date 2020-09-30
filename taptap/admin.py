from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Taptap)
admin.site.register(BonusPoint)
admin.site.register(TapHighestScore)
admin.site.register(TapActivePlayer)