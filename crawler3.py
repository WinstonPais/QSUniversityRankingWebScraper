import os
from selenium import webdriver
from time import sleep
import json

CHROMEDRIVER_LOCATION = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)),"chromedriver_win32"),"chromedriver.exe")

def getJsonData():
    return json.load(open('result2.json',))


def getMyUni():
    data = getJsonData()
    myUnis = set()
    for uni in data:
        myUnis.add(uni["Name"])

    return myUnis

def runCrawler():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path=str(CHROMEDRIVER_LOCATION),options=chrome_options)

    setOf100Unis = getMyUni()
    url = 'https://www.niche.com/colleges/search/best-colleges/?page='
    for pageNo in range(1,113):
        driver.get(url + str(pageNo))
        sleep(10)
        UniListItems = driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/main/div[2]/ol/*')

        for uniListItem in UniListItems:
            uniListItem.find_element_by_class_name('search-result__title').text
        break


if __name__ == "__main__":
    runCrawler()
