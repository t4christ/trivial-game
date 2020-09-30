from django.test import TestCase
from taptap.models import Taptap
from django.utils import timezone
from django.urls import reverse
from accounts.models import MyUser
from taptap.views import tap_score

# models test
class TaptapTest(TestCase):

    def create_taptap(self,score="400"):
            user=MyUser(username='temitayo',password='texplode',phone_number='07063419292',first_name='akanbi',last_name='bakare',email='bakakan@gmail.com')
            return Taptap(player=user, score=score, timestamp=timezone.now())

    def test_taptap_creation(self):
        w = self.create_taptap()
        self.assertTrue(isinstance(w, Taptap))
        self.assertEqual(w.__str__(), 'Score for %s'%w.player)

class TaptapListViewTest(TestCase):

    @classmethod
    def setUpTestViewData(cls):
        create_taptap()
        number_of_taps = 15
        for tap_num in range(number_of_taps):
            Taptap.objects.create(player=create_taptap(), score=score, timestamp=timezone.now())
           
    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/play_tap_tap/understand/') 
        self.assertEqual(resp.status_code, 200)  
           
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('taptap:understand_tap'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('taptap:understand_tap'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'taptap/understand.html')

