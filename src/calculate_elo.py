from fetch_server_data import get_data_by_name

def calculate_elo(name):
    data = get_data_by_name(name)
    rating = 0
    rating += int(data["stars"])
    rating += int(data["moons"])
    rating += 3*int(data["secretCoins"])
    rating += 3*int(data["usercoins"])
    demons = data["demons"]
    total_demons = 0;
    # Imma have to write a function to parse this for some reason (or not I can always just write it locally
    demons = demons.split(",")
    for i in range(10):
        total_demons += int(demons[i])
    rating += 10*int(total_demons)
    rating += 10*int(demons[0]) + 10*int(demons[5])
    rating += 20*int(demons[1]) + 20*int(demons[6])
    rating += 40*int(demons[2]) + 40*int(demons[7])
    rating += 80*int(demons[3]) + 80*int(demons[8])
    rating += 160*int(demons[4]) + 160*int(demons[9])
    return rating
