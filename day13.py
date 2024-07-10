
import random

easy_level = 10
hard_level = 5
def check_answer(guess,answer,turns):
    if guess > answer:
        print("to high")
        return  turns -1
    elif guess < answer:
        print("to less")
        return  turns -1
    else:
        print(f" You guess correct answer : {answer}")
def set_difficulties():
    level = input(" chose the level hard or easy :  ")
    if level == "easy":
        return easy_level
    else :
        return hard_level


answer = random.randint(1,100)
print(f" the answer :  {answer}")

turns = set_difficulties()

guess= 0
while guess != answer:
    print(f" you have only {turns} turns left")
    guess= int(input("make a guess : "))
    turns = check_answer(guess,answer,turns)
