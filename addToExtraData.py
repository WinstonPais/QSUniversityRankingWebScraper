import json


def getJsonData():
    return json.load(open('extraData.json',))

def saveJsonFile(data):
    with open('result2.json', 'w') as json_file:
        json.dump(data, json_file)

def addToExtra():
    # result = {
    #     'coverImage' : '',
    #     'AcceptanceRate' : '',
    #     'ApplicationDeadline' : '',
    #     'ApplicationFee' : '',
    #     'NetPrice' : '',
    #     'TotalAidAwardedPerYear' : '',
    #     'StudentsReceivingAid' : '',
    #     'MedianEarningsAfter6Years' : '',
    #     'GraduationRate' : '',
    #     'EmploymentRateAfter2Years' : ''
    # }
    result = {
        'coverImage' : ''
    }

    res = getJsonData()
    res.append(result)
    saveJsonFile(res)

addToExtra()