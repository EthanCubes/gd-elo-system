import serverData

def userSearch(name):
    playerData = serverData.getDataByName(name)
    if playerData == "errorCode1":
        return "Player not found. This may be because the player does not exist or because you aren't connected to the internet"
    rating = serverData.calculateRating(playerData)
    return playerData, rating