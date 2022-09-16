from typing import List
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert

from bs4 import BeautifulSoup
import re
import copy
import math 
import time

from time import sleep

##################################################################################


URL = 'https://sukebei.nyaa.si/'

driver = webdriver.Chrome(executable_path='C:\\Users\\ingn\\Desktop\\chromedriver_win32\\chromedriver')
driver.maximize_window()
driver.get(url=URL)
# driver.execute_script('_getCommentList(20)')

# driver.execute_script('_getCommentList(23)')
# driver.implicitly_wait(10)
# sleep(1)

workList = list();  # 품번을 저장할 리스트

with open("sakuhinbango.txt", mode = "r") as file:
    for line in file:
        workList.append(line.replace("\n", ""))

print(workList)
iter = 0
while iter < len(workList):    # 여기 조건을 위의 workList의 요소를 다 돌았다면 끝내는 것으로 하면 됨
    try:
        start = time.time()
        searchTextBox = driver.find_element_by_xpath('//*[@id="navbar"]/form/div/input')
        searchTextBox.clear()
        searchTextBox.send_keys(workList[iter]); #검색창에 품번 적는 부분
        # driver.find_element_by_xpath('//*[@id="navbar"]/form/div/input').send_keys('stars') #검색창에 품번 적는 부분
        searchButton = driver.find_element_by_xpath('//*[@id="navbar"]/form/div/div[3]')
        searchButton.click()

        # listTable = driver.find_element_by_xpath('/html/body/div/div[2]')
        # listTable = driver.find_element_by_xpath('/html/body/div/div[2]')
        table = driver.find_element_by_class_name("table.table-bordered.table-hover.table-striped.torrent-list")
        tbody = table.find_element_by_tag_name("tbody")
        trTable = list()
        for tr in tbody.find_elements_by_tag_name("tr"):
            if tr.get_attribute('class') == 'success':
                trTable.append(tr)
        moreSize = 0.0
        downData = None
        for success_tr in trTable:
            tdTable = list()
            for td in success_tr.find_elements_by_tag_name("td"):
                tdTable.append(td)
            size = float(re.sub(r"[^0-9.]","",tdTable[3].text))
            if size > moreSize: # 이 부분에 용량이 같을 때 시드로 비교 하는 부분을 추가하면 좋을 듯
                moreSize = size
                downData = tdTable[2]
                
        # 일단은 마그넷 버튼 클릭으로 해보기
        aList = list()
        for a in downData.find_elements_by_tag_name('a'):
            aList.append(a)
        magnetButton = aList[0]; #리스트의 0은 torrent 파일 다운 1은 마그넷 실행
        magnetButton.click()
        print("실행: " + str(iter))
    except :
        try:
            print("오류 발생: " + str(iter))
            print("continue")
            iter += 1
            continue
        except:
            print("오류 발생except")
            iter += 1
    iter += 1
    end = time.time() 
    print(f"{end - start:.5f} sec")

# driver.find_element_by_xpath('//*[@id="navbar"]/form/div/input').send_keys(workList[1]) #검색창에 품번 적는 부분
# driver.find_element_by_xpath('//*[@id="navbar"]/form/div/input').send_keys('stars') #검색창에 품번 적는 부분
# searchButton = driver.find_element_by_xpath('//*[@id="navbar"]/form/div/div[3]')
# searchButton.click();

# # listTable = driver.find_element_by_xpath('/html/body/div/div[2]')
# # listTable = driver.find_element_by_xpath('/html/body/div/div[2]')
# table = driver.find_element_by_class_name("table.table-bordered.table-hover.table-striped.torrent-list")
# tbody = table.find_element_by_tag_name("tbody");
# trTable = list();
# for tr in tbody.find_elements_by_tag_name("tr"):
#     if tr.get_attribute('class') == 'success':
#         trTable.append(tr);
# print(trTable)
# trs = tbody.find_element_by_tag_name("tr");
# print(trs.text + "와우")

sleep(3)
driver.close()


# 구현순서
#Check 1. 한줄에 1품번씩 적혀 있는 txt 파일을 읽어서 데이터베이스에 저장 

#Check 2. 열려진 nyaa사이트의 검색 텍스트박스 찾기
#Check 3. 텍스트박스에 포커스 줌
#Check 4. 품번 입력

# 5. 검색 시작
# 6. 배경이 녹색으로 된 라인 찾음(여러개가 가능하기 때문에 어떤 조건으로 1개를 걸러낼지 판단해야함)
# 7. torrent 파일로 다운(마그넷으로 다운해도 될것 같은데 이건 나중에 구현하면서 선택하기로)

# 특이사항
# torrent 파일로 다운로드시 최소 6초의 제한이 사이트 자체적으로 걸려 있는듯

