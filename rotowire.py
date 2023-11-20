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
        driver.get("https://www.rotowire.com/basketball/nba-lineups.php")
        driver.maximize_window()
        find = driver.find_element
        finds = driver.find_elements
        time.sleep(1)
        find(By.CLASS_NAME, "css-47sehv").click()
        # find(By.CLASS_NAME, "rp")
        time.sleep(1)
        find(By.CLASS_NAME, "fs-close-button").click()
        time.sleep(1)

        texts.append("NBA Lineups" )
        texts.append("=====")
        texts.append("=====")
        texts.append("=====")
        texts.append("First Match")
        texts.append("=====")
        texts.append("=====")

        firstmatch = finds(By.CLASS_NAME, "lineup.is-nba")[0]
        firstmatch_time = firstmatch.find_element(By.CLASS_NAME, "lineup__time").text
        firstmatch_1name = firstmatch.find_elements(By.CLASS_NAME, "lineup__abbr")[0].text
        firstmatch_2name = firstmatch.find_elements(By.CLASS_NAME, "lineup__abbr")[0].text
        firstmatch_1score = firstmatch.find_element(By.CLASS_NAME, "lineup__matchup").find_elements(By.TAG_NAME, "a")[0].text
        texts.append("=====")
        texts.append(firstmatch_time)
        texts.append("=====")

        texts.append(firstmatch_1name + " VS " + firstmatch_2name)
        texts.append("=====")

        texts.append("- " + firstmatch_1name + "( " + firstmatch_1score + " )" + " : ")

        texts.append("=====")
        texts.append("=====")

        texts.append("=====")
        texts.append("MainPlayer:")
        texts.append("=====")
        firstmatch_main = firstmatch.find_element(By.CLASS_NAME, "lineup__list.is-visit").find_elements(By.CLASS_NAME, "lineup__player")
        for player in firstmatch_main:
            if player.get_attribute("title") == "Very Unlikely To Play":
                texts.append(player.find_element(By.TAG_NAME, "div").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "a").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "span").text)
                texts.append(player.find_elements)

            if player.get_attribute("title") == "Very Likely To Play":
                texts.append(player.find_element(By.TAG_NAME, "div").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "a").text)
                texts.append("=====")
            
        texts.append("=====")
        texts.append( "VisitPlayer:" )
        texts.append("=====")
        firstmatch_visit = firstmatch.find_element(By.CLASS_NAME, "lineup__list.is-home").find_elements(By.CLASS_NAME, "lineup__player")
        for player in firstmatch_visit:
            if player.get_attribute("title") == "Very Unlikely To Play":
                texts.append(player.find_element(By.TAG_NAME, "div").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "a").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "span").text )
                texts.append("=====")
            if player.get_attribute("title") == "Very Likely To Play":
                texts.append(player.find_element(By.TAG_NAME, "div").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "a").text )
                texts.append("=====")

        texts.append("References & Line:" )
        texts.append("=====")
        references = firstmatch.find_element(By.CLASS_NAME, "lineup__umpire")
        texts.append("Referees : " + references.text)
        lines = firstmatch.find_elements(By.CLASS_NAME, "lineup__odds-item")
        texts.append("LINE : " + lines[0].find_element(By.CLASS_NAME, 'draftkings').text + ", " + "SPREAD :" + lines[1].find_element(By.CLASS_NAME, 'draftkings').text + ", " + "O/U :" + lines[2].find_element(By.CLASS_NAME, 'draftkings').text)

        
        secondmatch = finds(By.CLASS_NAME, "lineup.is-nba")[1]
        texts.append("Second Match")
        texts.append("=====")
        secondmatch_time = secondmatch.find_element(By.CLASS_NAME, "lineup__time").text
        secondmatch_1name = secondmatch.find_elements(By.CLASS_NAME, "lineup__abbr")[0].text
        secondmatch_2name = secondmatch.find_elements(By.CLASS_NAME, "lineup__abbr")[0].text
        secondmatch_1score = secondmatch.find_element(By.CLASS_NAME, "lineup__matchup").find_elements(By.TAG_NAME, "a")[0].text
        texts.append("=====")
        texts.append(secondmatch_time)
        texts.append("=====")

        texts.append(secondmatch_1name + " VS " + secondmatch_2name)
        texts.append("=====")

        texts.append("- " + secondmatch_1name + "( " + secondmatch_1score + " )" + " : ")

        texts.append("=====")

        texts.append("=====")
        texts.append("MainPlayer:")
        texts.append("=====")
        secondmatch_main = secondmatch.find_element(By.CLASS_NAME, "lineup__list.is-visit").find_elements(By.CLASS_NAME, "lineup__player")
        for player in secondmatch_main:
            if player.get_attribute("title") == "Very Unlikely To Play":
                texts.append(player.find_element(By.TAG_NAME, "div").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "a").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "span").text)
                texts.append("=====")

            if player.get_attribute("title") == "Very Likely To Play":
                texts.append(player.find_element(By.TAG_NAME, "div").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "a").text)
                texts.append("=====")
            
        texts.append("=====")
        texts.append( "VisitPlayer:" )
        texts.append("=====")
        secondmatch_visit = secondmatch.find_element(By.CLASS_NAME, "lineup__list.is-home").find_elements(By.CLASS_NAME, "lineup__player")
        for player in secondmatch_visit:
            if player.get_attribute("title") == "Very Unlikely To Play":
                texts.append(player.find_element(By.TAG_NAME, "div").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "a").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "span").text )
                texts.append("=====")
            if player.get_attribute("title") == "Very Likely To Play":
                texts.append(player.find_element(By.TAG_NAME, "div").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "a").text )
                texts.append("=====")

        texts.append("References & Line:" )
        texts.append("=====")
        references = secondmatch.find_element(By.CLASS_NAME, "lineup__umpire")
        texts.append("Referees : " + references.text)        
        # references = secondmatch.find_element(By.CLASS_NAME, "lineup__umpire").find_elements(By.TAG_NAME, "a")
        # texts.append("References : " + references[0].text + ", " + references[1].text + ", " + references[2].text + ", ")
        lines = secondmatch.find_elements(By.CLASS_NAME, "lineup__odds-item")
        texts.append("LINE : " + lines[0].find_element(By.CLASS_NAME, 'draftkings').text + ", " + "SPREAD :" + lines[1].find_element(By.CLASS_NAME, 'draftkings').text + ", " + "O/U :" + lines[2].find_element(By.CLASS_NAME, 'draftkings').text)
        
        thirdmatch = finds(By.CLASS_NAME, "lineup.is-nba")[0]
        thirdmatch_time = thirdmatch.find_element(By.CLASS_NAME, "lineup__time").text
        thirdmatch_1name = thirdmatch.find_elements(By.CLASS_NAME, "lineup__abbr")[0].text
        thirdmatch_2name = thirdmatch.find_elements(By.CLASS_NAME, "lineup__abbr")[0].text
        thirdmatch_1score = thirdmatch.find_element(By.CLASS_NAME, "lineup__matchup").find_elements(By.TAG_NAME, "a")[0].text
        texts.append("=====")
        texts.append(thirdmatch_time)
        texts.append("=====")

        texts.append(thirdmatch_1name + " VS " + thirdmatch_2name)
        texts.append("=====")

        texts.append("- " + thirdmatch_1name + "( " + thirdmatch_1score + " )" + " : ")

        texts.append("=====")
        texts.append("=====")

        texts.append("=====")
        texts.append("MainPlayer:")
        texts.append("=====")
        thirdmatch_main = thirdmatch.find_element(By.CLASS_NAME, "lineup__list.is-visit").find_elements(By.CLASS_NAME, "lineup__player")
        for player in thirdmatch_main:
            if player.get_attribute("title") == "Very Unlikely To Play":
                texts.append(player.find_element(By.TAG_NAME, "div").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "a").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "span").text)
                texts.append("=====")

            if player.get_attribute("title") == "Very Likely To Play":
                texts.append(player.find_element(By.TAG_NAME, "div").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "a").text)
                texts.append("=====")
            
        texts.append("=====")
        texts.append( "VisitPlayer:" )
        texts.append("=====")
        thirdmatch_visit = thirdmatch.find_element(By.CLASS_NAME, "lineup__list.is-home").find_elements(By.CLASS_NAME, "lineup__player")
        for player in thirdmatch_visit:
            if player.get_attribute("title") == "Very Unlikely To Play":
                texts.append(player.find_element(By.TAG_NAME, "div").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "a").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "span").text )
                texts.append("=====")
            if player.get_attribute("title") == "Very Likely To Play":
                texts.append(player.find_element(By.TAG_NAME, "div").text + ", ")
                texts.append(player.find_element(By.TAG_NAME, "a").text )
                texts.append("=====")

        texts.append("References & Line:" )
        texts.append("=====")
        references = thirdmatch.find_element(By.CLASS_NAME, "lineup__umpire")
        texts.append("Referees : " + references.text)
        lines = thirdmatch.find_elements(By.CLASS_NAME, "lineup__odds-item")
        texts.append("LINE : " + lines[0].find_element(By.CLASS_NAME, 'draftkings').text + ", " + "SPREAD :" + lines[1].find_element(By.CLASS_NAME, 'draftkings').text + ", " + "O/U :" + lines[2].find_element(By.CLASS_NAME, 'draftkings').text)

    except Exception as error:
        print('error=================', error)

f = open("rotowire.txt", "w")
for data in texts:
    
    if data == "=====":
        f.write("\n")
        data=""
    f.write(data)
f.close()