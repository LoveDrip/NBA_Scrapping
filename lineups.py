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
texts = []
while(i == 0):
    i += 1
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.lineups.com/nba/lineups")
        driver.maximize_window()
        find = driver.find_element
        finds = driver.find_elements    
        time.sleep(1)

        leftmenus = finds(By.CLASS_NAME, "starting-lineup-box")
        for leftmenu in leftmenus:
            shorttermname = leftmenu.find_element(By.CLASS_NAME, "event-away-participant").find_element(By.CLASS_NAME, "link-black-underline").find_elements(By.TAG_NAME, "span")[1].text          
            standing = leftmenu.find_element(By.CLASS_NAME, "event-away-participant").find_element(By.CLASS_NAME, "event-top-participant-standing").text
            texts.append("+++++" + shorttermname + "," + standing + "-----")
            headers = leftmenu.find_elements(By.TAG_NAME, "table")[0].find_element(By.CLASS_NAME, "stats-head").find_elements(By.TAG_NAME, "th")
            for header in headers:
                texts.append(header.text)
            texts.append("-----")
            boides = leftmenu.find_elements(By.TAG_NAME, "table")[0].find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")
            for body in boides:
                texts.append(body.find_element(By.TAG_NAME, "th").text + ", ")
                for basketinfo in body.find_elements(By.TAG_NAME, "td"):
                    texts.append(basketinfo.text + ",")
                texts.append("-----")
            time = leftmenu.find_element(By.CLASS_NAME, "event-date-cal-date").find_element(By.TAG_NAME, "h4").text
            texts.append("::::: VS - " + time + " ")
            texts.append(":::::")


            shorttermname1 = leftmenu.find_element(By.CLASS_NAME, "event-home-participant").find_element(By.CLASS_NAME, "link-black-underline").find_elements(By.TAG_NAME, "span")[1].text          
            standing1 = leftmenu.find_element(By.CLASS_NAME, "event-home-participant").find_element(By.CLASS_NAME, "event-top-participant-standing").text
            texts.append("+++++" + shorttermname1 + "," + standing1 + "-----")
            headers1 = leftmenu.find_elements(By.TAG_NAME, "table")[0].find_element(By.CLASS_NAME, "stats-head").find_elements(By.TAG_NAME, "th")
            for header in headers1:
                texts.append(header.text)
            texts.append("-----")
            boides1 = leftmenu.find_elements(By.TAG_NAME, "table")[0].find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")
            for body in boides:
                texts.append(body.find_element(By.TAG_NAME, "th").text + ", ")
                for basketinfo in body.find_elements(By.TAG_NAME, "td"):
                    texts.append(basketinfo.text + ",")
                texts.append("-----")
            texts.append("=====")
        print(texts)
    except Exception as error:
        print('error=================', error)

f = open("lineups.txt", "w")
for data in texts:
    if data == "+++++":
        f.write("============================")
    f.write(data)
    if data == "-----":
        f.write("\n")
    if data == ":::::":
        f.write("\n")
    if data == "=====":
        f.write("============================")
        f.write("\n")
        f.write("\n")

f.close()