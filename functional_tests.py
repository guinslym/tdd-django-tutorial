from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.  She goes to check
        # out its homepage.
        self.browser.get('http://localhost:8004')

        # She notices the page title and header mention to-do lists.
        self.assertIn('To-Do lists', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)

        # She is invited to enter a to-do item straight away.

        # She types "Buy peacock feathers" into a text box (her hobby is tying
        # fly-fishing lures).
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        inputbox.send_keys("\n")

        # When the hits enter, the page updates, and the page lists "1. Buy
        # peacock feathers" as an item in a to-do list.

        # There is still a text box inviting her to add another item.  She
        # enters "Use peacock feathers to make a fly".

        # The page updates again, and now shows both items on her list.

        # Edith wonders whether the site will remember her list.  Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL -- her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main()