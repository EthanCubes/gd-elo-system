import requests, demonlist

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
    try:
        response = requests.post(url, data=data, headers=headers)
    except:
        return "No internet connection"

    response = response.text
    return response

def getDataByPlayerId(playerID):
    # credit to ____ for code
    url = "https://www.boomlings.com/database/getGJUserInfo20.php"
    data = {
        "secret": "Wmfd2893gb7",
        "targetAccountID": playerID
    }
    headers = {
        "User-Agent": "" 
    }

    try:
        response = requests.post(url, data=data, headers=headers)
    except:
        return "No internet connection"
    
    response = response.text
    return response

def getDataByName(name):
    idData = parseReturnedData(getIDByPlayerName(name))
    try:
        id = int(idData["16"])
    except:
        return "No internet connection"

    playerData = getDataByPlayerId(id)
    parsedPlayerData = parseReturnedData(playerData)

    try:
        splitDemons = parsedPlayerData["55"].split(",")
    except:
        splitDemons = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    listPoints = demonlist.getListPoints(name)

    try:
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
            "extremeDemons": int(splitDemons[4]) + int(splitDemons[9]),

            "listPoints": listPoints
        }
    except:
        return "request blocked"
    return formattedPlayerData

def calculateRating(playerData):
    rating = 0
    try:
        rating += int(playerData["stars"])
        rating += int(playerData["moons"])
        rating += 3*int(playerData["secretCoins"])
        rating += 3*int(playerData["userCoins"])
        rating += 10*int(playerData["demons"])
        rating += 10*int(playerData["easyDemons"])
        rating += 20*int(playerData["mediumDemons"])
        rating += 40*int(playerData["hardDemons"])
        rating += 80*int(playerData["insaneDemons"])
        rating += 160*int(playerData["extremeDemons"])
        if playerData["listPoints"] >= 1:
            rating *= float(playerData[listPoints]/10)
        round(rating)
    except:
        return "Error in rating calcuation"

    return rating