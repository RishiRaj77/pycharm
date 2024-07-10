import random

easy_level = 10
hard_level = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high!")
        return turns - 1
    elif guess < answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You guessed the correct answer: {answer}")

def set_difficulty():
    level = input("Choose the level: 'hard' or 'easy': ")
    if level == "easy":
        return easy_level
    else:
        return hard_level

answer = random.randint(1, 100)
print(f"The answer is: {answer}")

turns = set_difficulty()

while turns > 0:
    print(f"You have {turns} turns left.")
    guess = int(input("Make a guess: "))

    turns = check_answer(guess, answer, turns)

    if turns == 0:
        print("Game over! You ran out of turns.")
        break
    elif guess != answer:
        print("Guess again!\n")

print("Thanks for playing!")
