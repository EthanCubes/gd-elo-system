import json
import requests
import sys

from pathlib import Path

def get_base_path():
    if getattr(sys, 'frozen', False):
        return Path(sys.MEIPASS)
    else:
        return Path(__file__).resolve().parent.parent

BASE_PATH = get_base_path()
DEMONLIST_NAME_PATH = BASE_PATH / "assets" / "demonlist.json"

with open(DEMONLIST_NAME_PATH, "r") as list_names:
    data = json.load(list_names)

def get_list_points(name):
    try:
        username = str(data[name])
    except KeyError:
        username = str(name)
    url = "https://api.aredl.net/v2/api/aredl/profile/" + username
    list_data = requests.get(url)
    list_data = list_data.json()
    try:
        points = round(list_data["rank"]["total_points"])
        return points
    except KeyError:
        return 0; # This happens when the user isn't in the AREDL database.
