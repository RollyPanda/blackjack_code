
import unittest

from main import Card


class CardTest(unittest.TestCase):

    def test_card_initialization(self):
        card1 = Card("Spades", "8")
        self.assertEqual(str(card1), "8 of Spades")

        card2 = Card("Diamonds", "King")
        self.assertEqual(str(card2), "King of Diamonds")

        card3 = Card("Hearts", "Ace")
        self.assertEqual(str(card3), "Ace of Hearts")

        card4 = Card("Clubs", "5")
        self.assertEqual(str(card4), "5 of Clubs")


if __name__ == '__main__':
    unittest.main()