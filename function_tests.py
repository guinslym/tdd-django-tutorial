import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        #Edith has heard about a cool new online to-do app. She goes
        #to check this homepage
        self.browser.get('http://localhost:8004')
        #she notics the page title and header mentionned to-do
        self.assertIn('To-Do', self.browser.title)
        self.fail('finish the test!')

        #she is invited to enter a to-do item straight away
        #she types "Buy peacock feathers" into a text box
        #is tying fly-fishing lures
        #when she hits enter, the page updates, 

if __name__ == '__main__':
    unittest.main()
