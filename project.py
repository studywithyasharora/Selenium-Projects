from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
query = "badminton+rackets"
file = 0
i = 0
for i in range(1,3):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=1GPSDEWYB7GHK&sprefix=badmin%2Caps%2C240&ref=nb_sb_ss_pltr-data-refreshed_2_6")

elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
print(f"{len(elems)} items found")
for elem in elems:
    d = elem.get_attribute("outerHTML")
    with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
        f.write(d)
        file+=1
#print(elem.text)
#print(elem)

time.sleep(0.2)
driver.close()