import json, requests

with open("../assets/demonlist.json") as file:
    data = json.load(file)

def getListPoints(name):
    try:
        username = str(data[name])
    except:
        username = str(name)
    url = "https://api.aredl.net/v2/api/aredl/profile/" + username
    listData = requests.get(url)
    listData = listData.json()
    try:
        points = round(listData["rank"]["total_points"])
    except:
        return 0
    return points