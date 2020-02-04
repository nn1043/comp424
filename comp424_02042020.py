global in_use_seq
sequences = {
    "1":["This ", "is ", "a ", "list."],
    "2":["1","2","3","4","5"],
    "3":["1 2 3 ", "Four ", "5"]
    }

def main():
    run_program = True
    while run_program is True:
        print("Please choose an operation:")
        print("MENU")
        user_response = input("Operation: ")
        if user_response.upper() == "MENU":
            print("View Sequences (VIEW)")
            print("Concatenation (CONCAT)")
            print("Split (SPLIT)")
            print("Quit Program (QUIT)")
        elif user_response.upper() == "VIEW":
            for i in sequences:
                print(sequences[i])
        elif user_response.upper() == "CONCAT":
            concatenation()
        elif user_response.upper() == "SPLIT":
            split()
        elif user_response.upper() == "EXIT":
            print("Goodbye.")
            run_program = False
        elif user_response.upper() == "QUIT":
            print("Goodbye.")
            run_program = False
        else:
            print("Not a valid command.")

def choose_sequence():
    use_sequence = input("Choose a sequence (1, 2, 3): ")
    if use_sequence in sequences:
        in_use_seq = sequences[use_sequence]
        print(in_use_seq)
    else:
        in_use_seq = []
        print("Not a valid sequence.")

def concatenation():
    choose_sequence()
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
