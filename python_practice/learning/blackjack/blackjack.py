import blackjack_art as a
import random as r

cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
player_hand_end = False
dealer_hand_end = False


def play():
    to_play = input(
        "Would you like to play a game of blackjack? Type 'y' or 'n': ").lower()
    if to_play == 'n':
        print("Good bye!")
    elif to_play == 'y':
        blackjack()


def deal_card():
    card = r.choice(cards)
    return card


def calculate_score(hand):
    score_hand = []
    for card in hand:
        if card in ('J', 'Q', 'K'):
            score_hand.append(10)
        elif card == 'A':
            score_hand.append(11)
        else:
            score_hand.append(card)

    score = sum(score_hand)
    if 11 in score_hand and score > 21:
        ace_count = score_hand.count(11)
        score -= 10 * ace_count
    return score


def start_game(hand):
    for _ in range(2):
        hand.append(deal_card())


def final_hand(p_hand, p_score, d_hand, d_score):
    print(
        f"  This is your final hand: {p_hand}. Your score was: {p_score}.")
    print(
        f"  This is the dealer's hand:{d_hand}. The Dealer's score was {d_score}.")


def blackjack():
    player_hand_end = False
    dealer_hand_end = False
    player_hand = []
    dealer_hand = []
    print(a.logo)
    start_game(player_hand)
    start_game(dealer_hand)
    print(
        f"  This is your hand: {player_hand}. Your score is {calculate_score(player_hand)}")
    print(f"    This is the dealer's first card: {dealer_hand[0]}")

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if player_score == 21 and dealer_score == 21:
        player_hand_end = True
        dealer_hand_end = True
        print(" It's a tie.")
        final_hand(player_hand, player_score, dealer_hand, dealer_score)
    elif player_score == 21:
        player_hand_end = True
        dealer_hand_end = True
        print(" Congrats you won!")
        final_hand(player_hand, player_score, dealer_hand, dealer_score)
    elif dealer_score == 21:
        player_hand_end = True
        dealer_hand_end = True
        print(" You Lose. The Dealer wins.")
        final_hand(player_hand, player_score, dealer_hand, dealer_score)

    while not player_hand_end:
        another_card = input("Would you like a hit? (Y/N) ").lower()
        if another_card == 'y':
            player_hand.append(deal_card())
            player_score = calculate_score(player_hand)
            dealer_score = calculate_score(dealer_hand)
            if player_score > 21:
                player_hand_end = True
                print(" You Lose. The Dealer wins.")
                final_hand(player_hand, player_score,
                           dealer_hand, dealer_score)
            else:
                print(
                    f"  This is your hand: {player_hand}. Your score is: {player_score}")
                print(f"    This is the dealer's first card: {dealer_hand[0]}")
        else:
            player_hand_end = True
            dealer_score = calculate_score(dealer_hand)
            while not dealer_hand_end:
                player_score = calculate_score(player_hand)
                dealer_score = calculate_score(dealer_hand)
                if dealer_score < 17:
                    dealer_hand.append(deal_card())
                elif dealer_score > 21:
                    dealer_hand_end = True
                    print(" You win.")
                    final_hand(player_hand, player_score,
                               dealer_hand, dealer_score)
                elif dealer_score > player_score:
                    dealer_hand_end = True
                    print(" You lose.")
                    final_hand(player_hand, player_score,
                               dealer_hand, dealer_score)
                elif dealer_score < player_score:
                    dealer_hand_end = True
                    print(" You win.")
                    final_hand(player_hand, player_score,
                               dealer_hand, dealer_score)
                elif dealer_score == player_score:
                    dealer_hand_end = True
                    print("You tie.")
                    final_hand(player_hand, player_score,
                               dealer_hand, dealer_score)
    to_play = input(
        "Would you like to play a game of blackjack? Type 'y' or 'n': ").lower()
    if to_play == 'n':
        print("Good bye!")
    elif to_play == 'y':
        player_hand_end = False
        dealer_hand_end = False
        player_hand = []
        dealer_hand = []
        blackjack()


play()
