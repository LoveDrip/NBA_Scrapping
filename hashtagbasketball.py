from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
        def Bestandworth():
            time.sleep(2)
            texts.append("Best Defense")
            texts.append("=====")
            bestDefense = finds(By.TAG_NAME, "table")[1]
            header_best = bestDefense.find_elements(By.TAG_NAME, "th")
            for header in header_best:
                texts.append(header.text + ", ")
            body_best = bestDefense.find_elements(By.TAG_NAME, "tr")
            for body in body_best:
                for table_value in body.find_elements(By.TAG_NAME, "td"):
                    texts.append(table_value.text + ", ")
                texts.append("=====")
            texts.append("Worst Defense")
            texts.append("=====")

            worstDefense = finds(By.TAG_NAME, "table")[2]
            header_worst = worstDefense.find_elements(By.TAG_NAME, "th")
            for header in header_worst:
                texts.append(header.text + ", ")
            body_worst = worstDefense.find_elements(By.TAG_NAME, "tr")
            for body in body_worst:
                for table_value in body.find_elements(By.TAG_NAME, "td"):
                    texts.append(table_value.text + ", ")
                texts.append("=====")

        time.sleep(1)
        texts.append("Summary By Position")
        texts.append("=====")

        position = finds(By.TAG_NAME, "table")[0]
        summarypositions = position.find_elements(By.TAG_NAME, "input")
        

        if summarypositions[0].is_displayed():
            summarypositions[0].click()
        Bestandworth()
        
        summarypositions4 = finds(By.TAG_NAME, "table")[0].find_elements(By.TAG_NAME, "input")
        if summarypositions4[1].is_displayed():
             summarypositions4[1].click()
        Bestandworth()

        summarypositions1 = finds(By.TAG_NAME, "table")[0].find_elements(By.TAG_NAME, "input")
        if summarypositions1[2].is_displayed():
             summarypositions1[2].click()
        Bestandworth()
        
        summarypositions2 = finds(By.TAG_NAME, "table")[0].find_elements(By.TAG_NAME, "input")
        if summarypositions2[3].is_displayed():
             summarypositions2[3].click()
        Bestandworth()
        
        summarypositions3 = finds(By.TAG_NAME, "table")[0].find_elements(By.TAG_NAME, "input")
        if summarypositions3[4].is_displayed():
            summarypositions3[4].click()
        Bestandworth()

        texts.append("All Position" + "=====")
        allposition = finds(By.TAG_NAME, "table")[3]
        header_all = allposition.find_elements(By.TAG_NAME, "th")
        texts.append("Header" + "=====")
        for header in header_all:
            texts.append(header.text + ", ")
        texts.append("Body" + "=====" + ", ")
        body_all = allposition.find_elements(By.TAG_NAME, "tr")
        for body in body_all:
            for table_value in body.find_elements(By.TAG_NAME, "td"):
                texts.append(table_value.text + ", ")
            texts.append("=====")
    except Exception as error:
        print('error=================', error)

f = open("hashtagbasketball.txt", "w")
for data in texts:
    f.write(data)
    if data == "=====":
        f.write("\n")

f.close()