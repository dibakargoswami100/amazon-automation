import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
query = "laptop"
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=3NVZ09554GIHV&sprefix=laptop%2Caps%2C286&ref=nb_sb_noss_2")


    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")
     # print(elem)
    for elem in elems:
       print(elem.text)
   # print(elem.txt)
   # print(elem.get_attribute("outerHTML"))


    time.sleep(2)
    driver.close()