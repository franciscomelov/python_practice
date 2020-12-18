from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

#chromedriver_location = "/Users/Downloads/chromedriver"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://clickclickclick.click/#d8c4b7c18e2803b6c7b9f936d778857e')

print("waiting")
time.sleep(10)
print("running")


for range in range(1000):
    time.sleep(0.500)
    driver.find_element_by_xpath("/html/body/main/div/div[1]/a") .click()
    print("-")
    print("click")
print("end")
#/html/body/main/div/div[1]/a
#//button[contains(@class,'gsc-search')]
