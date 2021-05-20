from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from django.test import Client
from time import sleep
# from accounts.models import Account

# UserAccount Testing
class UserAccounts(StaticLiveServerTestCase):

  fixtures = ['useraccounts-data.json']

  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.selenium = WebDriver()
    cls.selenium.implicitly_wait(10)

  @classmethod
  def tearDownClass(cls):
    cls.selenium.quit()
    super().tearDownClass()

  def testLogin(self):
    path = self.live_server_url
    pathLogin = path + '/user/login'
    pathEnd = path + '/user/logout'
    login_username = 'TestingBot'
    login_pass = 'Thetester123'
    
    self.selenium.get(pathLogin)
    username_input = self.selenium.find_element_by_id('login_username')
    password_input = self.selenium.find_element_by_id('login_password')
    login_button = self.selenium.find_element_by_id('user_button')
    
    username_input.send_keys(login_username)
    sleep(1)
    password_input.send_keys(login_pass)
    sleep(1)
    login_button.click()
    sleep(2)

    username_display = self.selenium.find_elements_by_id('username')[0].text
    
    #true(pass) if username is displayed on homepage
    self.assertEqual(username_display,login_username)
    
    sleep(2)
    self.selenium.get(pathEnd)
    sleep(2)

    
  # def testRequest(self):
    # login_page = self.client.get('/user/login')
    # self.assertContains(login_page,'csrfmiddlewaretoken')
    # self.assertEqual(login_page.status_code, 200)
