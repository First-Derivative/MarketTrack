from time import sleep
from re import sub
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from exceptions import ItemNotFound

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

def exit(driver):
  '''
    Auxiliary function to cleanly close webDrivers.
  '''
  driver.close()
  driver.quit()


def search_scrape(query, platform):
  '''
    Web scraping method that ____________
  '''
  
  # Load Chromdriver unto driver object for chrome-based scraping
  driver = webdriver.Chrome('chromedriver')
  
  # Get url for scraping
  user_query = sub(" ", "+", query)
  url = search_urls[platform]
  url = sub("_QUERY_", user_query, url)

  driver.get(url)
  
  # Scrape Specific Functions for each Platform 
  if(platform == "newegg"):
    items = []

    # Initial Scraping of elements based on xpath
    search_results = driver.find_elements_by_xpath('//div[@class="item-cell"]')
    
    # Check for non-result query.
    if(len(search_results) == 0):
      exit(driver)
      raise ItemNotFound(platform)
      return
    
    data = []
    for i in range(len(search_results)):
      if(search_results[i].is_displayed()):
          driver.findElement(By.cssSelector("body")).sendKeys(Keys.CONTROL +"t");
          search_results[i].click()
          sleep(4)
          # item = driver.find_elements

          # print(item.)

    # sleep(10)

  elif(platform == "currys"):
    pass
  elif(platform == "ebay"):
    pass

  exit(driver)
  


search_scrape("RTX 2060 super", "newegg")