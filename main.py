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

def getDataByName(name):
    idData = parseReturnedData(getIDByPlayerName(name))
    id = int(idData["16"])

    playerData = getDataByPlayerId(id)
    parsedPlayerData = parseReturnedData(playerData)

    splitDemons = parsedPlayerData["55"].split(",")
    print(splitDemons)

    formattedPlayerData = {
        "name": parsedPlayerData["1"],
        "stars": parsedPlayerData["3"],
        "moons": parsedPlayerData["52"],
        "secretCoins": parsedPlayerData["13"],
        "userCoins": parsedPlayerData["17"],
        
        "demons": parsedPlayerData["4"],

        "easyDemons": int(splitDemons[0]) + int(splitDemons[5]),
        "mediumDemons": int(splitDemons[1]) + int(splitDemons[6]),
        "hardDemons": int(splitDemons[2]) + int(splitDemons[7]),
        "insaneDemons": int(splitDemons[3]) + int(splitDemons[8]),
        "extremeDemons": int(splitDemons[4]) + int(splitDemons[9])
    }
    return formattedPlayerData

name = input("Enter someone to search up")
print(getDataByName(name))