import random
from utilities.art import blackjack_logo
# Game logic: The dealer should keep drawing cards if their total is below 17,
# and the player should be able to continue drawing cards until they choose to stand or their hand exceeds 21.


def play_blackjack():
    print(blackjack_logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player = Player("Player")
    dealer = Player("Dealer")

    dealer.get_a_card(cards)

    player.get_a_card(cards)
    player.get_a_card(cards)

    while sum(player.hand) < 21:
        user_action = input("Hit or Stand (hit/stand)?\n")
        if user_action == "hit":
            player.get_a_card(cards)
        else:
            print(f"THE PLAYER HAS {sum(player.hand)}\n")
            break

    dealer.get_a_card(cards)
    while sum(dealer.hand) < 17:
        dealer.get_a_card(cards)
    print(f"THE DEALER HAS {sum(dealer.hand)}\n")

    print(f"THE PLAYER HAS {sum(player.hand)} and THE DEALER HAS {sum(dealer.hand)}")

    if (sum(player.hand) > 21 and sum(dealer.hand) > 21) or sum(player.hand) == sum(dealer.hand):
        print("Draw!")
    elif sum(player.hand) > 21 >= sum(dealer.hand):
        print("You loose!")
    elif sum(player.hand) <= 21 < sum(dealer.hand):
        print("You win!")
    else:
        if sum(player.hand) < sum(dealer.hand):
            print("You loose!")
        else:
            print("You win!")


class Player:
    def __init__(self, role):
        self.role = role
        self.hand = []

    def get_a_card(self, cards):
        """Get a random card from the deck"""
        card = cards.pop(random.randint(0, len(cards) - 1))

        print(f"The card is: {card}")
        self.hand.append(card)
        print(f"{self.role}'s hand: {sum(self.hand)}")


if __name__ == "__main__":
    play_blackjack()
