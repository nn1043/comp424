global player
player = {"name": ""}


def user_interface():
    menu_list = {
        "MENU": print_menu, "START": start_game
        }
    print("Please choose an operation:")
    print("MENU")
    run_program = True
    while run_program is True:
        user_response = input("Input: ")
        if user_response.upper() in menu_list:
            if type(menu_list[user_response.upper()]) is list:
                for to_do in menu_list[user_response.upper()]:
                    to_do()
            else:
                menu_list[user_response.upper()]()
        elif user_response.upper() in ["EXIT", "QUIT"]:
            print("Goodbye.")
            run_program = False
        else:
            print("Not a valid command.")


def print_menu():
    print("Start a new game: START")
    print("Exit program: EXIT or QUIT")


def start_game():  # For debug purposes, this is not the initial function.
    run_program = True
    while run_program is True:
        user_response = input("New Game or Continue: ")
        response_upper = user_response.upper()
        if response_upper == "NEW GAME":
            create_character()
            run_program = False
        elif response_upper == "CONTINUE":
            load_character()
            run_program = False
        else:
            print("Invalid input.")


def create_character():
    char_name = input("Choose a name for your character: ")
    filename = char_name + ".txt"
    file = open(filename, "w+")
    file.write(char_name + ",default")
    file.close()
    game_menu()


def load_character():
    char_name = input("What character are you playing: ")
    filename = char_name + ".txt"
    file = open(filename, "r")
    for line in file.readlines():
        loading = line.split(",")
        for info in loading:
            if loading.index(info) == 0:
                player["name"] = info
    print(player)


def game_menu():
    print("This is the main menu.")


user_interface()
