import os
import requests

def get_holidays():
    url = "https://apis.digital.gob.cl/fl/feriados/2020"
    r = requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
    # print("ACAAAAAAAAAAAAAAAAaAAAAAAAA",response.status_code)
    holidays = r.json()
    print(type(holidays))
    return holidays
    # holidays_list = []
    # for i in range(len(holidays[i])):
    #     holidays_list.append(holidays[i][i])
    # return holidays_list