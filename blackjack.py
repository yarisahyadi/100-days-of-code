import random
import art

def pick_user_cards(card_list, score):
    user_card = random.choice(card_list)
    cards_picked["user"].append(user_card)
    score += user_card
    return score

def pick_computer_cards(card_list, score):
    computer_card = random.choice(card_list)
    cards_picked["computer"].append(computer_card)
    score += computer_card
    return score

def choose_winner(user_score, computer_score):
    if user_score > computer_score and user_score <= 21:
        result = "User"
    elif computer_score > user_score and computer_score <= 21:
        result = "Computer"
    elif user_score == computer_score:
        result = "Draw"
    return result

def is_blackjack(score):
    if score == 21:
        return True

def display_result():
    print(f"Your cards: {cards_picked['user']}, current score: {user_score}")
    print(f"Computer's first card: {cards_picked['computer'][0]}")

def display_final_result():
    print(f"Your final hand: {cards_picked['user']}, final score: {user_score}")
    print(f"Computer's final hand: {cards_picked['computer']}, final_score: {computer_score}")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = str(input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': "))
while play == "y":
    print("\n" * 50)
    print(art.logo)

    cards_picked = {
        "user": [],
        "computer": []
    }
    user_score = 0
    computer_score = 0

    for card in range(2):
        user_score = pick_user_cards(cards, user_score)
        computer_score = pick_computer_cards(cards, computer_score)

    # print(f"Your cards: {cards_picked['user']}, current score: {user_score}")
    # print(f"Computer's first card: {cards_picked['computer'][0]}")
    display_result()

    if is_blackjack(user_score):
        # print(f"Your final hand: {cards_picked['user']}, final score: {user_score}")
        # print(f"Computer's final hand: {cards_picked['computer']}, final_score: {computer_score}")
        display_final_result()
        print("Win with a Blackjack 😎")
    else:
        draw_card = str(input("Type \'y\' to get another card, type \'n\' to pass: "))
        while draw_card == "y":
            user_score = pick_user_cards(cards, user_score)
            display_result()
            if user_score > 21:
                display_final_result()
                print("Yow went over. You lose 😭")
                draw_card = "n"
            else:
                draw_card = str(input("Type \'y\' to get another card, type \'n\' to pass: "))

        while computer_score < 21:
            computer_score = pick_computer_cards(cards, computer_score)

        display_final_result()
        if choose_winner(user_score, computer_score) == "User":
            print("You win 😃")
        elif choose_winner(user_score, computer_score) == "Computer":
            print("You lose 😤")
        else:
            print("Draw")

    play = str(input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': "))
