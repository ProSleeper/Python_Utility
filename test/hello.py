from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome 웹 드라이버 생성
driver = webdriver.Chrome('C:/Python/chromedriver.exe')

# url 로딩
driver.maximize_window()
driver.get('https://sukebei.nyaa.si/')


#time.sleep(2)
search = driver.find_element_by_xpath('//*[@id="navbar"]/form/div/input')

search.send_keys('FADSS-018')
#time.sleep(1)

search.send_keys(Keys.ENTER)

downkey = driver.find_element_by_xpath('/html/body/div/div[2]/table/tbody/tr[6]/td[3]/a[1]').click()

