from  django.test import SimpleTestCase
from  django.urls import reverse,resolve
from  download.views import demo,tt

class TestUrl(SimpleTestCase):
    
    def test_url(self):
        url = reverse('test')
        self.assertEqual(resolve(url).func,tt)
        
    