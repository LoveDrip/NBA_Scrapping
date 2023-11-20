from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


i = 0
texts = []

while(i == 0):
    i += 1
    try:
        driver = webdriver.Chrome()
        driver.get("https://sports.yahoo.com/nba/players/6032/")
        time.sleep(2)
        driver.maximize_window()
        find = driver.find_element
        finds = driver.find_elements

        find(By.CLASS_NAME, "btn.secondary.accept-all").click()
        time.sleep(1)
        playerlist = finds(By.TAG_NAME, "table")[3].find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")
        time.sleep(2)
        texts.append("=====")
        texts.append("Players Information")
        texts.append("=====")

        for player in playerlist:
           
            playerlink = player.find_element(By.TAG_NAME, "a").get_attribute("href")

            driver1 = webdriver.Chrome()
            driver1.get(playerlink)
            time.sleep(1)
            driver1.maximize_window()
            find1 = driver1.find_element
            # finds = driver1.find_elements
            find1(By.CLASS_NAME, "btn.secondary.accept-all").click()
            texts.append("=====")
            texts.append("Name: " + find1(By.CLASS_NAME, "ys-name").text)
            texts.append("=====")
            texts.append(find1(By.CLASS_NAME, "Row").text)
            texts.append("=====")
            positions = find1(By.CLASS_NAME, "ys-player-key-stats").find_elements(By.TAG_NAME, "div")
            texts.append(positions[1].text + ": " + positions[2].text + ", " +  positions[4].text + ": " + positions[5].text + ", " + positions[7].text + ": " + positions[8].text)            
            texts.append("=====")
            bios = find1(By.CLASS_NAME, "PlayerBio").find_elements(By.TAG_NAME, "div")
            texts.append(bios[2].find_elements(By.TAG_NAME, "span")[0].text + " : " + bios[2].find_elements(By.TAG_NAME, "span")[2].text)
            texts.append("=====")
            texts.append(bios[3].find_elements(By.TAG_NAME, "span")[0].text + " : " + bios[3].find_elements(By.TAG_NAME, "span")[2].text)
            texts.append("=====")
            texts.append(bios[4].find_elements(By.TAG_NAME, "span")[0].text + " : " + bios[4].find_elements(By.TAG_NAME, "span")[0].text)
            texts.append("=====")
            texts.append(bios[5].find_elements(By.TAG_NAME, "span")[0].text + " : " + bios[5].find_elements(By.TAG_NAME, "span")[2].text)
            texts.append("=====")

            texts.append("Reguar Season")
            texts.append("=====")

            try:
                GameLogTable = driver1.find_elements(By.TAG_NAME, "table")[0]
                for headers in GameLogTable.find_element(By.TAG_NAME, "thead").find_elements(By.TAG_NAME, "tr"):
                    for header in headers.find_elements(By.TAG_NAME, "th"):
                        texts.append(header.text)
                    texts.append("=====")
                texts.append("=====")
                for bodies in GameLogTable.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr" ):
                    for body in bodies.find_elements(By.TAG_NAME, "td"):
                        try:
                            texts.append(body.find_element(By.TAG_NAME, "span").text)
                        except NoSuchElementException:
                            pass
                        try:
                            texts.append(body.find_element(By.TAG_NAME, "a").text)
                        except NoSuchElementException:
                            pass
                    texts.append("=====")
                texts.append("=====")
                time.sleep(2)

            except NoSuchElementException:
                pass

            try:
                GameLogTable1 = driver1.find_elements(By.TAG_NAME, "table")[1]
                for headers in GameLogTable1.find_element(By.TAG_NAME, "thead").find_elements(By.TAG_NAME, "tr"):
                    for header in headers.find_elements(By.TAG_NAME, "th"):
                        texts.append(header.text + ", ")
                    texts.append("=====")
                texts.append("=====")
                for bodies in GameLogTable1.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr" ):
                    for body in bodies.find_elements(By.TAG_NAME, "td"):
                        try:
                            texts.append(body.find_element(By.TAG_NAME, "span").text)
                        except NoSuchElementException:
                            pass
                        try:
                            texts.append(body.find_element(By.TAG_NAME, "a").text)
                        except NoSuchElementException:
                            pass
                    texts.append("=====")
                texts.append("=====")

                time.sleep(2)

            except NoSuchElementException:
                pass

            try:
                GameLogTable2 = driver1.find_elements(By.TAG_NAME, "table")[2]
                for headers in GameLogTable2.find_element(By.TAG_NAME, "thead").find_elements(By.TAG_NAME, "tr"):
                    for header in headers.find_elements(By.TAG_NAME, "th"):
                        texts.append(header.text + ", ")
                    texts.append("=====")
                texts.append("=====")
                for bodies in GameLogTable2.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr" ):
                    for body in bodies.find_elements(By.TAG_NAME, "td"):
                        try:
                            texts.append(body.find_element(By.TAG_NAME, "span").text)
                        except NoSuchElementException:
                            pass
                        try:
                            texts.append(body.find_element(By.TAG_NAME, "a").text)
                        except NoSuchElementException:
                            pass
                    texts.append("=====")
                texts.append("=====")
                
                time.sleep(2)

            except NoSuchElementException:
                pass
            
        driver1.quit()
    except Exception as error:
        print('error=================', error)


f = open("nbaplayers.txt", "w")
for data in texts:
    
    if data == "=====":
        f.write("\n")
        data=""
    f.write(data)
f.close()