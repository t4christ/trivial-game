from django.db import models
from accounts.models import MyUser
# Create your models here.

class QuestionDetail(models.Model):
    poster = models.CharField(max_length=150)
    question_name= models.CharField(max_length=100)
    # duration_min = models.PositiveIntegerField(default=0)
    # level = models.CharField(max_length=10,default=100)
    publish_status = models.BooleanField(default=False)
    
    @property
    def get_question_name(self):
        return self.question_name
    
    def __str__(self):
        return "{} question".format(self.question_name)

class EasyQuestion(models.Model):
    poster = models.CharField(max_length=50,default='')
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="easy_question_detail")
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)


class MediumQuestion(models.Model):
    poster = models.CharField(max_length=50,default='') 
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="medium_question_detail")
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)




class HardQuestion(models.Model):
    poster = models.CharField(max_length=50,default='') 
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="hard_question_detail")
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)


class LevelOneQuestion(models.Model):
    poster = models.CharField(max_length=50,default='') 
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="levelone_question_detail")
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)

class LevelTwoQuestion(models.Model):
    poster = models.CharField(max_length=50,default='') 
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="leveltwo_question_detail")
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)


class LevelThreeQuestion(models.Model):
    poster = models.CharField(max_length=50,default='')
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="levelthree_question_detail")
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)


class LevelFourQuestion(models.Model):
    poster = models.CharField(max_length=50,default='') 
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="levelfour_question_detail")
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)



class LevelFiveQuestion(models.Model):
    poster = models.CharField(max_length=50,default='') 
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="levelfive_question_detail")
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)

class AkwaIbomQuestion(models.Model):
    poster = models.CharField(max_length=50,default='') 
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="akwaibom_question_detail")
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)


class NigeriaAnniversaryQuestion(models.Model):
    poster = models.CharField(max_length=50,default='') 
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="nigeria_anniversary_question_detail")
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)


class TempAnswer(models.Model):
    answers = models.TextField()
    question_name = models.CharField(max_length=50)
    username = models.ForeignKey(MyUser,on_delete=models.CASCADE, related_name="temp_ans",default="")
    def __str__(self):
        return "Answers for {}".format(self.question_name)

class EasyAnswer(models.Model):
    questions = models.ForeignKey(EasyQuestion,on_delete=models.CASCADE,related_name="easy_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=500)
    # class Meta:
    #     unique= "questions"
            # no duplicated content per question
            
    def __str__(self):
        return "{}".format(self.correct_answer)


class MediumAnswer(models.Model):
    questions = models.ForeignKey(MediumQuestion, on_delete=models.CASCADE,related_name="medium_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)


class HardAnswer(models.Model):
    questions = models.ForeignKey(HardQuestion, on_delete=models.CASCADE,related_name="hard_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)




class LevelOneAnswer(models.Model):
    questions = models.ForeignKey(LevelOneQuestion, on_delete=models.CASCADE,related_name="levelone_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)





class LevelTwoAnswer(models.Model):
    questions = models.ForeignKey(LevelTwoQuestion, on_delete=models.CASCADE,related_name="leveltwo_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)



class LevelThreeAnswer(models.Model):
    questions = models.ForeignKey(LevelThreeQuestion, on_delete=models.CASCADE,related_name="levelthree_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)



class LevelFourAnswer(models.Model):
    questions = models.ForeignKey(LevelFourQuestion, on_delete=models.CASCADE,related_name="levelfour_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)



class LevelFiveAnswer(models.Model):
    questions = models.ForeignKey(LevelFiveQuestion, on_delete=models.CASCADE,related_name="levelfive_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)




class AkwaIbomAnswer(models.Model):
    questions = models.ForeignKey(AkwaIbomQuestion, on_delete=models.CASCADE,related_name="akwaibom_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)


class NigeriaAnniversaryAnswer(models.Model):
    questions = models.ForeignKey(NigeriaAnniversaryQuestion, on_delete=models.CASCADE,related_name="nigeria_anniversary_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)

class UserCorrectAnswer(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name="user_answer")
    phone_number=models.CharField(max_length=13,default="")
    difficulty=models.CharField(max_length=10)
    winner=models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return "{} Correct Question and Answer".format(self.user)




class PlayerStatistic(models.Model):
    player = models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name="user_stats")
    difficulty=models.CharField(max_length=10)
    phone_number=models.CharField(max_length=15,default='',null=True,blank=True)
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return "{} Player".format(self.player)


class HighestScoreStatistic(models.Model):
    user = models.ForeignKey(MyUser,default="", on_delete=models.CASCADE,related_name="highest_score")
    difficulty=models.CharField(max_length=10)
    score = models.IntegerField(default=0)
    winner=models.BooleanField(default=False)
    phone_number=models.CharField(max_length=15,default='',null=True,blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return "{} Correct Question with phonenumber {} and Answer on {}".format(self.user,self.phone_number,self.timestamp) 


class HighestLevelScore(models.Model):
    player = models.ForeignKey(MyUser,default="", on_delete=models.CASCADE,related_name="highest_level_score")
    difficulty=models.CharField(max_length=10)
    score = models.IntegerField(default=0)
    phone_number=models.CharField(max_length=13)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return "{} Completed".format(self.difficulty) 



class ActivePlayer(models.Model):
    player_num = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return "{} Players".format(self.player_num)

class BonusPointAirtime(models.Model):
    player = models.CharField(max_length=100,default="")
    list_numbers =  models.TextField(default="") # models.TimeField(null=True, blank=True) #assume minutes
    bonus_points=models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return "Bonus point for {} is {}".format(self.player,self.bonus_points)



######################### JAMB Practice Questions and Answers #####################################

class JAccountQuestion(models.Model):
    poster = models.CharField(max_length=50,default='') 
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="jaccount")
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)

class JGeoQuestion(models.Model):
    poster = models.CharField(max_length=50,default='')
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="jgeo") 
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)


class JBioQuestion(models.Model):
    poster = models.CharField(max_length=50,default='')
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="jbio") 
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)



class JPhysicsQuestion(models.Model):
    poster = models.CharField(max_length=50,default='')
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="jphysics") 
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)



class JChemistryQuestion(models.Model):
    poster = models.CharField(max_length=50,default='')
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="jchemistry") 
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)



class JCommerceQuestion(models.Model):
    poster = models.CharField(max_length=50,default='')
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="jcommerce") 
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)



class JIctQuestion(models.Model):
    poster = models.CharField(max_length=50,default='') 
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="jict") 
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)



class JCrkQuestion(models.Model):
    poster = models.CharField(max_length=50,default='')
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="jcrk") 
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)



class JLiteratureQuestion(models.Model):
    poster = models.CharField(max_length=50,default='')
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="jliterature") 
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)



class JEconomicsQuestion(models.Model):
    poster = models.CharField(max_length=50,default='') 
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="jeconomics") 
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)


class JGovQuestion(models.Model):
    poster = models.CharField(max_length=50,default='')
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="jgov") 
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)

class JEngQuestion(models.Model):
    poster = models.CharField(max_length=50,default='')
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="jeng")  
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)


class JMathQuestion(models.Model):
    poster = models.CharField(max_length=50,default='')
    question_detail = models.ForeignKey(QuestionDetail, on_delete=models.CASCADE,default='',related_name="jmath") 
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)

####################### JAMB Answer#########################

class JAccountAnswer(models.Model):
    questions = models.ForeignKey(JAccountQuestion, on_delete=models.CASCADE,related_name="jacct_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    choice5 = models.CharField(max_length=500,default='')
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4","choice5"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)



class JGeoAnswer(models.Model):
    questions = models.ForeignKey(JGeoQuestion, on_delete=models.CASCADE,related_name="jgeo_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    choice5 = models.CharField(max_length=500,default='')
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4","choice5"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)

class JBioAnswer(models.Model):
    questions = models.ForeignKey(JBioQuestion, on_delete=models.CASCADE,related_name="jbio_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    choice5 = models.CharField(max_length=500,default='')
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4","choice5"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)



class JPhysicsAnswer(models.Model):
    questions = models.ForeignKey(JPhysicsQuestion, on_delete=models.CASCADE,related_name="jphy_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    choice5 = models.CharField(max_length=500,default='')
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4","choice5"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)


class JChemistryAnswer(models.Model):
    questions = models.ForeignKey(JChemistryQuestion, on_delete=models.CASCADE,related_name="jchem_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    choice5 = models.CharField(max_length=500,default='')
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4","choice5"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)



class JCommerceAnswer(models.Model):
    questions = models.ForeignKey(JCommerceQuestion, on_delete=models.CASCADE,related_name="jcmm_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    choice5 = models.CharField(max_length=500,default='')
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4","choice5"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)



class JIctAnswer(models.Model):
    questions = models.ForeignKey(JIctQuestion, on_delete=models.CASCADE,related_name="jict_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    choice5 = models.CharField(max_length=500,default='')
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4","choice5"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)


class JCrkAnswer(models.Model):
    questions = models.ForeignKey(JCrkQuestion, on_delete=models.CASCADE,related_name="jcrk_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    choice5 = models.CharField(max_length=500,default='')
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4","choice5"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)


class JLiteratureAnswer(models.Model):
    questions = models.ForeignKey(JLiteratureQuestion, on_delete=models.CASCADE,related_name="jlit_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    choice5 = models.CharField(max_length=500,default='')
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4","choice5"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)


class JEconomicsAnswer(models.Model):
    questions = models.ForeignKey(JEconomicsQuestion, on_delete=models.CASCADE,related_name="jeco_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    choice5 = models.CharField(max_length=500,default='')
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4","choice5"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)


class JGovAnswer(models.Model):
    questions = models.ForeignKey(JGovQuestion, on_delete=models.CASCADE,related_name="jgov_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    choice5 = models.CharField(max_length=500,default='')
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4","choice5"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)

class JEngAnswer(models.Model):
    questions = models.ForeignKey(JEngQuestion, on_delete=models.CASCADE,related_name="jeng_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    choice5 = models.CharField(max_length=500,default='')
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4","choice5"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)

class JMathAnswer(models.Model):
    questions = models.ForeignKey(JMathQuestion, on_delete=models.CASCADE,related_name="jmath_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    choice5 = models.CharField(max_length=500,default='')
    correct_answer = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [
            # no duplicated content per question
            ("questions","choice1","choice2","choice3","choice4","choice5"),  
        ]
    def __str__(self):
        return "{}".format(self.correct_answer)