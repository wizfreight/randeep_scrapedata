import itertools

import pandas as pd
from openpyxl.reader.excel import load_workbook
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import openpyxl
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 3})
chromeOptions.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
# chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-dev-shm-usage")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-gpu")
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument("disable-infobars")
chromeOptions.add_argument("--allow-running-insecure-content")
chromeOptions.add_argument("--disable-webgl")
chromeOptions.add_argument("--disable-popup-blocking")
chromeOptions.add_argument("--remote-debugging-port=9222")
chromeOptions.add_argument("--window-size=1920,1080")
chromeOptions.add_argument("--proxy-server='direct://'")
chromeOptions.add_argument("--proxy-bypass-list=*")
s = Service(r'C:\Users\Bindu\PycharmProjects\big_schedules\chromedriver.exe')

driver = webdriver.Chrome(service=s, options=chromeOptions)

url = 'https://www.maharashtradirectory.com/product/freight-forwarders.html'
# inputFile = r"C:\Users\Bindu\Desktop\freight_forward_Randeep's _Data.xlsx"
driver.get(url)
time.sleep(0.1)
inputFile = r"C:\Users\Bindu\Desktop\freight_forward_Randeep's _Data.xlsx"
data = []
raw_data = []
driver.find_element(By.CLASS_NAME,'pb-5')

lists = driver.find_elements(By.XPATH, "//div[@class='result_container--right-title']/a")
links = []
for lis in lists:
    print(lis.get_attribute('href'))
    # Fetch and store the links
    links.append(lis.get_attribute('href'))

# Loop through all the links and launch one by one
for link in links:
    driver.get(link)
    try:
        company_name = driver.find_element(By.XPATH,
                                           '//*[@id="printableArea"]/div/div/div[1]/div/div[1]/div[2]/div').text
        address = driver.find_element(By.XPATH, '//*[@id="printableArea"]/div/div/div[2]/div/div/div[2]/div').text
        phone = driver.find_element(By.XPATH, '//*[@id="printableArea"]/div/div/div[1]/div/div[3]/div[2]/div').text
        raw_data_elem = {'company_name': company_name,
                         'address': address,
                         'phone': phone,
                         }
        raw_data.append(raw_data_elem)
        print(raw_data_elem)
        df = pd.DataFrame(raw_data, columns=['company_name', 'address',
                                             'phone'])

        df.to_csv('mango.csv')
        time.sleep(3)
    except NoSuchElementException:
        pass






#
#