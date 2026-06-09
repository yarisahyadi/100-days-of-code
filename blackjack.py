import random
# import art

def pick_player_cards(player, card_list, score):
    player_card = random.choice(card_list)
    cards_picked[player].append(player_card)
    score += player_card
    return score

def is_blackjack(score):
    if score == 21:
        return True
    
def choose_winner(player1_score, player2_score):
    if player1_score > player2_score or player2_score > 21:
        print("You win 😃")
    elif player2_score > player1_score:
        print("You lose 😤")
    elif player1_score == player2_score:
        print("Draw")

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
    print("art.logo")

    cards_picked = {
        "user": [],
        "computer": []
    }
    user_score = 0
    computer_score = 0

    for card in range(2):
        user_score = pick_player_cards("user", cards, user_score)
        computer_score = pick_player_cards("computer", cards, computer_score)

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
            user_score = pick_player_cards("user", cards, user_score)
            display_result()
            if user_score > 21:
                display_final_result()
                print("Yow went over. You lose 😭")
                draw_card = "n"
            else:
                draw_card = str(input("Type \'y\' to get another card, type \'n\' to pass: "))

        while computer_score < 17:
            computer_score = pick_player_cards("computer", cards, computer_score)

        if user_score <= 21:
            display_final_result()
            choose_winner(user_score, computer_score)

    play = str(input("\nDo you want to play a game of Blackjack? Type \'y\' or \'n\': "))
