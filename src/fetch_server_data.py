import requests

# I love writing libraries for me to use

def parse_returned_data(data):
    parts = data.split(":")
    split_data = {}
    for i in range(1, len(parts), 2):
        split_data[parts[i-1]] = parts[i]
    return split_data

def get_id_by_player_name(name):
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
    except ConnectionError:
        return "No Internet connection"
    
    response = response.text
    return response

def get_data_by_player_id(player_id):
    url = "https://www.boomlings.com/database/getGJUserInfo20.php"
    data = {
        "secret": "Wmfd2893gb7",
        "targetAccountID": player_id
    }
    headers = {
        "User-Agent": ""
    }
    try:
       response = requests.post(url, data=data, headers=headers)
    except ConnectionError:
        return "No Internet connection"
    response = response.text
    return response

def convert_data(data):
    name_list = {
        "1": "userName",
        "2": "userID",
        "3": "stars",
        "4": "demons",
        "6": "ranking",
        "7": "accountHighlight",
        "8": "creatorpoints",
        "9": "iconID",
        "10": "color",
        "11": "color2",
        "12": "shipID", # Deprecated, 1.4 and 1.5
        "13": "secretCoints",
        "14": "iconType",
        "15": "special",
        "16": "accountID",
        "17": "usercoins",
        "18": "messageState",
        "19": "friendsState",
        "20": "youTube",
        "21": "accIcon",
        "22": "accShip",
        "23": "accBall",
        "24": "accBird",
        "25": "accDart",
        "26": "accRobot",
        "27": "accStreak",
        "28": "accGlow",
        "29": "isRegistered",
        "30": "globalRank",
        "31": "friendstate",
        "32": "friendRequestID",
        "35": "friendRequestMessage",
        "37": "friendRequestAge",
        "38": "messages",
        "39": "friendRequests",
        "40": "newFriends",
        "41": "NewFriendRequest", # only returned by getGJFriendRequests20
        "42": "age", # only returned by getGJLevelScores211
        "43": "accSpider",
        "44": "twitter",
        "45": "twitch",
        "46": "diamonds",
        "48": "accExplosion",
        "49": "modLevel",
        "50": "commentHistoryState",
        "51": "color3",
        "52": "moons",
        "53": "accSwing",
        "54": "accJetpack",
        "55": "demons",
        "56": "classicLevels",
        "57": "platformerLevels",
        "58": "discord",
        "59": "instagram",
        "60": "tiktok",
        "61": "custom"
    }
    converted_data = {}
    for item in data:
        converted_data[name_list[str(item)]] = data[item]
    return converted_data

def get_data_by_name(name):
    id_data = parse_returned_data(get_id_by_player_name(name))
    try:
        id = int(id_data["16"])
    except:
        return "PlayerNotFound Error. The player may not exits or you may not be connected to the internet"
    raw_player_data = get_data_by_player_id(id)
    parsed_player_data = parse_returned_data(raw_player_data)
    converted_data = convert_data(parsed_player_data)
    return converted_data
