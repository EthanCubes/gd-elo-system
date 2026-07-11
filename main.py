import requests

ethanCubesID = 31268368

def parseReturnedData(data):
    parts = data.split(":")

    splitData = {}

    for i in range(1, len(parts), 2):
        splitData[parts[i-1]] = parts[i]
    
    return splitData

def getIDByPlayerName(name):
    url = "https://www.boomlings.com/database/getGJUsers20.php"
    data = {
        "secret": "Wmfd2893gb7",
        "str": name
    }
    headers = {
        "User-Agent": ""
    }
    response = requests.post(url, data=data, headers=headers)

    response = response.text
    return response #16 is id

def getDataByPlayerId(playerID):
    url = "https://www.boomlings.com/database/getGJUserInfo20.php"
    data = {
        "secret": "Wmfd2893gb7",
        "targetAccountID": playerID
    }
    headers = {
        "User-Agent": "" 
    }

    response = requests.post(url, data=data, headers=headers)
    
    response = response.text
    return response

user = getIDByPlayerName("EthanCubes")
print(user)
print(parseReturnedData(user))