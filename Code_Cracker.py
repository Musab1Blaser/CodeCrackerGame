import random

status = {"match": 'o', "partial": '-', "incorrect": 'x'}
digits = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

# Makes our output more appealing
# Only use if terminal supports emojis
# status = {"match": '🟩', "partial": '🟨', "incorrect": '🟥'}
# digits = {0: "0️⃣ ", 1: "1️⃣ ", 2: "2️⃣ ", 3: "3️⃣ ", 4: "4️⃣ ", 5: "5️⃣ ", 6: "6️⃣ ", 7: "7️⃣ ", 8: "8️⃣ ", 9: "9️⃣ "}

# Converts a list of numbers into a list of emojis as per the digits dictionary
def emoji_num(num):
    global digits
    return [digits[digit] for digit in num]

# Input and Validate difficulty - Must be integer and between 3 and 10 (inclusive)
def get_difficulty():
    valid = False

    while not valid:
        difficulty = input("What difficulty would you like to play at (3-10)? ").strip()
        if not difficulty.isnumeric():
            print("Difficulty is not a valid integer. Please re-enter.")
        elif int(difficulty) < 3 or int(difficulty) > 10:
            print("Difficulty must be between 3 and 10. Please re-enter.")
        else:
            valid = True

    return int(difficulty)

# Generates a List of Digits that make up our code (no repeating digits)
def generate_code():
    difficulty = get_difficulty()
    nums = range(10) #(0,1,2,3,....,8,9)
    code = random.sample(nums, difficulty)
    return code

# Lets the User take an attempt at guessing the code
def attempt(code):
    guess = get_guess(code)
    result, flag = evaluate_attempt(guess, code)

    # Show stylised output
    print("".join(emoji_num(guess)))
    print("".join(result))
    print()

    return flag

# Validate guess - must be integer and exactly as long as the code
def get_guess(code):
    valid = False
    while not valid:
        guessStr = input("What is your guess: ").strip()
        if not guessStr.isnumeric():
            print("Guess should be made up of digits only. Please re-enter.")
        elif len(guessStr) != len(code):
            print(f"Your guess should have exactly {len(code)} digits. Your current guess had {len(guessStr)} ({'too short' if len(guessStr) < len(code) else 'too long'}). Please re-enter.")
        else:
            valid = True

    # Convert the guess string into a list of digits for comparison with code
    guess = []
    for digit in guessStr:
        guess.append(int(digit))
    return guess

# Checks which digits matched completely, partially or were incorrect - returns stylised output and flag denoting victory status 
def evaluate_attempt(guess, code):
    global status
    result = []
    flag = True

    for idx in range(len(guess)):
        if guess[idx] == code[idx]:
            result.append(status["match"])

        elif guess[idx] in code:
            result.append(status["partial"])
            flag = False # guess does not completely match code

        else:
            result.append(status["incorrect"])
            flag = False # guess does not completely match code

    return result, flag

# Manages Game State
def play_game():
    code = generate_code()
    print(f"Code is {len(code)} digits long")

    # Manages attempts
    attempts = 10
    flag = False
    while attempts > 0:
        print("Attempts remaining:", attempts)
        flag = attempt(code)
        attempts -= 1

        if flag:
            break

    if flag: # Victory State
        print(f"YOU WON with {attempts} attempts remaining!")
    else: # Game Over State
        print("You ran out of attempts :(")
        print(f"The code was {''.join(emoji_num(code))}")

play_game()
