import requests
import pandas as pd
import json

def getJsonData():
    return json.load(open('result2.json',))

def getImg():
    data = getJsonData()
    # urls = pd.read_csv('cat_urls.csv') #save the url list as a dataframe

    rows = [d["ImageURL"] for d in data]

    # for index, i in urls.iterrows():
    #     rows.append(i[-1])



    counter = 0

    for i in rows:
    

        file_name = str(data[counter]["Name"]) + '.jpg'
        
        print(file_name)
        response = requests.get(i)
        file = open(f'ProfilePics\{file_name}', "wb")
        file.write(response.content)
        file.close()
        counter += 1

getImg()