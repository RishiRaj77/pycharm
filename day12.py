


import random
def deal_cards():
    """" return the random card from deck """""
    cards = [ 11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    cards = random.choice(cards)
    return cards

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #cards [1,2,3] = 5 print karega
    if 11 in cards and sum(cards) > 21:
        cards.remove(11) # remove
        cards.append(1) # add
    return sum(cards) # 2 cards ka addition karega

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "draw"
    elif user_score == 0:
        return "win with blackjack"
    elif user_score>21:
        return " you loose "
    elif computer_score>21:
        return " you win "
    else:
        return "loser"

user_cards = []
computer_cards = []
is_game_over = False
for _ in range(2): # need nahi hai varible ka 2 baar run karna hai isliye _ diya hai

    user_cards.append(deal_cards())      # The append() method appends an element to the end of the list
    computer_cards.append(deal_cards())

while not is_game_over: # for user

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" your cards {user_cards} and current score is {user_score}")
    print(f" computer first card {computer_cards[0]}")


    if user_score == 0 or computer_score ==0 or user_score > 21:
        is_game_over = True
    else:
        card_need=input(" y for new card n for no need of card ")
        if card_need == " y ":
            user_cards.append(deal_cards())
        else:
            is_game_over == True


while computer_score != 0 and computer_score < 17: # for computer
    computer_cards.append(deal_cards())
    computer_score = calculate_score(computer_cards)

print(compare(user_score,computer_score))


