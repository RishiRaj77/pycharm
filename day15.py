import random

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },

    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'india'
    },
    {
        'name': 'Ronaldo',
        'follower_count': 15,
        'description': 'Footballer',
        'country': 'brazil'
    },
    {
        'name': 'Cris',
        'follower_count': 21,
        'description': 'actor',
        'country': 'nagaland'
    },
    {
        'name': 'Neymar',
        'follower_count': 190,
        'description': 'Footballer',
        'country': 'brazil'
    },
]

def account_format(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    print(f" {account_name}, a {account_desc}, from {account_country}")

def check_answer(guess, account_a, account_b):
    if account_a["follower_count"] > account_b["follower_count"]:
        return guess.lower() == "a"
    else:
        return guess.lower() == "b"

def game():
    account_a = random.choice(data)
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {account_format(account_a)}")
    print(f"Compare B: {account_format(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ")

    correct = check_answer(guess, account_a, account_b)
    if correct:
        print("You're right!")
    else:
        print("Sorry, that's wrong.")

game()