import serverData

name = input("Enter the name of the player you want to search up: ")
playerData = serverData.getDataByName(name)
if playerData == "errorCode1":
    print("Player not found. This may be because the player does not exist or because you aren't connected to the internet")
rating = serverData.calculateRating(playerData)
print(rating)