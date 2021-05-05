from time import sleep
from re import sub
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from exceptions import ItemNotFound
# from UserAccounts.models import UserAccount
# from Frontend.models import Item, Tracked, PermanentTrack

search_urls = {
  "newegg": "https://www.newegg.com/global/uk-en/p/pl?d=_QUERY_",
  "currys": "https://www.currys.co.uk/gbuk/search-keywords/xx_xx_xx_xx_xx/_QUERY_/xx-criteria.html",
  "ebay": "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=_QUERY_&_sacat=0"
}

'''
  seach_urls stores a dictionary of the static search URLS for the given platforms.
  The full search query replaces the '_QUERY_' and is written in standard
  html ?= query notation. So spaces identified with +:
   
  e.g
  Search Term = "256GB SSD Samsung"
  _QUERY_ = 256GB+SSD+Samsung
'''


def scheduledScrapes():
  # Order users by number of tracked items to create SJF
  all_users = sorted(UserAccount.objects.all(), key=lambda x: x.numberOfTracked)
  for user in all_users:
    # queryset for userTracked Items
    user_tracked = Tracked.objects.all().filter(user=user)
    for tracked_item in user_tracked:
      item = tracked_item.item
      updatePermanentItem(item)

def updatePermanentItem():
  pass  

def exitDriver(driver):
  '''
    Auxiliary function to cleanly close webDrivers.
  '''
  driver.close()
  driver.quit()

def scrapeHandler(query):
  pass

def search_scrape(query, platform):
  '''
    Web scraping method that ____________
  '''
  
  # Load Chromdriver unto driver object for chrome-based scraping
  driver = webdriver.Chrome(ChromeDriverManager().install())
  # driver = webdriver.Chrome('chromedriver')
  
  # Get url for scraping
  user_query = sub(" ", "+", query)
  url = search_urls[platform]
  url = sub("_QUERY_", user_query, url)
  driver.get(url)
  
  # Scrape Specific Functions for each Platform 
  if(platform == "newegg"):
    items = []

    # Initial Scraping of elements based on xpath
    search_results = driver.find_element(By.CLASS_NAME, 'product').Click();
    # search_results = driver.find_elements(By.XPATH, '/html/body/div/div[4]/div/div[1]/div/p')
    sleep(10)
    print(search_results, len(search_results))
    # # Check for non-result query.
    # if(len(search_results) == 0):
    #   exit(driver)
    #   raise ItemNotFound(platform)
    #   return
    
    # data = []
    # for i in range(len(search_results)):
    #   if(search_results[i].is_displayed()):
    #       driver.findElement(By.cssSelector("body")).sendKeys(Keys.CONTROL +"t");
    #       search_results[i].click()
    #       sleep(4)
    #       # item = driver.find_elements

    #       # print(item.)

    # sleep(10)

  elif(platform == "currys"):
    pass
  elif(platform == "ebay"):
    pass

  exitDriver(driver)
  


# search_scrape("RTX 2060 super", "newegg")
# scheduledScrapes()

def test():

  # Load Chromdriver unto driver object for chrome-based scraping
  driver = webdriver.Chrome(ChromeDriverManager().install())
  
  url = "https://chiefobrienatwork.com/post/106684455801/episode-1-r%C3%A9sum%C3%A9-builder-read-the-next-episode"
  driver.get(url)
  identifier = "/html/body/div[3]/div[2]/article/div[2]/div[1]/p[1]"

  item = driver.find_elements(By.XPATH, identifier)

  print("item", item)
  print("item.text", item.text)

  exitDriver(driver)

test()