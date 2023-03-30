import itertools

import pandas as pd
from openpyxl.reader.excel import load_workbook
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import openpyxl
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

url = 'https://www.wcaworld.com/directory?siteID=24&au=&pageIndex=1&pageSize=100&searchby=CountryCode&country=IN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=118&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&networkIds=116&layout=v1&submitted=search'
# inputFile = r"C:\Users\Bindu\Desktop\freight_forward_Randeep's _Data.xlsx"
driver.get(url)

inputFile = r"C:\Users\Bindu\Desktop\freight_forward_Randeep's _Data.xlsx"
raw_data = []
lists = driver.find_elements(By.XPATH, "//li[@class='directoyname']/a[1]")
links = []
while True:
    for lis in lists:
        print(lis.get_attribute('href'))
        # Fetch and store the links
        links.append(lis.get_attribute('href'))

    # Loop through all the links and launch one by one
    for link in links:
        driver.get(link)
        try:
            company_name = driver.find_element(By.XPATH, "//div[@class='company']").text
            address = driver.find_element(By.XPATH, '//*[@class="profile_headline"]/following-sibling::span').text
            phone = driver.find_element(By.XPATH, '//*[@class="profile_row"]').text
            raw_data_elem = {'company_name': company_name,
                             'address': address,
                             'phone': phone,
                             }
            raw_data.append(raw_data_elem)
            df = pd.DataFrame(raw_data, columns=['company_name', 'address',
                                                 'phone'])

            df.to_csv('mango.csv')


        except NoSuchElementException:
            pass




