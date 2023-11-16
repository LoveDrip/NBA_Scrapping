from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

i = 0
headers = []
while(i == 0):
    i += 1
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.nba.com/stats/players/shots-general?GeneralRange=Overall&Season=2023-24&dir=D&sort=GP")
        driver.maximize_window()
        find = driver.find_element
        finds = driver.find_elements
        time.sleep(1)
        accept = find(By.ID, "onetrust-accept-btn-handler")
        accept.click()
        time.sleep(2)
        pagination = find(By.CLASS_NAME, "Pagination_pageDropdown__KgjBU").find_element(By.TAG_NAME, "select")

        pagination.click()
        time.sleep(1)
        selectAll = find(By.CLASS_NAME, "Pagination_pageDropdown__KgjBU").find_elements(By.TAG_NAME, "option")
        option = selectAll[0]
        option.click()
        # time.sleep(1)
        # driver.switch_to.window(driver.window_handles[1])
        # driver.switch_to.window(driver.window_handles[0])

        time.sleep(1)
        table_header = find(By.CLASS_NAME, "Crom_headers__mzI_m").find_elements(By.TAG_NAME, "th")
        for header in table_header:
            print("table_header: ", header)
            headers.append(header.text + " , ")
        headers.append("--------------------------------------------------------------")    
        

        tbody = find(By.CLASS_NAME, "Crom_body__UYOcU").find_elements(By.TAG_NAME, "tr")
        for rows in tbody:
            row = rows.find_elements(By.TAG_NAME, "td")
            for i in row:
                headers.append(i.text + ",") 
            headers.append("--------------------------------------------------------------")    
        f = open("nba.txt", "w")
        for header in headers:
            f.write(header)
            if header == "--------------------------------------------------------------":
                f.write("\n")
        f.close()
    except Exception as error:
        print('error=================', error)


f = open("nba.txt", "w")
print("fs")
for header in headers:
    f.write(header)
    if header == "--------------------------------------------------------------":
        f.write("\n")
f.close()
