import os
from selenium import webdriver
from time import sleep
import json

CHROMEDRIVER_LOCATION = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)),"chromedriver_win32"),"chromedriver.exe")

def runCrawler():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path=str(CHROMEDRIVER_LOCATION),options=chrome_options)
    url = "https://www.topuniversities.com/university-rankings/usa-rankings/2021"
    
    driver.get(url)
    sleep(10)
    
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button').click()
    sleep(2)
    driver.execute_script("window.scrollTo(0, 1600)")
    sleep(1)
    
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div[3]/div/div[1]/div/div[3]/div[3]/div[1]/div[2]').click()
    sleep(3)
    
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div[3]/div/div[1]/div/div[3]/div[3]/div[1]/div[2]/div[2]/div[4]').click()
    sleep(8)
    listOfUniversities = driver.find_elements_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div[3]/div/div[1]/div/div[3]/div[1]/div[2]/*')
    
    result = []
    for uni in listOfUniversities:
        try:
            name = uni.find_element_by_class_name("uni-link").text
            website = uni.find_element_by_class_name("uni-link").get_attribute('href')
            rating = uni.find_element_by_class_name("overall-score-span").text
            temp = {
                "Name" : name,
                "Rating" : rating,
                "Website" : website
            }
            result.append(temp)
        except:
            continue
    with open('result.txt', 'w') as json_file:
        json.dump(result, json_file)

if __name__ == "__main__":
    runCrawler()