import json, requests, os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)
json_path = os.path.join(BASE_DIR, "assets", "demonlist.json")

with open(json_path, "r") as file:
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
        return points
    except:
        return 0