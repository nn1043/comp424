global sequence_1
sequence_1 = ["This ", "is ", "a ", "list."]
sequence_2 = ["1","2","3","4","5"]
sequence_3 = ["1 2 3 ", "Four ", "5"]

def main():
    run_program = True
    while run_program is True:
        print("Please choose an operation:")
        print("MENU")
        user_response = input("Operation: ")
        if user_response.upper() == "MENU":
            print("View Sequences (VIEW)")
            print("Concatenation (CONCAT)")
            print("Quit Program (QUIT)")
        elif user_response.upper() == "VIEW":
            print(sequence_1)
            print(sequence_2)
            print(sequence_3)
        elif user_response.upper() == "CONCAT":
            concatenation()
        elif user_response.upper() == "EXIT":
            print("Goodbye.")
            run_program = False
        elif user_response.upper() == "QUIT":
            print("Goodbye.")
            run_program = False
        else:
            print("Not a valid command.")
            
def concatenation():
    use_sequence = input("Choose a sequence (1, 2, 3): ")
    if use_sequence == "1":
        real_answer = "".join(sequence_1)
        print(sequence_1)
    elif use_sequence == "2":
        real_answer = "".join(sequence_2)
        print(sequence_2)
    elif use_sequence == "3":
        real_answer = "".join(sequence_3)
        print(sequence_3)
    print("What would this sequence produce if .join() was used?")
    user_answer = input()
    if user_answer == real_answer:
        print("Correct.")
    else:
        print("Incorrect. The correct answer is:")
        print(real_answer)
#def split():

main()
