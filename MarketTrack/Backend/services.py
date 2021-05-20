from time import sleep
from re import sub
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
# from UserAccounts.models import *
# from Frontend.models import *

search_urls = {
  "newegg": "https://www.newegg.com/global/uk-en/p/pl?d=_QUERY_",
  "currys": "https://www.currys.co.uk/gbuk/search-keywords/xx_xx_xx_xx_xx/_QUERY_/xx-criteria.html",
  # "ebay": "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=_QUERY_&_sacat=0"
}

'''
  seach_urls stores a dictionary of the static search URLS for the given platforms.
  The full search query replaces the '_QUERY_' and is written in standard
  html ?= query notation. So spaces identified with +:
   
  e.g
  Search Term = "256GB SSD Samsung"
  _QUERY_ = 256GB+SSD+Samsung
'''

def exitDriver(driver):
  '''
    Auxiliary function to cleanly close webDrivers.
  '''
  driver.close()
  driver.quit()

def scheduledScrapes():
  # Order users by number of tracked items to create SJF
  all_users = sorted(UserAccount.objects.all(), key=lambda x: x.numberOfTracked)
  for user in all_users:
    # queryset for userTracked Items
    user_tracked = Tracked.objects.all().filter(user=user)
    for tracked_item in user_tracked:
      item = tracked_item.item
      updatePermanentItem(item)


def updatePermanentItem(item):
  # driver = webdriver.Chrome(ChromeDriverManager().install()) #dependency run
  driver = WebDriver()
  
  # Try scrapes safely
  try:
    # handle Newegg requests
    if(item.abstract_source == "NE"):
      url = item.source
      driver.get(url)
      sleep(2) # chance for whole HTML to load

      # Evaluate Price
      # price_div = driver.find_element_by_class_name('price-current')
      prices_pounds = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/strong').text
      prices_pence = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/sup').text
      total_price = prices_pounds + prices_pence
      
      # Evaluate Stock Availability
      stock_bool = True
      try:
        no_stock_element = driver.find_element_by_xpath('//*[@id="synopsis"]/div[2]/div[1]/p').text
        if(no_stock_element):
          stock_bool = False
      except NoSuchElementException:
        print("stock element not found")

      
      # Produce New PermanentTracked item
      NewPermanent = PermanentTrack(item=item,price=total_price,abstract_source=item.abstract_source, stock_bool=stock_bool, stock_no=-1, timestamp=datetime.now())
      NewPermanent.save()
      
    elif(item.abstract_source == "CU"):
      url = item.source
      driver.get(url)
      sleep(2) # chance for whole HTML to load

      # Evaluate Price
      # price_div = driver.find_element_by_class_name('price-current')
      total_price = driver.find_element_by_xpath('//*[@id="product-actions"]/div[2]/div/div/span').text
      total_price = total_price[1:]

      # Evaluate Stock Availability
      stock_bool = True
      try:
        no_stock_element = driver.find_element_by_xpath('//*[@id="product-actions"]/div[4]/strong/i').text
        if(no_stock_element):
          stock_bool = False
      except NoSuchElementException:
        print("stock element not found")

      
      # Produce New PermanentTracked item
      NewPermanent = PermanentTrack(item=item,price=total_price,abstract_source=item.abstract_source, stock_bool=stock_bool, stock_no=-1, timestamp=datetime.now())
      NewPermanent.save()
      # TrackedItem 
    exitDriver(driver)

  # Must catch exception so driver can exit when given error
  except NameError as error:
    print("Got error: {error}".format(error=error))
    exitDriver(driver)



def search_scrape(query, platform):
  '''
    Web scraping method that ____________
  '''
  
  # Load Chromdriver unto driver object for chrome-based scraping
  # driver = webdriver.Chrome(ChromeDriverManager().install())
  driver = WebDriver()
  
  # Get url for scraping
  user_query = sub(" ", "+", query)
  url = search_urls[platform]
  url = sub("_QUERY_", user_query, url)
  driver.get(url)
  
  # Scrape Specific Functions for each Platform 
  if(platform == "newegg"):
    try:
      # Evaluate/Get first Item Result for Scraping Results
      item_container = driver.find_elements_by_class_name('item-container')[0] #item_container containing the child elements with semantic data, get first item-container
      item_info = item_container.find_elements_by_class_name('item-info')[0]
      item_action = item_container.find_elements_by_class_name('item-action')[0]
      item_title = item_info.find_elements_by_class_name('item-title')[0]
      item_prices_ul_wrapper = item_action.find_elements_by_class_name('price')[0]
      item_prices_li_wrapper = item_prices_ul_wrapper.find_elements_by_class_name('price-current')[0]

      # Derive semantic data from Scraping Results
      name = item_title.text
      source = item_title.get_attribute('href')
      price_pounds = item_prices_li_wrapper.find_element_by_tag_name('strong').text
      price_pence = item_prices_li_wrapper.find_element_by_tag_name('sup').text
      total_price = price_pounds + price_pence

      # Evaluate Stock Availability
      stock_bool = True
      try:
        no_stock_element = item_info.find_element_by_class_name('item-promo')
        if(no_stock_element.text == "OUT OF STOCK"):
          stock_bool = False
      except NoSuchElementException:
        print("stock element not found")
      
      scraped_item = {"name": name, "price": total_price, "stock_bool": stock_bool,"source": source, "abstract_source": "Currys"}
      return scraped_item
    except:
      return {"error":"Could Not Find Any Items"}

  elif(platform == "currys"):
    try:
      # Evaluate/Get first Item Result for Scraping Results
      product_container = driver.find_elements_by_class_name('product')[0] #product containing the child elements with semantic data, get first product
      product_wrapper = product_container.find_elements_by_class_name('productWrapper')[0]
      product_title = product_wrapper.find_elements_by_class_name('productTitle')[0]
      product_title_a = product_title.find_elements_by_tag_name('a')[0]
      product_prices = product_wrapper.find_elements_by_class_name('productPrices')[0]
      channels_avail_wrapper = product_prices.find_elements_by_class_name('channels-availability')[0]
      channels_avail = channels_avail_wrapper.find_elements_by_class_name('prd-channels')[0]
      prices_wrapper = product_prices.find_elements_by_tag_name('div')[0]
      prices_span = prices_wrapper.find_elements_by_tag_name('span')[0]
      
      # Derive semantic data from Scraping Results
      brand_name = product_title_a.find_elements_by_tag_name('span')[0].text
      name_name = product_title_a.find_elements_by_tag_name('span')[1].text
      product_name = brand_name + " " + name_name
      source = product_title_a.get_attribute('href')
      total_price = prices_span.text

      # Price Formatting
      total_price = total_price[1:] #Removes £ symbol as it's always present as first character in string
      total_price = total_price.strip(",")
      total_price = total_price.strip(" ")

      # Evaluate Stock Availability
      stock_bool = True
      try:
        no_stock_element = channels_avail.find_element_by_class_name('nostock')
        if(no_stock_element):
          stock_bool = False
      except NoSuchElementException:
        print("stock element not found")
      
      scraped_item = {"name": product_name, "price": total_price, "stock_bool": stock_bool,"source": source, "abstract_source": "Currys"}
      return scraped_item
    except:
      return {"error":"Could Not Find Any Items"}
  #Need concise implementation and layout to accomodate ebay functionality. 
  elif(platform == "ebay"):
    pass

  exitDriver(driver)

# search_scrape("RTX 2060 super", "newegg")
# scheduledScrapes()
'''
Testing Code:
'''
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

search_scrape("Corsair 16GB RAM", "currys")