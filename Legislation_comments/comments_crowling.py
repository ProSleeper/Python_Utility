import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

from time import sleep

##################################################################################



URL = 'https://pal.assembly.go.kr/attention/readView.do?lgsltpaId=PRC_Z2H1L0B3W2Q2B1P4Y3K8M1W1C1N0C2#a'

driver = webdriver.Chrome(executable_path='C:\\Users\\ingn\\Desktop\\chromedriver_win32 (1)\\chromedriver')
driver.get(url=URL)
# driver.execute_script('_getCommentList(20)')

# driver.execute_script('_getCommentList(23)')
# driver.implicitly_wait(10)
# sleep(1)

pageW = driver.find_element_by_class_name('page_w')
pageA = pageW.find_elements_by_tag_name('a')

PageCount = None;

for e in pageA:
    # print(e.get_attribute('href'));
    PageCount = e.get_attribute('href')

# print(len(PageCount))

pageNumber = ""

for p in range(len(PageCount) - 1, 0, -1):
    if PageCount[p] == '(':
        break
    elif PageCount[p] == ')':
        continue
    
    # print(PageCount[p])
    pageNumber = pageNumber + PageCount[p]

numberValue = ""

for r in range(len(pageNumber) - 1, -1, -1):
    numberValue = numberValue + pageNumber[r]

numberValue = int(numberValue)

print(numberValue)

# for n in range(numberValue):
n = 268;# 크롤링을 시작할 page의 번호

while n <= numberValue:
    driver.execute_script('_getCommentList(' + str(n) + ')');
    sleep(0.5);

    table = driver.find_element_by_class_name('sub_board')
    tbody = table.find_element_by_tag_name("tbody");
    rows = tbody.find_elements_by_tag_name("tr")

    with open("lawlist.txt", mode = "a") as file:
        for e in rows:
            if e.text != "":
                print(e.text);
                file.writelines(e.text+'\n')
            
    
    n += 1;
    
print("완료");

sleep(60)
driver.close();

