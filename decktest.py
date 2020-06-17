import unittest

from main import Deck


class DeckTest(unittest.TestCase):

    def test_deck_initialization(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_deal(self):
        deck = Deck()
        deck.deal()
        self.assertEqual(len(deck.cards), 51)

    def test_deck_dealHalf(self):
        deck = Deck()
        for i in range(1, 38):
            deck.deal()
        self.assertEqual(len(deck.cards), 15)

    def test_deck_shuffle(self):
        deck1, deck2, deck3 = Deck(), Deck(), Deck()

        deck1.shuffle()
        deck2.shuffle()
        deck3.shuffle()

        card1 = deck1.cards.pop(0)
        card2 = deck2.cards.pop(0)
        card3 = deck3.cards.pop(0)

        if str(card1) == str(card2) and str(card1) == str(card3):
            self.fail("The decks were not shuffled well")


if __name__ == '__main__':
    unittest.main()