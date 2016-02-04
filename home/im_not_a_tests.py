import unittest

from django.core.urlresolvers import reverse
from django.test import Client
from blog import views

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        testings_app_reversed = ['polls:index', 'blog:home','blog:about', 'taskbuster:index', 'newsletter:home']
        '''#just hardcodding some url, rewrite it latter
        testings_app_NOT_reversed = ['/blog/', '/', '/blog/articles/1', '/polls/1/' ]
        for i in testings_app_NOT_reversed:
            response = self.client.get(i)
            self.assertEqual(response.status_code, 200)
            print ('!! NOT reversed __', i, '__ --- was passed')'''

        for i in testings_app_reversed:
            print ('trying reversed __', i)
            response = self.client.get(reverse(i))
            self.assertEqual(response.status_code, 200)
            print ('!! reversed __', i, '__ --- was passed')