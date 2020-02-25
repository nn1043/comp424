def user_interface():
    options = {
        "MENU" : print_menu, "TEST" : test_1, "OPTIONS": opt
    }
    print("Please choose an operation:")
    print("MENU")
    run_program = True
    while run_program is True:
        user_response = input("Input: ")
        if user_response.upper() in options:
            options[user_response.upper()]()
        elif user_response.upper() == "EXIT":
            print("Goodbye.")
            run_program = False
        elif user_response.upper() == "QUIT":
            print("Goodbye.")
            run_program = False
        else:
            print("Not a valid command.")

def print_menu():
    print("print menu")

def test_1():
    print("test 1")

def opt():
    print("options")

user_interface()
