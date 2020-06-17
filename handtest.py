import unittest

from main import Hand, Card


class HandTest(unittest.TestCase):

    def test_hand_initialization(self):
        hand = Hand()
        self.assertEqual(len(hand.cards), 0)
        self.assertEqual(hand.total_value, 0)

    def test_hand_value1(self):
        players_hand = Hand()
        players_hand.add_card(Card("Clubs", "K"))
        players_hand.add_card(Card("Hearts", "3"))
        self.assertEqual(13, players_hand.total_value)

    def test_hand_value2(self):
        players_hand = Hand()
        players_hand.add_card(Card("Clubs", "K"))
        players_hand.add_card(Card("Hearts", "J"))
        self.assertEqual(20, players_hand.total_value)

    def test_hand_value3(self):
        players_hand = Hand()
        players_hand.add_card(Card("Spades", "2"))
        players_hand.add_card(Card("Hearts", "2"))
        players_hand.add_card(Card("Diamonds", "2"))
        players_hand.add_card(Card("Clubs", "2"))
        self.assertEqual(8, players_hand.total_value)

    def test_hand_value4(self):
        players_hand = Hand()
        players_hand.add_card(Card("Spades", "9"))
        players_hand.add_card(Card("Hearts", "9"))
        players_hand.add_card(Card("Diamonds", "9"))
        self.assertEqual(27, players_hand.total_value)

    def test_hand_ace1(self):
        players_hand = Hand()
        players_hand.add_card(Card("Clubs", "K"))
        players_hand.add_card(Card("Spades", "K"))
        players_hand.add_card(Card("Clubs", "A"))
        self.assertEqual(21, players_hand.total_value)

    def test_hand_ace2(self):
        players_hand = Hand()
        players_hand.add_card(Card("Clubs", "K"))
        players_hand.add_card(Card("Hearts", "A"))
        self.assertEqual(21, players_hand.total_value)

    def test_hand_ace3(self):
        players_hand = Hand()
        players_hand.add_card(Card("Clubs", "K"))
        players_hand.add_card(Card("Spades", "5"))
        players_hand.add_card(Card("Clubs", "A"))
        self.assertEqual(16, players_hand.total_value)

    def test_hand_ace4(self):
        players_hand = Hand()
        players_hand.add_card(Card("Clubs", "A"))
        players_hand.add_card(Card("Spades", "2"))
        self.assertEqual(13, players_hand.total_value)

    def test_hand_ace5(self):
        players_hand = Hand()
        players_hand.add_card(Card("Clubs", "A"))
        players_hand.add_card(Card("Diamonds", "A"))
        self.assertEqual(12, players_hand.total_value)


if __name__ == '__main__':
    unittest.main()