from fetch_server_data import get_data_by_name
from calculate_elo import calculate_elo
from fetch_aredl_data import get_list_points

def parse_input(input):
    parsed_input = input.split(" ")
    return parsed_input

running = True
while running:
    user_input = input("$ ")
    parsed_input = parse_input(user_input)
    if parsed_input[0] == "exit":
        running = False
    elif parsed_input[0] == "help":
        print("Search player:\n\n  search <player name> <optional specific information you want>")
        print("    For example: \"search EthanCubes stars\" returns the amount of stars EthanCubes has")
        print("    For example: \"search EthanCubes\" returns all the data on EthanCubes in a dictionary")
        print("\n")
        print("Other commands:\n\n  help\n    Opens this help page\n\n  exit\n    Exits the program")
    elif parsed_input[0] == "search":
        key = ""
        if len(parsed_input) > 2:
            key = parsed_input[2]
        if len(parsed_input) > 1:
            name = parsed_input[1]
            data = get_data_by_name(name)
            if key != "":
                try:
                    key_fetched_data = data[key]
                    print(key_fetched_data)
                except KeyError:
                    if key == "elo":
                        print(calculate_elo(name))
                    elif key == "list_points":
                        print(get_list_points(name))
                    else:
                        print(f"Invalid key: {key}")
                except:
                    print("Key does not exist, or you are not connected to the internet")
            else:
                print(data)
        else:
            print("Usage: search <name> <modifier>")
    else:
        print(f"Invalid command: {parsed_input[0]}")
