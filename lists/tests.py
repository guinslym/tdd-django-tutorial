from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page
# Create your tests here.

class HomePageViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn('<title>To-Do lists</title>', response.content.decode('utf8'))
        self.assertTrue(response.content.startswith(b'<html>'))
        #print(response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))
        #expected_content = open('lists/templates/home.html').read()
        expected_content = render_to_string('home.html')
        self.assertEqual(response.content.decode('utf8'), expected_content)

    def test_home_page_can_store_post_requests(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'new item'
        response = home_page(request)

        expected_content = render_to_string('home.html',
        {'new_item_text': 'new item'})
        self.assertEqual(response.content.decode('utf8'), expected_content)
