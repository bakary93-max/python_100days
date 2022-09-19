import random

from replit import clear


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards_list):
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose opponent score has Blackjack "
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose..😒"
    elif computer_score > 21:
        return "Opponent went over. You win..😀😀"
    elif user_score > computer_score:
        return "You win 😀😀"
    else:
        return "You lose"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"computer_car {computer_cards[0]}")
        print(f"user_card {user_cards} your score {user_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Tape 'y' to get another or tape 'no' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is {user_cards}, final score {user_score}")
    print(f"Computer final hand is {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))


while input("Tape 'y' to start another game or 'no' to exit: ") == 'y':
    clear()
    play_game()
