from django.test import TestCase, Client

from counter.models import Counter
from counter import views 

# Create your tests here.
class CounterTest(TestCase):

    def test_first(self):
        l = len(Counter.objects.all())
        print(l)
        self.assertEqual(l, 0)

    def test_status(self):
        c = Client()
        # follow any redirection
        # log in response.redirect_chain
        # c.post('/counter/up', {'hello': 1})
        # -> 결과 값으로 form data : multipart/form-data
        response = c.post('/counter/up', follow=True)
        print("response=", response)
        print("status_code=", response.status_code)
        print("context=", response.context)
        print("Content-Type=", response['Content-Type'])



