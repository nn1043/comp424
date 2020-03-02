# I need to make a list of saved / valid .txt files and make to globally
# available, otherwise I'm gonna have a bad time. Probably a global 'in_use'
# file too, check word_manipulation.py, it might have an answer to that.


def user_interface():
    menu_list = {
        "MENU": print_menu, "NEW": new_text, "READ": read_text,
        "SAVE": save_text
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
    print("Write a new text file: NEW")
    print("Read a saved text file: READ")
    print("Overwrite a saved text file: SAVE")
    print("Exit program: EXIT or QUIT")


def new_text():
    filename_counter = ""  # Will make a better name function in full version.
    filename_counter = input("Filename? 1, 2, 3: ")
    filename_counter = filename_counter + ".txt"
    file = open(filename_counter, "w+")
    file.write("This is a file written by Python")
    file.write(",Use a comma to create a simple CSV.")
    print("new_text() done.")


def read_text():
    to_open = input("Which file do you want to load: ")
    to_open = to_open + ".txt"
    file = open(to_open, "r")
    print(file.read())


def save_text():
    filename = input("Which file do you want to overwrite: ")
    to_open = filename + ".txt"
    file = open(to_open, "w")
    file.write("This file has been overwritten.")
    print("save_text() done.")


user_interface()
