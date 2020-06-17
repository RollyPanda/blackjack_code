import random

class Card:
    """Card class represents a basic playing card. The card has a suit and a rank"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    """Deck class represents a collection of cards. It contains 52 unique cards (exclude red/black Jokers)"""

    def __init__(self):
        cards = []
        for i in ["Spades", "Hearts", "Diamonds", "Clubs"]:
            for j in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
                cards.append((i, j))
        self.cards = cards

    """Shuffle the cards in a deck"""
    def shuffle(self):
        random.shuffle(self.cards)

    """The dealer deals cards from the deck to the players"""

    def deal(self):
        self.cards.pop(random.randint(0, len(self.cards) - 1))

    def __str__(self):
        self.shuffle()
        return "\n".join([str(card) for card in self.cards])

class Hand:
    """Hand class represents cards on each player’s hand. It defines scores of each player"""

    def __init__(self):
        self.cards = []
        self.total_value = 0  # Total value of a hand
        self.ace_count = 0  # Tracking number of aces used as 11

    def add_card(self, card):
        """
        Whenever a card is added to the hand, the value will be calculated. For each 'ACE' card, treat it as 11.
        While the total value is over 21, subtract 10 from the total value for each 'ACE' card, one by one
        :param card:
        :return:
        """
        if card.rank == "A":
            self.cards.append("A")
            self.total_value += 11
            self.ace_count += 1
            if self.total_value > 21:
                self.total_value -= 10
        elif card.rank in [2, 3, 4, 5, 6, 7, 8, 9]:
            self.cards.append(card.rank)
            self.total_value += int(card.rank)
        elif card.rank in [10, "J", "Q", "K"]:
            self.cards.append(card.rank)
            self.total_value += 10
        else:
            self.cards.append(card.rank)
            self.total_value += int(card.rank)

    def __str__(self):
        return "\n".join([str(card) for card in self.cards]) + f"\nTotal Value: {self.total_value}\n"

class Game:
    def play(self):
        while True:
            self.show_opening_statement()

            # Create a deck
            deck = Deck()

            # shuffle a deck
            deck.shuffle()

            # Deal two cards to each player
            player_hand = Hand()
            dealer_hand = Hand()

            for _ in range(2):
                player_hand.add_card(deck.deal())
                dealer_hand.add_card(deck.deal())

            # Show player's cards
            self.show_cards(player_hand)

            # Show Dealer's cards
            self.show_cards(dealer_hand, is_dealer=True, hide_first=True)

            game_over = False
            while not game_over:  # play game until game over
                # The player can make a choice to hit(ask for another card) or stand(stop asking for more cards)
                choice = self.get_user_command("\nPlease enter 'hit' or 'stand' (or H/S) ", ["h", "s", "hit", "stand"])

                if choice in ['hit', 'h']:
                    #  player add cards
                    player_hand.add_card(deck.deal())
                    # if hand's value > 21, print a message and game over
                    if sum(player_hand) > 21:
                        print("Game Over!")
                else:
                    # Force dealer to hit while its value is less than 17
                    dealer_hand.add_card(deck.deal())

                    if sum(dealer_hand) > 21:
                        print("Game Over!")

                    self.show_final_results(player_hand.total_value, dealer_hand.total_value)
                    game_over = True

            # Ask the user whether he wants to play again
            play_again = self.get_user_command("Play Again? [Y/N] ", ["y", "n"])

            if play_again == "n":
                quit()

    def show_opening_statement(self):
        print("-------Welcome to Blackjack Game---------")
        print("\nGet as close to 21 as you can. A dealer hits until he reaches 17. Aces count as 1 or 11\n")

    """ Display the final game results """
    def show_final_results(self, player_hand_value, dealer_hand_value):
        print("Final Results")
        print("Your hand:", player_hand_value)
        print("Dealer's hand:", dealer_hand_value)

        if player_hand_value > dealer_hand_value:
            print("You Win!")
        elif player_hand_value == dealer_hand_value:
            print("Tie!")
        else:
            print("You Lost!")

    """
    Let the user to select a command from the command list with a prompt message
    """
    def get_user_command(self, prompt_message, command_list):
        choice = input(prompt_message).lower()
        while choice not in command_list:
            choice = input(prompt_message).lower()
        return choice

    """ The first card of a deal is hidden """
    def show_cards(self, hand, is_dealer=False, hide_first=False):
        if is_dealer:
            print("Dealer's Hand: ")
        else:
            print("Your Hand: ")

        if hide_first:
            print(" <Card Hidden> ")
            print(hand.cards[1])
        else:
            print(hand)

# Entry point of the program
if __name__ == "__main__":
    Game()