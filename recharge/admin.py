from django.contrib import admin

# Register your models here.
from .models import *

class EasyQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]

	
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = EasyQuestion



class QuestionDetailModelAdmin(admin.ModelAdmin):
	list_display = ["question_name", "publish_status"]
	list_display_links = ["question_name"]
	# list_editable = ["content"]

	
	list_filter = ["question_name", "publish_status"]

	search_fields = ["question_name", "publish_status"]
	class Meta:
		model = QuestionDetail


class MediumQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = MediumQuestion



class HardQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = HardQuestion


class LevelOneQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = LevelOneQuestion



class LevelTwoQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = LevelTwoQuestion




class LevelThreeQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = LevelThreeQuestion




class LevelFourQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = LevelFourQuestion


class LevelFiveQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = LevelFiveQuestion

class AkwaIbomQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = AkwaIbomQuestion






class HighestScoreModelAdmin(admin.ModelAdmin):
	list_display = ["phone_number", "timestamp"]
	# list_display_links = ["content"]
	# list_editable = ["content"]
	# list_filter = ["content","timestamp"]

	search_fields = ["phone_number"]
	class Meta:
		model = HighestScoreStatistic


###################### JAMB Model Admin ########################

class JAccountQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = JAccountQuestion


class JGeoQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = JGeoQuestion


class JBioQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = JBioQuestion

class JPhysicsQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = JPhysicsQuestion

class JChemistryQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = JChemistryQuestion


class JCommerceQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = JCommerceQuestion

class JIctQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = JIctQuestion

class JCrkQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = JCrkQuestion

class JLiteratureQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = JLiteratureQuestion

class JEconomicsQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = JEconomicsQuestion


class JGovQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = JGovQuestion


class JMathQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = JMathQuestion


class JEngQuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content", "timestamp"]
	list_display_links = ["content"]
	# list_editable = ["content"]
	list_filter = ["content","timestamp"]

	search_fields = ["content","poster"]
	class Meta:
		model = JEngQuestion

# Bonus Points
admin.site.register(BonusPointAirtime)







# High Score Based
admin.site.register(EasyQuestion, EasyQuestionModelAdmin)
admin.site.register(QuestionDetail, QuestionDetailModelAdmin)
admin.site.register(MediumQuestion, MediumQuestionModelAdmin)
admin.site.register(HardQuestion, HardQuestionModelAdmin)
admin.site.register(EasyAnswer)
admin.site.register(MediumAnswer)
admin.site.register(HardAnswer)

# Level Based
admin.site.register(LevelOneQuestion, LevelOneQuestionModelAdmin)
admin.site.register(LevelTwoQuestion, LevelTwoQuestionModelAdmin)
admin.site.register(LevelThreeQuestion, LevelThreeQuestionModelAdmin)
admin.site.register(LevelFourQuestion, LevelFourQuestionModelAdmin)
admin.site.register(LevelFiveQuestion, LevelFiveQuestionModelAdmin)
admin.site.register(AkwaIbomQuestion, AkwaIbomQuestionModelAdmin)
admin.site.register(LevelOneAnswer)
admin.site.register(LevelTwoAnswer)
admin.site.register(LevelThreeAnswer)
admin.site.register(LevelFourAnswer)
admin.site.register(LevelFiveAnswer)
admin.site.register(AkwaIbomAnswer)
admin.site.register(UserCorrectAnswer)
admin.site.register(HighestScoreStatistic,HighestScoreModelAdmin)
admin.site.register(PlayerStatistic)
admin.site.register(ActivePlayer)
admin.site.register(HighestLevelScore)



################## JAMB Register Admin #####################
admin.site.register(JAccountQuestion, JAccountQuestionModelAdmin)
admin.site.register(JAccountAnswer)

admin.site.register(JGeoQuestion, JGeoQuestionModelAdmin)
admin.site.register(JGeoAnswer)

admin.site.register(JBioQuestion, JBioQuestionModelAdmin)
admin.site.register(JBioAnswer)

admin.site.register(JPhysicsQuestion, JPhysicsQuestionModelAdmin)
admin.site.register(JPhysicsAnswer)


admin.site.register(JChemistryQuestion, JChemistryQuestionModelAdmin)
admin.site.register(JChemistryAnswer)

admin.site.register(JCommerceQuestion, JCommerceQuestionModelAdmin)
admin.site.register(JCommerceAnswer)


admin.site.register(JIctQuestion, JIctQuestionModelAdmin)
admin.site.register(JIctAnswer)

admin.site.register(JCrkQuestion, JCrkQuestionModelAdmin)
admin.site.register(JCrkAnswer)

admin.site.register(JLiteratureQuestion, JLiteratureQuestionModelAdmin)
admin.site.register(JLiteratureAnswer)

admin.site.register(JEconomicsQuestion, JEconomicsQuestionModelAdmin)
admin.site.register(JEconomicsAnswer)

admin.site.register(JGovQuestion, JGovQuestionModelAdmin)
admin.site.register(JGovAnswer)

admin.site.register(JEngQuestion, JEngQuestionModelAdmin)
admin.site.register(JEngAnswer)


admin.site.register(JMathQuestion, JMathQuestionModelAdmin)
admin.site.register(JMathAnswer)