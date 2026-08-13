import tkinter as tk
import sys

from fetch_server_data import get_data_by_name
from calculate_elo import calculate_elo
from fetch_aredl_data import get_list_points

from pathlib import Path

def get_base_path():
    if getattr(sys, 'frozen', False):
        return Path(sys.MEIPASS)
    else:
        return Path(__file__).resolve().parent.parent

BASE_PATH = get_base_path()

def search():
    name = search_text.get()
    data = get_data_by_name(name)
    # now, we need to process the data and then change it into data that can be read by the user
    # Stars
    # Moons
    # Secret and user coins
    # Demons
    # List Points
    try:
        elo = calculate_elo(name)
        stars = data["stars"]
        moons = data["moons"]
        secret_coins = data["secretCoins"]
        user_coins = data["usercoins"]
        easy_demons = int(data["demons"][0]) + int(data["demons"][5])
        medium_demons = int(data["demons"][1]) + int(data["demons"][6])
        hard_demons = int(data["demons"][2]) + int(data["demons"][7])
        insane_demons = int(data["demons"][3]) + int(data["demons"][8])
        extreme_demons = int(data["demons"][4]) + int(data["demons"][9])
        list_points = get_list_points(name)

        username_message.config(text=name)
        elo_message.config(text=str(elo)+" elo")
        stars_message.config(text=str(stars)+" stars")
        moons_message.config(text=str(moons)+" moons")
        secret_coins_message.config(text=str(secret_coins)+" secret coins")
        user_coins_message.config(text=str(user_coins)+" user coins")
        easy_demons_message.config(text=str(easy_demons)+" easy demons")
        medium_demons_message.config(text=str(medium_demons)+" medium demons")
        hard_demons_message.config(text=str(hard_demons)+" hard demons")
        insane_demons_message.config(text=str(insane_demons)+" insane demons")
        extreme_demons_message.config(text=str(extreme_demons)+" extreme demons")
        list_points_message.config(text=str(list_points)+" list points")
    except:
        # the user does not exist in this case
        print("The user does not exits")
        username_message.config(text="This user does not exist")
        stars_message.config(text="")
        moons_message.config(text="")
        secret_coins_message.config(text="")
        user_coins_message.config(text="")
        easy_demons_message.config(text="")
        medium_demons_message.config(text="")
        hard_demons_message.config(text="")
        insane_demons_message.config(text="")
        extreme_demons_message.config(text="")
# Credit to Bro Code: https://www.youtube.com/watch?v=lyoyTlltFVU
# Also credit to w3schools https://www.geeksforgeeks.org/python/python-tkinter-tutorial/

window = tk.Tk() # intiate instance of window
window.geometry("1280x720")
window.title("Geometry Dash ELO System")

icon = tk.PhotoImage(file=BASE_PATH / "assets" / "gd_elo.png")
window.iconphoto(True, icon)
#window.config(bg="black")

main_label = tk.Label(window, text="Geometry Dash ELO System\nSearch for a Player")
main_label.pack()

search_text = tk.Entry(window, text="Look up a player!")
search_text.pack()

search_button = tk.Button(window, text="Search!", command=search, cursor="hand2")
search_button.pack()

# Messages
username_message = tk.Message(window, text="", width="200")
elo_message = tk.Message(window, text="", width="200")
stars_message = tk.Message(window, text="", width="200")
moons_message = tk.Message(window, text="", width="200")
secret_coins_message = tk.Message(window, text="", width="200")
user_coins_message = tk.Message(window, text="", width="200")
easy_demons_message = tk.Message(window, text="", width="200")
medium_demons_message = tk.Message(window, text="", width="200")
hard_demons_message = tk.Message(window, text="", width="200")
insane_demons_message = tk.Message(window, text="", width="200")
extreme_demons_message = tk.Message(window, text="", width="200")
list_points_message = tk.Message(window, text="", width="200")

username_message.pack()
elo_message.pack()
stars_message.pack()
moons_message.pack()
secret_coins_message.pack()
user_coins_message.pack()
easy_demons_message.pack()
medium_demons_message.pack()
hard_demons_message.pack()
insane_demons_message.pack()
extreme_demons_message.pack()
list_points_message.pack()

window.mainloop()
