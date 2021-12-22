from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options as ChromeOptions 
from bs4 import BeautifulSoup as BS 
import os 
import wget 
from time import sleep
import random
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver

cookie = input('enter cookie: ')

def pars(url): 
   rand = random.randint(10, 1000) 
   cwd = os.getcwd() 

   os.mkdir(f"{cwd}\\{rand}") 
   os.chdir(f"{os.getcwd()}\\{rand}")
   print('folder created.')


   driver.get(url) 
   sleep(1)
   html = driver.page_source
   soup = BS(html, 'html.parser')
   print('page loaded, html received.')

   print('loading in progress.')
   print('ctrl+c - stop loading .')

   try:
      kol = 0
      for el in soup.select('.photos_row '):
         href = el.find('a').get('href')
         urls = ('https://vk.com/' + href)
         driver.get(urls)
         WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, 'pv_photo')))
         sleep(1)
         html_ph = driver.page_source
         soup_ph = BS(html_ph, 'html.parser').find('div', {'id': 'pv_photo'}).find('img').get('src') 
         wget.download(soup_ph) 
         kol += 1
         print(f' Number of uploaded photos: {kol}.')

      print('loading is complete')
      driver.quit() 

   except KeyboardInterrupt: 
      print('\rwork stopped ')
      driver.quit() 

def interceptor(request):
   request.headers['cookie'] = cookie


if __name__ == '__main__':
   link = input('enter link: ')
   options = ChromeOptions()
   options.add_argument('--headless')
   driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')
   driver.request_interceptor = interceptor
   
   pars(link)