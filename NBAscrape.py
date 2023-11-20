from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException 


i = 0
j = 0
k=0 
l = 0
headers = []
texts = []
pts = 0.0
player_point = 0.0
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

        time.sleep(1)
        # table_header = find(By.CLASS_NAME, "Crom_headers__mzI_m").find_elements(By.TAG_NAME, "th")
        # for header in table_header:
        #     headers.append(header.text + " , ")
        # headers.append("--------------------------------------------------------------")    
        

        tbody = find(By.CLASS_NAME, "Crom_body__UYOcU").find_elements(By.TAG_NAME, "tr")
        for rows in tbody:
            row = rows.find_elements(By.TAG_NAME, "td")
            # for i in row:
            #     headers.append(i.text + " , ")
            if row[1].text == "BKN":
                headers.append(row[0].text)
            # headers.append("-")    
        driver1 = webdriver.Chrome()
        driver1.get("https://sports.yahoo.com/nba/players/5473/")
        driver1.maximize_window()
        time.sleep(2)
        driver1.find_element(By.CLASS_NAME, "btn.secondary.accept-all").click()
        
        for name in headers:
            search_tag = driver1.find_element(By.CLASS_NAME, "ys-players-index")
            search_button = search_tag.find_element(By.TAG_NAME, "input")
            search_button.clear()
            search_button.send_keys(name)
            time.sleep(1)
            try:
                search_elements = search_tag.find_elements(By.TAG_NAME, "a")
                print(name)
                if search_elements:
                    search_elements[0].click()
                    time.sleep(6)
                    try:
                        pts = 0.0
                        i = 0
                        j = 0
                        k = 0
                        
                        GameLogTable = driver1.find_elements(By.TAG_NAME, "table")[0]
                        matches = GameLogTable.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr" )
                        if len(matches) > 0:
                            for bodies in matches:
                                pts += float(bodies.find_elements(By.TAG_NAME, "td")[23].text)
                            
                            print(float(pts) / float(len(matches)))

                            player_point = 0.0
                            average = float(pts) / float(len(matches))
                            for bodies in matches:
                                if (float(bodies.find_elements(By.TAG_NAME, "td")[23].text) - 23.0) > 0.0:
                                    j += 1
                                elif (float(bodies.find_elements(By.TAG_NAME, "td")[23].text) - average) > 5.0:
                                    k += 1
                                elif (float(bodies.find_elements(By.TAG_NAME, "td")[23].text) - average) > -8.0:
                                    l += 1
                            print(j, k, l)
                            player_point = (j * 70 + k * 20 + l * 10) / float(len(matches))

                            print(player_point)
                            texts.append(str(int(player_point)))
                            time.sleep(2)
                        else:
                            print("No matches found.")
                    except (NoSuchElementException, WebDriverException) as e:
                        # Check for specific error messages
                        if "handshake failed" in str(e) and "SSL error code 1, net_error -101" in str(e):
                            print("SSL handshake failed. Please handle the specific SSL error.")
                        else:
                            # Handle other WebDriverExceptions
                            print(f"An error occurred: {e}")
                        pass


                else:
                    print("not element")
            except NoSuchElementException as error:
                pass
            # time.sleep(2)
            
            # headers.append("=====")
            # headers.append("Name: " + find1(By.CLASS_NAME, "ys-name").text)
        
        print(texts)

    except Exception as error:
        print('error=================', error)


f = open("nba.txt", "w")
for header in texts:
    f.write(header)
    if header == "-":
        header = ""
        f.write("\n")
f.close()
