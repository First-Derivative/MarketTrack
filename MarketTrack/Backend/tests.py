from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from django.test import Client
from time import sleep
# from accounts.models import Account

# # UserAccount Testing
# class UserAccounts(StaticLiveServerTestCase):

#   fixtures = ['useraccounts_1-data.json']

#   @classmethod
#   def setUpClass(cls):
#     super().setUpClass()
#     cls.selenium = WebDriver()
#     cls.selenium.implicitly_wait(10)

#   @classmethod
#   def tearDownClass(cls):
#     cls.selenium.quit()
#     super().tearDownClass()

#   def testRegister(self):
#     path = self.live_server_url
#     pathRegister = path + '/user/registrations/'
#     pathEnd = path + '/user/logout'
#     username = 'RegisterTest'
#     email = 'testinginput@emails.com'
#     password = 'validpassword123'
    
#     self.selenium.get(pathRegister)
#     username_input = self.selenium.find_element_by_id('register_username')
#     email_input = self.selenium.find_element_by_id('register_email')
#     password1_input = self.selenium.find_element_by_id('register_pass1')
#     password2_input = self.selenium.find_element_by_id('register_pass2')
#     register_button = self.selenium.find_element_by_id('user_button')
    
#     username_input.send_keys(username)
#     sleep(2)
#     email_input.send_keys(email)
#     sleep(2)
#     password1_input.send_keys(password)
#     sleep(2)
#     password2_input.send_keys(password)
#     sleep(2)
#     register_button.click()
#     sleep(2)
    
#     username_display = self.selenium.find_elements_by_id('username')[0].text
#     #true(pass) if username is displayed on homepage
#     self.assertEqual(username_display,login_username)

#     sleep(2)
#     self.selenium.get(pathEnd)
#     sleep(2)