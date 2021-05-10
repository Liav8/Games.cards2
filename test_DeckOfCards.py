from unittest import TestCase
from DeckOfCards import *


class TestDeckOfCards(TestCase):
    def setUp(self):
        print("A setup has been done!--------")
        self.d1 = DeckOfCards()

    # לבדוק האם יש בחפיסה 52 קלפים
    def test_has_52(self):
        self.assertEqual(len(self.d1.cards), 52)

    # בדיקה שאין כפילויות בחפיסה
    def test_is_dif(self):
        while self.d1.cards != []:
            c1 = self.d1.deal_one()
            for card in self.d1.cards:
                self.assertNotEqual(c1, card)

    # בידקת שהפעולה מערבבת את החפיסה ומשנה אותו
    def test_shuffle(self):
        self.d1.shuffle()
        d2 = DeckOfCards()
        self.assertNotEqual(self.d1.cards, d2.cards)

    def test_repr(self):
        self.assertEqual(f"This deck's cards are: {self.d1.cards}", repr(self.d1))

    def test_show(self):
        self.assertEqual(f"This deck's cards are: {self.d1.cards}", repr(self.d1))

    # בדיקת תקינותעל חפיסה ריקה
    def test_deal_one(self):
        for i in range(52):
            self.d1.deal_one()
        print(self.d1.cards)
        self.assertFalse(self.d1.deal_one())
