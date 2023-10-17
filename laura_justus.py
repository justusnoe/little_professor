import random

# Global variables:
N = 10  # Number of problems
T = 3   # Maximum number of tries

def main():
    # Step 1: Get the user's selected level
    level = get_level()  # Calls the get_level function to get the user's chosen level
    count_correct = 0    # Initialize the count of correct answers

    for i in range(N):
        # Step 2: Create a math problem
        prompt, correct_answer = generate_prompt(level)
        
        # Step 3: Prompt the user for an answer, with up to T tries
        correct = get_answer(prompt, correct_answer, T)
        
        # Step 4: Update the count of correct answers or provide the correct answer
        if correct:
            count_correct += 1
        else:
            print(prompt + " " + str(correct_answer))
    
    # Step 5: Print the user's score
    print("Score:", count_correct)

# Input: void
# Output: integer (user-provided integer between 1 and 3)
def get_level():
    while True:
        try: 
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass
       
# Input: integer (level)
# Output: string (prompt for the user, e.g., '3 + 8 = '), integer (correct answer, e.g., 11)
def generate_prompt(level):
    # Step 2.1: Generate random numbers X and Y based on the chosen level
    X = generate_integer(level)
    Y = generate_integer(level)
    # Step 2.2: Create a prompt for the user, e.g., '3 + 8 = '
    prompt = f"{X} + {Y} = "
    # Step 2.3: Calculate the correct answer
    correct_answer = X + Y
    return prompt, correct_answer

# Input: integer (level)
# Output: integer (random number between 0 and 9, 10 and 99, or 100 and 999)
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

# Input: string (prompt for user), integer (correct answer), integer (T = maximum number of tries)
# Output: boolean (True if the answer is correct within T tries, False otherwise)
def get_answer(prompt, n, T):
    tries = 0
    while tries < T:
        try:
            user_answer = int(input(prompt))
            if user_answer == n:
                # Step 3.1: Correct answer
                return True
            else:
                # Step 3.2: Incorrect answer, display 'EEE'
                print("EEE")
                tries += 1
        except ValueError:
            # Step 3.3: Invalid input, display 'EEE'
            print("EEE")
            tries += 1
    # Step 3.4: User couldn't answer correctly within T tries, provide the correct answer
    return False  # User couldn't answer correctly within T tries

# Main
if __name__ == "__main__":
    main()
