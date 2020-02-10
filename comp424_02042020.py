in_use_seq = []
sequences = {}
dict_counter = 0

def main():
    run_program = True
    while run_program is True:
        print("Please choose an operation:")
        print("MENU")
        user_response = input("Operation: ")
        if user_response.upper() == "MENU":
            print("View Sequences (VIEW)")
            print("Add / Clear Sequences (ADD)")
            print("Concatenation (CONCAT)")
            print("Split (SPLIT)")
            print("Quit Program (QUIT)")
        elif user_response.upper() == "VIEW":
            for i in sequences:
                print(sequences[i])
        elif user_response.upper() == "ADD":
            add_sequence()
        elif user_response.upper() == "CONCAT":
            concatenation()
        elif user_response.upper() == "SPLIT":
            split()
            #I'm realizing split() is a bad name for a function, given that
            #it already exists as a built-in Python function. Will fix once
            #I think of a better name.
        elif user_response.upper() == "EXIT":
            print("Goodbye.")
            run_program = False
        elif user_response.upper() == "QUIT":
            print("Goodbye.")
            run_program = False
        else:
            print("Not a valid command.")

def add_sequence():
    print("Type 'DONE' when complete.")
    print("Type 'CLEAR' to delete all sequences in memory.")
    print(
        "Usage: Inputs will have blank spaces stripped. A number will " +
        "be assigned to the sequence automatically so that it can be " +
        "called at a later point in time."
        )
    #This is a bug caused by line 60 below, used to split the input so that it
    #can be used by the concatenation() function below. Ironically, this might
    #make it work better for split(), although I haven't tried it yet.
    adding_seq = True
    while adding_seq is True:
        to_add = input()
        if to_add.upper() == "DONE":
            adding_seq = False
        elif to_add.upper() == "CLEAR":
            global sequences
            global dict_counter
            sequences = {}
            dict_counter = 0
        else:
            to_dict = to_add.split()
            sequences[dict_counter] = to_dict
            dict_counter = dict_counter + 1
            print(sequences)

def choose_sequence():
    user_response = input("Choose a sequence (integer): ")
    use_sequence = int(user_response)
    if use_sequence in sequences:
        global in_use_seq
        in_use_seq = sequences[use_sequence]
        print(in_use_seq)
    else:
        in_use_seq = []
        print("Not a valid sequence.")

def concatenation():
    choose_sequence()
    global in_use_seq
    if in_use_seq == []:
        return
    real_answer = "".join(in_use_seq)
    print("What would this sequence produce if .join() was used?")
    user_answer = input()
    if user_answer == real_answer:
        print("Correct.")
    else:
        print("Incorrect. The correct answer is:")
        print(real_answer)

def split():
    """
    This might still work as is, haven't tested it yet.

    choose_sequence()
    if in_use_seq == []:
        return
    """
    in_use_seq = ["This ", "is ", "a ", "list."]
    present_seq = "".join(in_use_seq)
    print(present_seq)
    print("How do you want to split() this sequence?")
    split_at = input()
    temp = present_seq.split(split_at)
    real_answer = "".join(temp)
    print("What would this sequence produce if .split() was used as entered?")
    user_answer = input()
    if user_answer == real_answer:
        print("Correct.")
    else:
        print("Incorrect. The correct answer is:")
        print(real_answer)

main()
