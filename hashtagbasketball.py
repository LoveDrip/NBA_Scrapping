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
        driver.get("https://hashtagbasketball.com/nba-defense-vs-position")
        driver.maximize_window()
        find = driver.find_element
        finds = driver.find_elements
        time.sleep(1)
        texts.append("Summary By Position")
        position = finds(By.TAG_NAME, "table")[0]
        summarypositions = position.find_elements(By.TAG_NAME, "td")
        for summaryposition in summarypositions:
            summaryposition.click()
            time.sleep(5)
            texts.append("Best Defense =====")
            bestDefense = finds(By.TAG_NAME, "table")[2]
            header_best = bestDefense.find_elements(By.TAG_NAME, "th")
            for header in header_best:
                texts.append(header.text + ",")
            body_best = bestDefense.find_elements(By.TAG_NAME, "tr")
            for body in body_best:
                for table_value in body.find_elements(By.TAG_NAME, "td"):
                    texts.append(table_value.text + ",")
                texts.append("=====")
            

        # texts.append("All Position =====")
        # allposition = finds(By.TAG_NAME, "table")[3]
        # header_all = allposition.find_elements(By.TAG_NAME, "th")
        # texts.append("Header =====")
        # for header in header_all:
        #     texts.append(header.text + ",")
        # texts.append("Body =====" + ",")
        # body_all = allposition.find_elements(By.TAG_NAME, "tr")
        # for body in body_all:
        #     for table_value in body.find_elements(By.TAG_NAME, "td"):
        #         texts.append(table_value.text + ",")
        #     texts.append("=====")
        print(texts)
    except Exception as error:
        print('error=================', error)