"""
comp424_02032020.py
This Python file allows users to test their understanding of Python string
methods in a closed environment.
Nicholas Noboa
Created 2/4/20
Updated 2/17/20
"""

in_use_seq = []
sequences = {}
dict_counter = 0


def main():
    """
This is the main function that runs when the program is started. It acts as the
user interface and allows the user to access relavant functions.
    """
    run_program = True  # This function is based off of task_manager() from
    while run_program is True:  # word_manipulation.py, written by myself.
        print("Please choose an operation:")
        print("MENU")
        user_response = input("Operation: ")
        if user_response.upper() == "MENU":
            print("View Sequences (VIEW)")
            print("Add / Clear Sequences (ADD)")
            print("Make String Uppercase (UPPER)")
            print("Make String Lowercase (LOWER)")
            print("Concatenation (CONCAT)")
            print("Split (SPLIT)")
            print("Quit Program (QUIT)")
        elif user_response.upper() == "VIEW":
            for i in sequences:
                print(sequences[i])
        elif user_response.upper() == "ADD":
            add_sequence()
        elif user_response.upper() == "UPPER":
            make_uppercase()
        elif user_response.upper() == "LOWER":
            make_lowercase()
        elif user_response.upper() == "CONCAT":
            concatenation()
        elif user_response.upper() == "SPLIT":
            make_split()
        elif user_response.upper() == "EXIT":
            print("Goodbye.")
            run_program = False
        elif user_response.upper() == "QUIT":
            print("Goodbye.")
            run_program = False
        else:
            print("Not a valid command.")


def add_sequence():
    """
This function allows the user to input their own sequences, which are then
stored as a list within a dictionary. This method allows the user to later call
the desired sequence with the key, which, for the sake of simplicity, is an
automatically assigned integer.
    """
    print("Type 'DONE' when complete.")
    print("Type 'CLEAR' to delete all sequences in memory.")
    print(
        "Usage: Inputs will have blank spaces stripped. A number will " +
        "be assigned to the sequence automatically so that it can be " +
        "called at a later point in time."
        )
    adding_seq = True
    while adding_seq is True:
        to_add = input()
        if to_add.upper() == "DONE":
            adding_seq = False
        elif to_add.upper() == "CLEAR":
            global sequences  # I'm sure this isn't the best usage of global,
            global dict_counter  # however for some reason this was the only
            sequences = {}  # way I could get it to take it rather than see
            dict_counter = 0  # it as a local variable.
        else:
            to_dict = to_add.split()  # This originally caused a bug that made
            sequences[dict_counter] = to_dict  # everything appear as one long
            dict_counter = dict_counter + 1  # string, when later used. This
            print(sequences)  # was fixed by reiterating through and manually
#                                adding spaces back in.


def choose_sequence():
    """
This function is used by every string method function to properly grab the
correct sequence for use. This function is separate mostly to prevent
unecessary repetition of code.
    """
    user_response = input("Choose a sequence (integer): ")
    use_sequence = int(user_response)  # A bug exists where program will crash
    if use_sequence in sequences:      # if the user doesn't input an integer.
        global in_use_seq
        in_use_seq = sequences[use_sequence]
        print(in_use_seq)
    else:
        in_use_seq = []  # Exception handler.
        print("Not a valid sequence.")


def make_uppercase():
    """
This function takes the desired test sequence and applies .upper() to it, and
tests to see if the user's input response matches.
    """
    choose_sequence()
    global in_use_seq  # Again, I broke something and needed to reissue the
    if in_use_seq == []:  # global parameter in order to avoid using a local
        return  # variable instead. No idea what caused it.
    upper_str = ""
    for word in in_use_seq:
        if upper_str == "":  # This puts the sequence back together with
            upper_str = word  # spaces.
        else:
            upper_str = upper_str + " " + word
# The below portion is echoed by every string method function. There's probably
# some way to make this a reusable function.
    real_answer = upper_str.upper()
    print("What would this sequence produce if .upper() was used?")
    user_answer = input()
    if user_answer == real_answer:  # Simple comparator.
        print("Correct.")
    else:
        print("Incorrect. The correct answer is:")
        print(real_answer)


def make_lowercase():
    """
This function takes the desired test sequence and applies .lower() to it, and
tests to see if the user's input response matches. Functions almost identical
to make_uppercase().
    """
    choose_sequence()
    global in_use_seq
    if in_use_seq == []:
        return
    lower_str = ""
    for word in in_use_seq:
        if lower_str == "":
            lower_str = word
        else:
            lower_str = lower_str + " " + word
    real_answer = lower_str.lower()
    print("What would this sequence produce if .lower() was used?")
    user_answer = input()
    if user_answer == real_answer:
        print("Correct.")
    else:
        print("Incorrect. The correct answer is:")
        print(real_answer)
# This ended up being practically the same thing as make_uppercase(), with the
# exception of the change between the word upper and lower. Not my intent when
# originally planning this out. Probably could have made this one function with
# a boolean determining an if statement between .upper() and .lower(), based on
# the user input from main(). If I have time I might change that.


def concatenation():
    """
This function takes the desired test sequence and applies .join() to it, and
tests to see if the user's input response matches.
    """
    choose_sequence()  # This was the first function I wrote, with the rest of
    global in_use_seq  # the design drawing from how this one works. Not really
    if in_use_seq == []:  # important, just a design philosophy I noticed.
        return
    real_answer = "".join(in_use_seq)
    print("What would this sequence produce if .join() was used?")
    user_answer = input()
    if user_answer == real_answer:
        print("Correct.")
    else:
        print("Incorrect. The correct answer is:")
        print(real_answer)


def make_split():
    """
This function takes the desired test sequence and applies .split() to it, and
tests to see if the user's input response matches. The user designates where to
.split() the string, so as to emulate a programmer or function splitting a
string.
    """
    choose_sequence()
    global in_use_seq
    if in_use_seq == []:
        return
    prep_str = ""  # This idea from make_uppercase() fixed an earlier bug that
    for word in in_use_seq:  # made it impossible to use user-inputted
        if prep_str == "":  # sequences.
            prep_str = word
        else:
            prep_str = prep_str + " " + word
    print(prep_str)
    print("How do you want to split() this sequence?")
    split_at = input()
    temp = prep_str.split(split_at)  # Since the string is split into a list,
    real_answer = "".join(temp)  # I have to then remake the string.
    print("What would this sequence produce if .split() was used as entered?")
    user_answer = input()
    if user_answer == real_answer:
        print("Correct.")
    else:
        print("Incorrect. The correct answer is:")
        print(real_answer)


main()
