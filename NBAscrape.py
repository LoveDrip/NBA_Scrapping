import time
import sys
import keyboard
import threading
import signal
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options


Sentry = True


def compile_code():
    i = j = k = l = 0
    n = 0
    j1 = k1 = l1 = 0
    headers = []
    texts = []
    pts = 0.0
    player_point = oponnent_point = 0.0
    oponnent_name = ""
    infos = ""
    try:
        chrome_options = Options()
        chrome_options.add_argument("--ignore-certificate-error")
        chrome_options.add_argument("--ignore-ssl-errors")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.nba.com/stats/players/shots-general?GeneralRange=Overall&Season=2023-24&dir=D&sort=GP")
        time.sleep(1)

        driver.maximize_window()

        accept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
        accept.click()
        time.sleep(2)
        # pagination = find(By.CLASS_NAME, "Pagination_pageDropdown__KgjBU").find_element(By.TAG_NAME, "select")
        pagination = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Pagination_pageDropdown__KgjBU select")))
        pagination.click()

        # time.sleep(1)
        # selectAll = find(By.CLASS_NAME, "Pagination_pageDropdown__KgjBU").find_elements(By.TAG_NAME, "option")
        selectAll = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "Pagination_pageDropdown__KgjBU")))
        # option = WebDriverWait(selectAll, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "option")))
        option = selectAll.find_elements(By.TAG_NAME, "option")
        option[0].click()

        # time.sleep(1)
        # table_header = find(By.CLASS_NAME, "Crom_headers__mzI_m").find_elements(By.TAG_NAME, "th")
        # for header in table_header:
        #     headers.append(header.text + " , ")
        # headers.append("--------------------------------------------------------------")    
        

        # tbody = find(By.CLASS_NAME, "Crom_body__UYOcU").find_elements(By.TAG_NAME, "tr")
        tbody_class = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "Crom_body__UYOcU")))
        tbody = WebDriverWait(tbody_class, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
        for rows in tbody:
            row = WebDriverWait(rows, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "td")))
            # print("2")
            # for i in row:
            #     headers.append(i.text + " , ")
            if row[1].text == "BKN":
                headers.append(row[0].text)
            # headers.append("-")    
        # print("new")
        driver1 = webdriver.Chrome(options=chrome_options)
        driver1.get("https://sports.yahoo.com/nba/players/5473/")
        driver1.maximize_window()
        # time.sleep(2)
        # driver1.find_element(By.CLASS_NAME, "btn.secondary.accept-all").click()
        WebDriverWait(driver1, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.secondary.accept-all"))).click()
        
        for name in headers:
            try:
                # search_tag = driver1.find_element(By.CLASS_NAME, "ys-players-index")
                search_tag = WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ys-players-index")))
                # search_button = search_tag.find_element(By.TAG_NAME, "input")
                search_button = WebDriverWait(search_tag, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
                WebDriverWait(driver1, 10).until(
                    EC.element_to_be_clickable((By.TAG_NAME, "input"))
                )
                search_button.clear()
                search_button.send_keys(name)
                time.sleep(2)
                try:
                    

                    
                    # search_elements = search_tag.find_elements(By.TAG_NAME, "a")
                    search_elements = WebDriverWait(search_tag, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
                    print("------------------ " +name+ " --------------------------")
                    if search_elements:
                        search_elements[0].click()
                        time.sleep(2)
                        player_status = WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "Row")))
                        player_position = player_status.find_elements(By.TAG_NAME, "span")[3].text

                        player_key_status = WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ys-player-key-stats")))
                        print("player key status")
                        player_pts = player_key_status.find_elements(By.TAG_NAME, "div")[2].text
                        print("player pts")

                        print("PlayerPosition: " + player_position)
                        WebDriverWait(driver1, 10).until(
                            EC.presence_of_element_located((By.TAG_NAME, "table"))
                        )
                        pts = 0.0
                        
                        GameLogTable = driver1.find_elements(By.TAG_NAME, "table")[0]
                        # print("GameLogTable")
                        tbody = WebDriverWait(GameLogTable, 10).until(
                            EC.presence_of_element_located((By.TAG_NAME, "tbody"))
                        )
                        # print("GameLogTabTbody")
                        matches = WebDriverWait(tbody, 10).until(
                            EC.presence_of_all_elements_located((By.TAG_NAME, "tr"))
                        )
                        # print("Matches")
                        if len(matches) > 0:
                            for bodies in matches:
                                
                                td_23 = WebDriverWait(bodies, 10).until(
                                    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(24)"))  # Assuming it's the 24th td
                                )
                                pts += float(td_23.text)
                            # print("switch to main")
                            # print("Get PTS")
                            
                            # print("matches Length: " + str(len(matches)))

                            # print("--- average ----")
                            # print(float(pts) / float(len(matches)))

                            player_point = 0.0
                            j = k = l = 0

                            average = float(pts) / float(len(matches))
                            for bodies in matches:
                                if (float(WebDriverWait(bodies, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(24)"))).text) - 23.0) > 0.0:
                                    j += 1
                                    # print ("passed j")
                                elif (float(WebDriverWait(bodies, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(24)"))).text) - average) > 5.0:
                                    k += 1
                                    # print ("passed k")
                                elif (float(WebDriverWait(bodies, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(24)"))).text) - average) > -8.0:
                                    l += 1
                                    # print ("passed l")
                            print("get percent")
                            print("J: " +  str(j) + ", K: " + str(k) + ", L: " + str(l))
                            player_point = (j * 70 + k * 20 + l * 10) / float(len(matches))

                            # print("player point : " + str(player_point))
                            for bodies in matches:
                                time.sleep(2)
                                j1 = k1 = l1 = 0
                                match_link = bodies.find_element(By.TAG_NAME, "a").get_attribute("href")
                                # print(match_link)
                                # print("Match Link")
                                driver1.execute_script("window.open(" + "'" + match_link + "'" + "," + " '_blank');")
                                driver1.switch_to.window(driver1.window_handles[1])
                                match_header = WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "match-stats")))
                                oponnent_name = match_header.find_elements(By.TAG_NAME, "a")[0].text
                                # print("Oponent name: " + oponnent_name)            
                                names = oponnent_name.split()
                                oponnent_short_name = names[1]                    
                                # print("oponnentshort name: ", oponnent_short_name)
                                driver1.execute_script("window.open('https://draftedge.com/nba/nba-defense-vs-position/', '_blank');")
                                driver1.switch_to.window(driver1.window_handles[2])



                                # print("Switch to VS position")
                                time.sleep(2)
                                
                                button_groups = WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-group")))
                                # print("Button Groups")
                                positions = button_groups.find_elements(By.TAG_NAME, "button")
                                # print("positions")
                                for btn in positions:
                                    # print(btn.text)
                                    # print(player_position)
                                    btn_text = btn.text
                                    if (btn_text + ",") == player_position:
                                        btn.click()
                                

                                tbody = WebDriverWait(driver1, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "tbody")))
                                # print("TBODY")
                                teams = tbody[0].find_elements(By.TAG_NAME, "tr")
                                tr_elements = tbody[0].find_elements(By.CSS_SELECTOR, 'tr')
                                # print("TEA<S")
                                total = 0.0
                                averag = 0.0
                                n = 0
                                for tr_element in tr_elements:
                                    if tr_element.is_displayed():
                                        n += 1
                                        # print("Element  The td element is visible.")

                                        td = tr_element.find_elements(By.TAG_NAME, "td")
                                        # print("Game: ", td[0].text, " - ", oponnent_short_name)
                                        pts =td[3].text
                                        # print("PTS is succes")
                                        print(pts)
                                        if td[0].text == oponnent_short_name:
                                            if (float(player_pts) -float(int(pts[1:]))) >= 0:
                                                j1 += 1
                                            elif (float(player_pts) - float(int(pts[1:]))) >= -5:
                                                k1 += 1
                                            elif (float(player_pts) - float(int(pts[1:]))) >= -8:
                                                l1 += 1
                                        else:
                                            print("Team Not found")
                                    else:
                                        print("Then TD element is invisible.")

                                driver1.close()
                                driver1.switch_to.window(driver1.window_handles[1])
                                driver1.close()
                                driver1.switch_to.window(driver1.window_handles[0])

                            
                            oponnent_point = (j1 * 70 + k1 * 20 + l1 * 10) / float(len(matches))

                            texts.append(name + ", ")
                            texts.append(str(player_point) + ", ")
                            texts.append(str(oponnent_point) + ", ")
                        else:
                            print("No matches found.")
                    else:
                        print("not element")
                except Exception as error:
                    print('-'*50)
                    print(error)
                    print('-'*50)
                    pass
            except Exception as e:
                print('-'*50)
                print(e)
                print('-'*50)
           
        
        print(texts)

    except Exception as error:
        print('error=================', error)

    print("----------- Calculator finished  -----------")

    print("----------- Save File  -----------")
    f = open("nba.txt", "a")
    for header in texts:
        f.write(header)
        # if header == "-":
        #     header = ""
        f.write(", ")
    f.write("\n") 
    f.close()
    print("----------- Completed Ended  -----------")



def main():
    while Sentry:
        compile_code()
    while True:
        if keyboard.is_pressed("q"):
            print("Q Pressed ending loop")
            sys.exit()
    


if __name__ == "__main__":
    main()