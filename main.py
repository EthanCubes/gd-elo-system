import requests

ethanCubesID = 31268368

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

# print(getDataByPlayerId(ethanCubesID))
print(getIDByPlayerName("EthanCubes"))