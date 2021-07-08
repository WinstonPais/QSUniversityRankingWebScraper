import os
from selenium import webdriver
from time import sleep
import json

CHROMEDRIVER_LOCATION = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)),"chromedriver_win32"),"chromedriver.exe")

def getUrls():
    return json.load(open('result1.json',))

def runCrawler():
    urls = getUrls()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path=str(CHROMEDRIVER_LOCATION),options=chrome_options)

    result = []
    num = 1
    for obj in urls:
        try:
            url = obj['Website']
            
            driver.get(url)
            sleep(5)

            uniImageUrl = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/main/section/div/section/section/div/div/article/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/img').get_attribute('src')
            # print(uniImageUrl)
            status = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/main/section/div/section/section/div/div/article/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/ul/li[1]/span[2]').text
            researchOutput = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/main/section/div/section/section/div/div/article/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/ul/li[2]/span[2]').text
            studentFacultyRatio = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/main/section/div/section/section/div/div/article/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/ul/li[3]/span[2]').text
            if len(driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/main/section/div/section/section/div/div/article/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/ul/*')) == 6:
                
                internationalStudents = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/main/section/div/section/section/div/div/article/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/ul/li[4]/span[2]').text
                size = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/main/section/div/section/section/div/div/article/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/ul/li[5]/span[2]').text
                totalFaculty = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/main/section/div/section/section/div/div/article/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/ul/li[6]/span[2]').text
            else:
                internationalStudents = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/main/section/div/section/section/div/div/article/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/ul/li[5]/span[2]').text
                size = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/main/section/div/section/section/div/div/article/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/ul/li[6]/span[2]').text
                totalFaculty = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/main/section/div/section/section/div/div/article/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/ul/li[7]/span[2]').text
            print(num, [status, researchOutput, studentFacultyRatio, internationalStudents, size, totalFaculty])
            num += 1

            temp = dict(obj)
            temp['ImageURL'] = uniImageUrl
            temp['status'] = status
            temp['Research Output'] = researchOutput
            temp['Student/Faculty Ratio'] = studentFacultyRatio
            temp['International Students'] = internationalStudents
            temp['Size'] = size
            temp['Total Faculty'] = totalFaculty

            result.append(temp)
        except:
            print('**************************')
            print(num)
            print('**************************')

            num += 1
            continue
    
    with open('result2.json', 'w') as json_file:
        json.dump(result, json_file)

if __name__ == "__main__":
    runCrawler()